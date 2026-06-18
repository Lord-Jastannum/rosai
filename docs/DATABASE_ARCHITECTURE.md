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

# Master Tables

---

## 1. Countries

Purpose

Stores supported countries.

Primary Key

id

Columns

| Column | Type | Nullable |
|----------|----------|----------|
| id | INTEGER | NO |
| name | VARCHAR(100) | NO |
| iso_code | VARCHAR(5) | NO |
| currency_code | VARCHAR(5) | NO |
| created_at | TIMESTAMP | YES |
| updated_at | TIMESTAMP | YES |

---

## 2. Currencies

Purpose

Stores currency information.

Primary Key

id

Columns

| Column | Type |
|----------|----------|
| id | INTEGER |
| currency_name | VARCHAR(100) |
| currency_code | VARCHAR(10) |
| currency_symbol | VARCHAR(10) |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

## 3. Subscriptions

Purpose

Restaurant subscription plans.

Primary Key

subscription_id

Columns

| Column | Type |
|----------|----------|
| subscription_id | INTEGER |
| plan_name | VARCHAR(50) |
| monthly_price | DECIMAL |
| currency | VARCHAR(5) |
| max_restaurants | INTEGER |
| max_users | INTEGER |
| analytics | BOOLEAN |
| ai_features | BOOLEAN |
| support_level | VARCHAR(100) |
| status | VARCHAR(20) |

---

## 4. Clients

Purpose

Restaurant companies.

Primary Key

client_id

Foreign Keys

subscription_id

Columns

| Column | Type |
|----------|----------|
| client_id | INTEGER |
| client_name | VARCHAR(200) |
| industry | VARCHAR(100) |
| country | VARCHAR(100) |
| currency | VARCHAR(5) |
| language | VARCHAR(30) |
| timezone | VARCHAR(60) |
| subscription_id | INTEGER |
| registration_number | VARCHAR(50) |
| vat_number | VARCHAR(50) |
| financial_year_start | VARCHAR(20) |
| status | VARCHAR(20) |
| activation_date | DATE |
| inactivation_date | DATE |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

## 5. Primary Contacts

Purpose

Primary contact person for each client.

Primary Key

contact_id

Foreign Key

client_id

Columns

| Column | Type |
|----------|----------|
| contact_id | INTEGER |
| client_id | INTEGER |
| first_name | VARCHAR(100) |
| last_name | VARCHAR(100) |
| designation | VARCHAR(100) |
| email | VARCHAR(200) |
| phone | VARCHAR(30) |
| secondary_phone | VARCHAR(30) |
| preferred_contact_method | VARCHAR(30) |
| verified | BOOLEAN |
| status | VARCHAR(20) |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

## 6. Restaurants

Purpose

Restaurant branches.

Primary Key

restaurant_id

Foreign Key

client_id

Columns

| Column | Type |
|----------|----------|
| restaurant_id | INTEGER |
| client_id | INTEGER |
| restaurant_name | VARCHAR(200) |
| restaurant_type | VARCHAR(50) |
| cuisine | VARCHAR(100) |
| country | VARCHAR(50) |
| currency | VARCHAR(10) |
| city | VARCHAR(100) |
| postcode | VARCHAR(20) |
| address | TEXT |
| phone | VARCHAR(30) |
| email | VARCHAR(200) |
| opening_time | TIME |
| closing_time | TIME |
| seating_capacity | INTEGER |
| delivery_available | BOOLEAN |
| takeaway_available | BOOLEAN |
| average_daily_customers | INTEGER |
| rating | DECIMAL(2,1) |
| status | VARCHAR(20) |
| activation_date | DATE |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

## 7. Departments

Purpose

Employee departments.

Primary Key

id

Columns

id

name

created_at

updated_at

---

## 8. Roles

Purpose

Employee roles.

Primary Key

id

Columns

id

name

guard_name

created_at

updated_at

---

## 9. Users

Purpose

Restaurant employees.

Primary Key

user_id

Foreign Keys

restaurant_id

department_id

role_id

Columns

| Column | Type |
|----------|----------|
| user_id | INTEGER |
| restaurant_id | INTEGER |
| department_id | INTEGER |
| role_id | INTEGER |
| first_name | VARCHAR(100) |
| last_name | VARCHAR(100) |
| gender | VARCHAR(20) |
| email | VARCHAR(200) |
| phone | VARCHAR(30) |
| employment_type | VARCHAR(30) |
| salary | DECIMAL |
| joining_date | DATE |
| status | VARCHAR(20) |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

## 10. PDQ Machines

Purpose

Card payment terminals.

Primary Key

machine_id

Foreign Key

