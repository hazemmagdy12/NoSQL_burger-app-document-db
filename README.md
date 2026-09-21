# 🍔 Burger Recommendation Data Platform

## 📌 Project Overview
A robust, NoSQL-first backend infrastructure designed to power a real-time Burger Recommendation System. This project demonstrates modern data engineering practices by utilizing a Document-based database to handle flexible schemas for menus, ingredients, and user interactions.

## 🏗️ Architecture & Tech Stack
* **Database:** DataStax Astra DB (Serverless NoSQL based on Apache Cassandra).
* **Language:** Python 3.
* **SDK/Driver:** `astrapy` for interacting with the Stargate API Gateway.
* **Data Model:** Document-oriented (JSON) to efficiently store and query hierarchical burger catalogs.

## 🚀 Current Implementation (Phase 1: Document Persistence)
* Designed the `burgers` Keyspace and `burger_info` Collection.
* Established secure, token-based connection via `dotenv` and `astrapy`.
* Implemented core CRUD operations for menu items, including complex nested JSON documents (ingredients, locations, pricing).

## 🔮 Roadmap: The Polyglot Persistence Vision
As the application scales, the architecture will evolve into a Polyglot Persistence model:
1. **Document (Current):** Astra DB for core catalog and menu items.
2. **Key-Value (Future):** Redis for blazing-fast user session and cart management.
3. **Wide-Column (Future):** Cassandra for high-throughput user activity tracking (clicks, orders).
4. **Graph (Future):** Neo4j for deep recommendation engines (User A likes X, similar to User B).

## 🛠️ Setup & Installation
1. Clone the repo: `git clone https://github.com/your-username/Burger-Recommendation-Data-Platform.git`
2. Create virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file and add your Astra DB Token:
   ```env
   ASTRA_DB_TOKEN="your_secure_token_here"
