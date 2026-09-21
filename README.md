# 🍔 Burger App: Document Database (Part 1 of NoSQL Series)

## 📌 Project Overview
This repository is part of a larger Data Engineering portfolio series demonstrating **Polyglot Persistence**. 

After completing a traditional SQL Data Warehouse in a previous repository, this project focuses specifically on **Document-based NoSQL Databases**. We use it to manage flexible, hierarchical data like burger menus, complex ingredients, and pricing without the constraints of relational tables.

*Note: This is Repository 2 of 6 in the complete Burger Data Ecosystem Architecture.*

## 🗺️ The Burger Data Ecosystem Series
1. ✅ **SQL Data Warehouse** (Completed in separate repo)
2. 🟢 **Document DB** (This Repo - DataStax Astra DB)
3. ⏳ **Key-Value DB** (Redis - Upcoming)
4. ⏳ **Wide-Column DB** (Cassandra - Upcoming)
5. ⏳ **Graph DB** (Neo4j - Upcoming)
6. ⏳ **The Integrator** (Orchestrating the 4 NoSQL databases together)

## 🎯 Project Objectives
The goal of this specific repository is to act as a standalone **Data Store** and provide a Python-based library/module to interact with the data:
* Setup the `BURGER` Keyspace and `burger_info` Collection in Astra DB.
* Establish secure connectivity using DataStax API Gateways (Stargate) and `.env`.
* Build Python functions to handle JSON data ingestion, extraction, and updates (CRUD operations).

## 🛠️ Tech Stack
* **Database:** DataStax Astra DB (Serverless Document API)
* **Language:** Python 3
* **Libraries:** `astrapy`, `python-dotenv`

## 🚀 Setup & Installation
1. Clone the repo:
   ```bash
   git clone [https://github.com/your-username/burger-app-document-db.git](https://github.com/your-username/burger-app-document-db.git)
