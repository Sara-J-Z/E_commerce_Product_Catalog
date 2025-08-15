🌸 Scentora Backend — Django REST API

![alt text](logo.png)

The Scentora Backend is a Django REST Framework API that powers the Scentora perfume and makeup store.
It provides secure authentication, CRUD functionality for products, brands, categories, and newsletter subscriptions, and serves as the data layer for the React frontend.

📖 Description

This backend is built with Django and Django REST Framework to provide a robust, scalable API for Scentora.
It includes a Custom User Model for flexible authentication, image uploads for brands and categories, and a structured database designed from an ERD.

🗂 ERD (Entity Relationship Diagram)



Models:

CustomUser — Stores user credentials and profile info.

Brand — Holds brand name and logo.

Category — Holds category name and icon.

Product — Linked to Brand & Category, stores product details and image.

Newsletter — Stores email addresses for newsletter subscriptions.

**Repository**:  
`git clone https://github.com/Sara-J-Z/E_commerce_Product_Catalog.git`  
`cd E_commerce_Product_Catalog/scentora_app`  


#### Installation:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Backend will run at:
`http://localhost:8000` 

🔑 API Endpoints
### 🧾 Authentication

| Method | Endpoint         | Description             |
|--------|------------------|-------------------------|
| POST   | `/api/register/` | Register a new user     |
| POST   | `/api/login/`    | Login and receive token |
| POST   | `/api/logout/`   | Logout user             |

---

### 🏷️ Brands

| Method | Endpoint             | Description        |
|--------|----------------------|--------------------|
| GET    | `/api/brands/`       | List all brands    |
| POST   | `/api/brands/`       | Create a new brand |
| GET    | `/api/brands/:id/`   | Retrieve brand     |
| PUT    | `/api/brands/:id/`   | Update brand       |
| DELETE | `/api/brands/:id/`   | Delete brand       |

---

### 🗂️ Categories

| Method | Endpoint                | Description           |
|--------|-------------------------|-----------------------|
| GET    | `/api/categories/`      | List all categories   |
| POST   | `/api/categories/`      | Create a new category |
| GET    | `/api/categories/:id/`  | Retrieve category     |
| PUT    | `/api/categories/:id/`  | Update category       |
| DELETE | `/api/categories/:id/`  | Delete category       |

---

### 💄 Products

| Method | Endpoint              | Description          |
|--------|-----------------------|----------------------|
| GET    | `/api/products/`      | List all products    |
| POST   | `/api/products/`      | Create a new product |
| GET    | `/api/products/:id/`  | Retrieve product     |
| PUT    | `/api/products/:id/`  | Update product       |
| DELETE | `/api/products/:id/`  | Delete product       |

---

### 📨 Newsletter

| Method | Endpoint                   | Description             |
|--------|----------------------------|-------------------------|
| GET    | `/api/newsletter/`         | List all subscribers    |
| POST   | `/api/newsletter/`         | Add subscriber          |
| DELETE | `/api/newsletter/:id/`     | Remove subscription     |


## 🛠 Technologies Used

- [Python 3](https://www.python.org/)  
- [Django](https://www.djangoproject.com/) — Web framework  
- [Django REST Framework](https://www.django-rest-framework.org/) — API layer  
- [Pillow](https://python-pillow.org/) — Image uploads  
- [django-cors-headers](https://pypi.org/project/django-cors-headers/) — CORS handling  
- **SQLite / PostgreSQL** — Databases


📚 Attributions

Django — Web framework

DRF — API framework

Pillow — Image handling

🔮 Next Steps

- Implement order & payment models.

- Add pagination to API endpoints.