# BiteDelight | Recipe Sharing Website

BiteDelight is a **full-stack recipe sharing platform** built using **Flask** where users can explore, add, and search recipes easily. The website provides a smooth, modern interface with interactive features that make finding and sharing recipes intuitive and fun.

---

## 🌟 Features

- **User Registration and Login**  
  Secure login system for users to manage their recipes.

- **Add New Recipes with Images**  
  Users can add recipes with title, ingredients, steps, and images.

- **Search Recipes**  
  Search recipes by **name** or **ingredients**. Results are displayed in a card layout.

- **Recipe Slider on Homepage**  
  Featured recipes appear in a horizontal slider for easy browsing.

- **API-based Recipe Integration**  
  Integrates with **TheMealDB API** to fetch additional recipes dynamically.

- **Responsive Design**  
  Works well on both **desktop** and **mobile** devices.

- **Contact Form**  
  Users can send messages to the admin via email using **Flask-Mail**.

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Backend programming language |
| **Flask** | Web framework for routing, templates, and API calls |
| **Flask-Mail** | Sending contact form emails |
| **HTML / CSS / JavaScript** | Frontend structure, styling, and interactivity |
| **SQLite** | Local database for users and recipes |
| **SQLAlchemy** | ORM to interact with SQLite in Python |
| **TheMealDB API** | Fetch additional recipes dynamically |
| **Werkzeug** | Secure file handling for image uploads |

---

## 📂 Project Structure
BiteDelight/
│
├─ app.py # Main Flask app
├─ recipes.db # SQLite database
├─ static/
│ ├─ css/ # Stylesheets
│ ├─ js/ # JavaScript files (slider, search)
│ ├─ images/ # Default/placeholder images
│ └─ uploads/ # User uploaded images
├─ templates/ # HTML templates
│ ├─ index.html
│ ├─ recipes.html
│ ├─ add_recipe.html
│ ├─ contact.html
│ ├─ login.html
│ └─ register.html
└─ README.md


---

## ⚙ How It Works

1. Users register and log in to access recipe features.  
2. Recipes can be added with ingredients, steps, and images.  
3. Search finds recipes from the database or TheMealDB API.  
4. Featured recipes appear in a horizontal slider on the homepage.  
5. Contact form allows users to send messages to admin email.

---

## 💻 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/bite-delight-recipe-website.git
   
2.Enter project folder:

    cd bite-delight-recipe-website

3.Create a virtual environment and activate it:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

4.Install dependencies:

pip install -r requirements.txt

5.Run the app:

python app.py

6.Open browser at:

http://127.0.0.1:5000


Screenshots of the Site
<img width="1920" height="1080" alt="Screenshot (60)" src="https://github.com/user-attachments/assets/bf561db1-eff7-4bb0-b843-f00ce132d362" />
<img width="1920" height="1080" alt="Screenshot (59)" src="https://github.com/user-attachments/assets/abcf550d-e097-467d-b71a-1f1ac7595f07" />
<img width="1920" height="1080" alt="Screenshot (58)" src="https://github.com/user-attachments/assets/8d4c8339-4f87-4556-ba1d-c527f3a2a3a5" />
<img width="1920" height="1080" alt="Screenshot (57)" src="https://github.com/user-attachments/assets/def7c2db-a77a-402c-b5f1-04111d1e18b8" />
<img width="1920" height="1080" alt="Screenshot (56)" src="https://github.com/user-attachments/assets/5a0b8795-5b15-4f08-8e84-41e5989d3497" />
<img width="1920" height="1080" alt="Screenshot (55)" src="https://github.com/user-attachments/assets/41e03647-add9-4162-9c30-526e3c9cc582" />
<img width="1920" height="1080" alt="Screenshot (54)" src="https://github.com/user-attachments/assets/a7d0162a-8df2-4482-aef2-ea02508e9f84" />
<img width="1920" height="1080" alt="Screenshot (53)" src="https://github.com/user-attachments/assets/1ed61948-e54e-4c28-8e29-b3c71083a7e3" />
<img width="1920" height="1080" alt="Screenshot (52)" src="https://github.com/user-attachments/assets/b953e4e5-6a26-4376-958e-435436ecc7bc" />
<img width="1920" height="1080" alt="Screenshot (51)" src="https://github.com/user-attachments/assets/546c406b-7609-4d94-894b-1b1d7fe2ef59" />
<img width="1920" height="1080" alt="Screenshot (50)" src="https://github.com/user-attachments/assets/99e31b0a-a160-4d54-ad1b-24262cfb430e" />
<img width="1920" height="1080" alt="Screenshot (66)" src="https://github.com/user-attachments/assets/9f2af96a-7ba1-436d-b7f6-1e5de9a982ed" />
<img width="1920" height="1080" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/809c3a91-a854-42ec-bb78-0b387743edbf" />
<img width="1920" height="1080" alt="Screenshot (64)" src="https://github.com/user-attachments/assets/6eb76556-d095-4c32-b6ce-6808252444a7" />
<img width="1920" height="1080" alt="Screenshot (63)" src="https://github.com/user-attachments/assets/004c3f96-9e06-461e-8a42-c8dae350c0a5" />
<img width="1920" height="1080" alt="Screenshot (62)" src="https://github.com/user-attachments/assets/34bd6eb9-e737-439e-b1ae-89e07534de1c" />
<img width="1920" height="1080" alt="Screenshot (61)" src="https://github.com/user-attachments/assets/7903816f-d18f-4cba-9f18-0430127cd676" />
