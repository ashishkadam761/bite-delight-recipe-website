import os
import requests
import json

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash

print("THIS IS THE ACTIVE APP FILE")

app = Flask(__name__)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")          # app password from Gmail

mail = Mail(app)

app.secret_key = "bitedelight_secret_key"
import os

print("STATIC FOLDER PATH:", app.static_folder)
print("TEMPLATE FOLDER PATH:", app.template_folder)

# Database setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'recipes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# Recipe model
class Recipe(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    image = db.Column(db.String(150))

    ingredients = db.Column(db.Text, nullable=False)

    steps = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# User model (for login system)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    recipes = db.relationship('Recipe', backref='author', lazy=True)


def fetch_and_store_recipes():
    
    categories_url = "https://www.themealdb.com/api/json/v1/1/categories.php"
    categories_resp = requests.get(categories_url).json()

    categories = [c['strCategory'] for c in categories_resp['categories']]

    for category in categories:

        meals_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}"
        meals_resp = requests.get(meals_url).json()
        meals = meals_resp.get("meals", [])

        for meal in meals:

            meal_id = meal['idMeal']

            detail_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
            detail_resp = requests.get(detail_url).json()
            details = detail_resp.get("meals")[0]

            ingredients_list = []

            for i in range(1, 21):

                ingredient = details.get(f"strIngredient{i}")
                measure = details.get(f"strMeasure{i}")

                if ingredient and ingredient.strip():
                    ingredients_list.append(f"{measure} {ingredient}")

            ingredients_text = "\n".join(ingredients_list)

            if Recipe.query.filter_by(title=details['strMeal']).first():
                continue

            new_recipe = Recipe(
                title=details['strMeal'],
                ingredients=ingredients_text,
                steps=details['strInstructions'],
                image=details['strMealThumb'],
                user_id=None
            )

            db.session.add(new_recipe)

        db.session.commit()
   
    print("Recipes fetched successfully!")


def import_indian_recipes():

    json_path = "indian_recipes.json"

    if not os.path.exists(json_path):
        print("Indian dataset not found")
        return

    with open(json_path, "r", encoding="utf-8") as file:
        recipes = json.load(file)

    for recipe in recipes:

        existing = Recipe.query.filter_by(title=recipe["title"]).first()

        if not existing:

            new_recipe = Recipe(
                title=recipe["title"],
                ingredients=recipe["ingredients"],
                steps=recipe["steps"],
                image=recipe["image"],
                user_id=None
            )

            db.session.add(new_recipe)

    db.session.commit()

    print("Indian recipes imported successfully!")


       
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/send_contact", methods=["POST"])
def send_contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Compose email
    msg = Message(
        subject=f"New Contact Message from {name}",
        sender=email,
        recipients=["kadamashish720@gmail.com"],  # your email
        body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    )

    try:
        mail.send(msg)
        return render_template("contact.html", success=True)
    except Exception as e:
        print("Error sending email:", e)
        return render_template("contact.html", success=False)

@app.route("/add", methods=["GET", "POST"])
def add_recipe():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        title = request.form['title']
        ingredients = request.form['ingredients']
        steps = request.form['steps']

        image_file = request.files.get('image')
        image_filename = None

        if image_file and image_file.filename != "":
            from werkzeug.utils import secure_filename
            image_filename = secure_filename(image_file.filename)

            upload_folder = os.path.join(app.root_path, 'static', 'uploads')
            os.makedirs(upload_folder, exist_ok=True)

            image_path = os.path.join(upload_folder, image_filename)
            image_file.save(image_path)

        new_recipe = Recipe(
    title=title,
    ingredients=ingredients,
    steps=steps,
    image=image_filename,
    user_id=session["user_id"]
)

        db.session.add(new_recipe)
        db.session.commit()

        return redirect(url_for("recipes"))

    return render_template("add_recipe.html")

@app.route("/recipes")
def recipes():

    recipes = Recipe.query.all()

    my_recipes = []

    if "user_id" in session:
        my_recipes = Recipe.query.filter_by(user_id=session["user_id"]).all()

    return render_template(
        "recipes.html",
        recipes=recipes,
        my_recipes=my_recipes
    )

@app.route("/search")
def search():

    query = request.args.get("query")

    if not query:
        return redirect(url_for("home"))

    # Search in local database first
    recipes = Recipe.query.filter(
        Recipe.title.ilike(f"%{query}%") |
        Recipe.ingredients.ilike(f"%{query}%")
    ).all()

    # If found in database
    if recipes:
        return render_template("recipes.html", recipes=recipes)

    # If not found → fetch from API
    api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"

    response = requests.get(api_url)
    data = response.json()

    if data["meals"]:

        for meal in data["meals"]:

            ingredients_list = []

            for i in range(1, 21):

                ingredient = meal.get(f"strIngredient{i}")
                measure = meal.get(f"strMeasure{i}")

                if ingredient and ingredient.strip():

                    ingredients_list.append(
                        f"{measure} {ingredient}".strip()
                    )

            ingredients_text = "\n".join(ingredients_list)

            new_recipe = Recipe(
                title=meal["strMeal"],
                image=None,
                ingredients=ingredients_text,
                steps=meal["strInstructions"],
                user_id=None
            )

            db.session.add(new_recipe)

        db.session.commit()

        recipes = Recipe.query.filter(
            Recipe.title.ilike(f"%{query}%")
        ).all()

        return render_template("recipes.html", recipes=recipes)

    return render_template("recipes.html", recipes=[])



@app.route("/delete/<int:id>")
def delete_recipe(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    recipe = Recipe.query.get_or_404(id)

    # Only allow owner to delete
    if recipe.user_id != session.get("user_id"):
        return "Unauthorized action", 403

    db.session.delete(recipe)
    db.session.commit()

    return redirect(url_for("recipes"))


@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            session["user_id"] = user.id
            session["user_name"] = user.name

            return redirect(url_for("home"))

        else:
            return "Invalid email or password"

    return render_template("login.html")

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))



@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/import-recipes")
def import_recipes():

    fetch_and_store_recipes()
    import_indian_recipes()

    return "Recipes imported successfully!"




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=True)
