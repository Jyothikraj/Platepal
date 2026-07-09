# 🍽️ PlatePal

PlatePal is a full-stack recipe discovery web application built with Django and Django REST Framework. It allows users to browse recipes, search meals, view detailed cooking instructions, save favorite recipes, and leave ratings and reviews.

---

## ✨ Features

- 🔐 User Authentication (Register, Login & Logout)
- 🍽️ Browse Popular Recipes
- 🔍 Search Recipes
- 📖 Detailed Recipe Pages
- ❤️ Add & View Favorite Recipes
- ⭐ Rate & Review Recipes
- 📱 Responsive Bootstrap UI
- 🌐 Integration with TheMealDB API
- 🔑 JWT Authentication for REST APIs
- 📄 RESTful API Endpoints

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- Bootstrap 5
- HTML5
- CSS3
- TheMealDB API

---

## 📂 Project Structure

```
platepal/
│── favorites/
│── recipes/
│── reviews/
│── users/
│── static/
│── templates/
│── platepal/
│── manage.py
│── requirements.txt
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Jyothikraj/Platepal.git
```

Move into the project:

```bash
cd Platepal
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

Add screenshots here.

Example:

```
screenshots/
├── home.png
├── recipe-detail.png
├── favorites.png
├── reviews.png
├── login.png
```

---

## 📚 REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/recipes/` | List recipes |
| GET | `/api/recipes/<id>/` | Recipe details |
| GET | `/api/recipes/search/?q=` | Search recipes |
| GET | `/api/favorites/` | User favorites |
| POST | `/api/favorites/` | Add favorite |
| GET | `/api/reviews/?recipe_id=` | Recipe reviews |
| POST | `/api/reviews/` | Create review |

---

## 📖 Learning Outcomes

This project helped me gain practical experience with:

- Django
- Django REST Framework
- REST API Development
- User Authentication
- CRUD Operations
- External API Integration
- Bootstrap UI Development
- Git & GitHub

---

## 👨‍💻 Author

**Srinivasan Jyothik Raj**

GitHub: https://github.com/Jyothikraj

---

## 📄 License

This project is developed for learning and portfolio purposes.
