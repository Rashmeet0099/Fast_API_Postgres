# 📚 FastAPI Bookstore API with PostgreSQL

A backend RESTful API built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, providing CRUD functionality for a bookstore system. The application is modular, production-ready, and supports OpenAPI docs via Swagger UI.

---

## 🧠 Features

- 🚀 High-performance asynchronous FastAPI backend
- 🗄️ PostgreSQL database connectivity via SQLAlchemy ORM
- 📄 Automatic Swagger documentation at `/docs`
- 🛡️ Data validation using Pydantic
- 🧪 Easily extendable for authentication, pagination, etc.

---

## 🔧 Tech Stack

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-8A0707?style=for-the-badge)

---

## 📁 Folder Structure

ap_postgres/
├── api_postgres/
│ ├── init.py
│ ├── main.py # FastAPI app + endpoints
│ ├── models.py # SQLAlchemy DB models
│ ├── schemas.py # Pydantic schemas
│ ├── services.py # Business logic (CRUD)
│ └── db.py # DB connection/session
├── requirements.txt # All dependencies
└── README.md # 📘 You are here

yaml
Copy
Edit

---

## 📊 ER Diagram / Structure Flow

```mermaid
erDiagram
    Book {
        INT id PK
        STRING title
        STRING description
        STRING author
        INT year
    }
You can visualize this using Mermaid Live Editor.

🚀 Getting Started
📦 1. Clone the repository
bash
Copy
Edit
git clone https://github.com/<your-username>/fastapi-postgres-api.git
cd fastapi-postgres-api
📥 2. Create virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
📦 3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🗃️ 4. Configure PostgreSQL
Update db.py with your own credentials:

python
Copy
Edit
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost:5432/dbname"
🧱 5. Run migrations (optional step)
bash
Copy
Edit
# Already auto-creates tables in main.py using Base.metadata.create_all()
⚡ 6. Start server
bash
Copy
Edit
uvicorn api_postgres.main:app --reload
Go to:

arduino
Copy
Edit
http://127.0.0.1:8000/docs
📬 API Endpoints
Method	Endpoint	Description
GET	/books/	Get all books
POST	/books/	Create a new book

Example POST payload:

json
Copy
Edit
{
  "title": "AI Revolution",
  "author": "Rashmeet Singh",
  "description": "A guide to intelligent systems",
  "year": 2025
}
📸 Screenshots
Paste your Swagger UI or response screenshots here

🙌 Contributors
👨‍💻 Rashmeet Singh – Developer

📝 License
This project is licensed under the MIT License. Feel free to use and adapt.