restaurant_id

Columns

machine_id

restaurant_id

provider

serial_number

installation_date

status

created_at

updated_at

# Transaction Tables

---

## 11. Customers

Purpose

Stores customer information for loyalty, analytics and AI.

Primary Key

customer_id

Foreign Key

restaurant_id

Columns

| Column | Type |
|----------|----------|
| customer_id | INTEGER |
| restaurant_id | INTEGER |
| first_name | VARCHAR(100) |
| last_name | VARCHAR(100) |
| email | VARCHAR(200) |
| phone | VARCHAR(30) |
| gender | VARCHAR(20) |
| dob | DATE |
| loyalty_points | INTEGER |
| vip_status | BOOLEAN |
| join_date | DATE |
| last_visit | DATE |
| status | VARCHAR(20) |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

## 12. Orders

Purpose

Stores every customer order.

Primary Key

order_id

Foreign Keys

restaurant_id

customer_id

user_id

Columns

| Column | Type |
|----------|----------|
| order_id | BIGINT |
| restaurant_id | INTEGER |
| customer_id | INTEGER |
| user_id | INTEGER |
| order_datetime | TIMESTAMP |
| order_type | VARCHAR(30) |
| order_status | VARCHAR(30) |
| subtotal | DECIMAL |
| discount | DECIMAL |
| tax | DECIMAL |
| total_amount | DECIMAL |
| payment_status | VARCHAR(30) |
| created_at | TIMESTAMP |
| updated_at | TIMESTAMP |

---

## 13. Order Items

Purpose

Stores products inside each order.

Primary Key

order_item_id

Foreign Keys

order_id

menu_item_id

Columns

| Column | Type |
|----------|----------|
| order_item_id | BIGINT |
| order_id | BIGINT |
| menu_item_id | INTEGER |
| quantity | INTEGER |
| unit_price | DECIMAL |
| total_price | DECIMAL |

---

## 14. Sales

Purpose

Completed payments.

Primary Key

sale_id

Foreign Key

order_id

Columns

| Column | Type |
|----------|----------|
| sale_id | BIGINT |
| order_id | BIGINT |
| sale_datetime | TIMESTAMP |
| gross_sales | DECIMAL |
| tax_amount | DECIMAL |
| discount_amount | DECIMAL |
| net_sales | DECIMAL |

---

## 15. Payments

Purpose

Payment details.

Primary Key

payment_id

Foreign Keys

sale_id

machine_id

Columns

payment_id

sale_id

machine_id

payment_method

transaction_reference

payment_status

payment_datetime

amount

---

## 16. Deliveries

Purpose

Delivery information.

Primary Key

delivery_id

Foreign Key

order_id

Columns

delivery_id

order_id

delivery_partner

delivery_status

delivery_distance

estimated_minutes

actual_minutes

delivery_charge

created_at

updated_at

---

## 17. Expenses

Purpose

Restaurant operating expenses.

Primary Key

expense_id

Foreign Keys

restaurant_id

user_id

Columns

expense_id

restaurant_id

user_id

expense_category

expense_date

amount

payment_method

description

status

created_at

updated_at

---

## 18. CashUp

Purpose

Daily cash reconciliation.

Primary Key

cashup_id

Foreign Keys

restaurant_id

user_id

Columns

cashup_id

restaurant_id

user_id

business_date

opening_cash

cash_sales

card_sales

upi_sales

refund_amount

expense_amount

closing_cash

variance

status

created_at

updated_at

---

## 19. CashUp Notes

Purpose

Manager notes.

Primary Key

note_id

Foreign Key

cashup_id

Columns

note_id

cashup_id

note

created_by

created_at

---

## 20. Cash & PDQ

Purpose

Daily payment reconciliation.

Primary Key

record_id

Foreign Keys

cashup_id

machine_id

Columns

record_id

cashup_id

machine_id

cash_amount

card_amount

upi_amount

total_amount

created_at

---

## 21. Banking

Purpose

Daily bank deposits.

Primary Key

banking_id

Foreign Key

restaurant_id

Columns

banking_id

restaurant_id

deposit_date

bank_name

account_number

deposit_amount

reference_number

status

created_at

updated_at

---

## 22. TaxInfo

Purpose

Restaurant tax configuration.

Primary Key

tax_id

Foreign Key

restaurant_id

Columns

tax_id

restaurant_id

tax_name

tax_percentage

effective_from

status

created_at

updated_at

---

## 23. WageAdvance

Purpose

Employee salary advances.

Primary Key

advance_id

Foreign Key

user_id

Columns

advance_id

user_id

request_date

approved_date

amount

reason

approved_by

status

created_at

updated_at