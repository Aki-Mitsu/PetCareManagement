# 🐾 Pet Care Management System

An Object-Oriented Python Database Management System (DBMS) backed by MySQL for managing users, pet profiles across multiple species, and pet care records.

## ✨ Features
* **Object-Oriented Pet Models:** Structured base `Pet` class with dedicated species models for **Cats**, **Dogs**, **Hamsters**, and **Rabbits**.
* **User Management:** Account creation, authentication, and owner record handling via `UserManager` and `User` models[cite: 3].
* **Pet Management:** Register, view, update, and manage pet records via `PetManager`[cite: 3].
* **Persistent MySQL Storage:** Centralized database connection and CRUD operations handled through `DBHandler` (`mysql-connector-python`)[cite: 3].

## 🛠️ Tech Stack
* **Language:** Python 3
* **Database:** MySQL
* **Driver:** `mysql-connector-python`

## 📂 Project Structure
```text
PetCareManagement/
├── main.py                  # Application entry point[cite: 3]
├── models/
│   ├── pet.py               # Base Pet class[cite: 3]
│   ├── cat.py               # Cat model[cite: 3]
│   ├── dog.py               # Dog model[cite: 3]
│   ├── hamster.py           # Hamster model[cite: 3]
│   ├── rabbit.py            # Rabbit model[cite: 3]
│   └── user.py              # User model[cite: 3]
├── system/
│   ├── db_handler.py        # MySQL connection and query execution[cite: 3]
│   ├── pet_manager.py       # Pet CRUD and business logic[cite: 3]
│   └── user_manager.py      # User management and authentication logic[cite: 3]
└── README.md
