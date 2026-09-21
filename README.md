# 🍔 Burger App: Document Database (Phase 1 of NoSQL Series)

## 📌 Project Overview
This repository is the first phase of a larger Data Engineering portfolio series demonstrating **Polyglot Persistence**. 

This specific project focuses on **Document-based NoSQL Databases** using DataStax Astra DB. It serves as the core Data Store to manage flexible, hierarchical data like burger menus, complex ingredients, and pricing without the constraints of relational tables.

## 🗺️ The Polyglot Data Ecosystem Roadmap
To build a highly scalable Burger Recommendation System, the architecture is divided into the following phases:
1. 🟢 **Phase 1: Document DB** (This Repo - Astra DB for core catalog and menus).
2. ⏳ **Phase 2: Key-Value DB** (Redis for shopping carts and sessions).
3. ⏳ **Phase 3: Wide-Column DB** (Cassandra for user activity tracking).
4. ⏳ **Phase 4: Graph DB** (Neo4j for AI recommendation engine).
5. ⏳ **Phase 5: The Integrator** (Orchestrating the databases together).

## 🏗️ Project Architecture (Modular Design)
The code is structured into a modular Python application following software engineering best practices:
* `database.py`: Handles secure connection and authentication with Astra DB using `.env`.
* `crud.py`: The core Data Store module containing pure functions for Create, Read, Update, and Delete operations.
* `main.py`: The execution script that imports the CRUD module to test and run the data pipeline.

## 🛠️ Tech Stack
* **Database:** DataStax Astra DB (Serverless Document API)
* **Language:** Python 3
* **Libraries:** `astrapy`, `python-dotenv`

## 🚀 Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hazemmagdy12/burger-app-document-db.git
   
   python -m venv venv
pip install astrapy python-dotenv

ASTRA_DB_TOKEN="your_secure_token_here"

python main.py
