# ROSAI Database Architecture

Version : 1.0

Author : Jatin Naik

Project :
AI Powered Restaurant Operating System

---

# Objectives

Build an AI-powered Restaurant Operating System capable of

- Restaurant Management
- Staff Management
- Sales Analytics
- Expense Tracking
- Inventory Management
- Forecasting
- AI Decision Support
- Multi Restaurant Support
- Multi Country Support

---

# Technology Stack

Frontend

- React
- TailwindCSS

Backend

- FastAPI

Database

- PostgreSQL

ORM

- SQLAlchemy

Authentication

- JWT

AI

- LangGraph
- LangChain
- OpenAI / Anthropic

Deployment

- Docker

# Database Principles

The database is designed using Third Normal Form (3NF).

Every operational table supports CRUD operations.

Every business entity belongs to a Restaurant.

Restaurant is the tenant.

Client owns Restaurants.

Users belong to Restaurants.

Orders belong to Restaurants.

Sales belong to Orders.

AI never writes into operational tables.

AI only reads operational tables and writes predictions into AI tables.

Soft delete is preferred over hard delete.


# Folder Structure

src/

database/

generators/

utils/

api/

models/

schemas/

services/

tests/

docs/


# Naming Convention

Primary Key

id

Foreign Keys

restaurant_id

client_id

user_id

order_id

customer_id

supplier_id

menu_item_id

expense_id

cashup_id


# Audit Fields

Every table contains

created_at

updated_at

status

Optional

deleted_at
