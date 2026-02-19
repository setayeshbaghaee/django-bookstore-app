# 📚 Django Bookstore Management System

## 📌 Project Overview

This project is a web-based bookstore management system built with Django.  
I developed this application to gain hands-on experience in backend development, relational database modeling, and implementing real-world business logic using Django.

The platform simulates a real bookstore environment where:

- Customers can browse books, add them to their cart, and place orders.
- Managers and employees can manage stores, books, and operational data through the Django Admin panel.

The main focus of this project was understanding how to properly structure a Django application and translate business rules into clean backend logic.


##  Technologies Used

- **Python**
- **Django**
- **SQLite** (default development database)
- **HTML / CSS**
- **Django ORM**
- **Django Admin**

These technologies allowed rapid development while keeping the system scalable and maintainable.


##  User Roles & Access Control

The system supports multiple user roles:

###  Customer
- Browse available books  
- Add books to cart  
- Place orders  
- View order history  

###  Employee
- Assigned to a specific store  
- Manage store-related data  

###  Manager
- Full administrative control over stores  
- Manage employees  
- Oversee operational data  

Role-based access control ensures that each user only accesses the features relevant to their responsibilities.


## Core Features

- User registration and authentication  
- Role-based permission handling  
- Book creation, editing, and deletion  
- Inventory tracking  
- Store and employee management  
- Shopping cart functionality  
- Order placement and status tracking  
- Discount code logic  
- Notification/announcement capability  
- Full backend management via Django Admin  


##  Project Architecture

The project follows Django’s app-based architecture.  
Each responsibility is separated into its own application to keep the codebase organized and scalable.

django-bookstore-app/
│
├── accounts/ # User management
├── bookstore/ # Book models and logic
├── cart/ # Shopping cart functionality
├── orders/ # Order management
├── store/ # Store and employee management
├── core/ # Shared logic and configurations
├── media/ # Uploaded images
└── manage.py


This modular structure makes future expansion and maintenance easier.

Particular attention was given to:
- Keeping business logic inside models and views  
- Avoiding unnecessary duplication  
- Maintaining relational integrity using ForeignKey and ManyToMany fields  


## Database & Model Design

The database schema was carefully designed to:

- Maintain referential integrity  
- Separate responsibilities across models  
- Implement role-based permissions clearly  
- Support future scalability  

Django ORM was heavily used to define relationships and enforce constraints cleanly.


## ▶️ How to Run
```bash
git clone https://github.com/setayeshbaghaee/django-bookstore-app
cd django-bookstore-app
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```


##  What I Learned

Through building this project, I strengthened my understanding of:

- Designing relational models in Django  
- Implementing business logic beyond simple CRUD  
- Structuring medium-sized Django applications  
- Managing authentication and role-based permissions  
- Thinking about system behavior, not just individual features  

---

## Future Improvements

In future iterations, I plan to:

- Convert the system into a RESTful API using **Django REST Framework**
- Implement **JWT-based authentication**
- Integrate a real **payment gateway**
- Containerize the project using **Docker**
- Deploy the project to a production environment

---

## 📌 Author

Setayesh Baghaee
Computer Engineering Student
