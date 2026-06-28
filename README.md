# SmartStock API

## Project Overview

SmartStock API is a professional Django REST Framework-based inventory management system designed to help businesses track stock items, manage suppliers, detect low stock situations, and send restock requests automatically. The project is built to support efficient inventory operations with a clean API structure and secure authentication.

This solution demonstrates practical backend development skills, including database modeling, API development, authentication, validation, email integration, and deployment-ready project structure.

---

## Highlights of the Work Completed

This project includes the following completed features:

- Built a fully functional inventory management API
- Implemented supplier and inventory data models
- Added CRUD operations for inventory items
- Created reorder alert functionality for low stock items
- Added email-based restock notification support
- Implemented JWT authentication for secure access
- Enabled search functionality for inventory items
- Added custom validation logic to enforce business rules
- Structured the project in a clean Django application format

---

## Project Goals

The main objective of this project is to provide a reliable backend system that allows a business to:

- Monitor stock levels in real time
- Maintain supplier information
- Identify items that need replenishment
- Send restock requests quickly
- Manage inventory through API endpoints

---

## Technologies Used

- Python
- Django
- Django REST Framework
- Django REST Framework Simple JWT
- SQLite Database
- Django Filters
- SMTP/Email integration

---

## Project Structure

The project is organized as follows:

- inventory/ - Main Django project folder
- inventory/myapp/ - Application containing models, views, serializers, URLs, and logic
- inventory/db.sqlite3 - SQLite database file
- inventory/manage.py - Django management script

### Main Application Files

- models.py - Defines the Supplier and Inventory database models
- views.py - Contains API logic for inventory operations and email alerts
- serializer.py - Handles data validation and API serialization
- urls.py - Defines all API routes

---

## Core Features

### 1. Inventory Management

Users can create, view, update, and delete inventory items through API endpoints.

### 2. Supplier Management

Each inventory item is linked to a supplier, allowing better stock and purchase tracking.

### 3. Reorder Alerts

The system identifies items whose current stock is at or below the reorder threshold.

### 4. Restock Email Notifications

When stock is low, the system can send an email notification to the supplier requesting restocking.

### 5. Authentication and Security

The API supports secure authentication using JWT tokens and session-based access for the browsable interface.

### 6. Search and Filtering

Inventory items can be searched by item name to make data retrieval faster and more efficient.

---

## Database Models

### Supplier

Stores supplier details such as:

- Name
- Email address

### Inventory

Stores inventory item details such as:

- Associated supplier
- Item name
- Current stock
- Reorder stock level

---

## API Endpoints

The project exposes the following API routes:

- GET /inventory/ - Retrieve inventory items
- POST /inventory/ - Add a new inventory item
- GET /inventory/<id>/ - Retrieve a specific inventory item
- PUT /inventory/<id>/ - Update an inventory item
- DELETE /inventory/<id>/ - Delete an inventory item
- GET /inventory/reorder-list/ - Retrieve items that need restocking
- POST /inventory/<id>/send-email/ - Send a restock email for a specific item
- POST /api/token/ - Obtain JWT access token
- POST /api/token/refresh/ - Refresh JWT token

---

## Authentication

The API uses JWT authentication for secure access. Users can obtain tokens using the token endpoint and include them in API requests for protected actions.

---

## Installation and Setup

Follow these steps to run the project locally:

1. Open the project folder
2. Create and activate a virtual environment
3. Install the required dependencies
4. Apply database migrations
5. Run the development server

### Example Setup

```bash
cd inventory
python -m venv .venv
.venv\Scripts\activate
pip install django djangorestframework djangorestframework-simplejwt django-filter
python manage.py migrate
python manage.py runserver
```

---

## Database Migration

To initialize the database schema, run:

```bash
python manage.py migrate
```

---

## Running the Project

Start the application with:

```bash
python manage.py runserver
```

Then open the browser or API client and use the available endpoints.

---

## Business Logic Included

The application includes basic business rules such as:

- Low-stock items are flagged for reorder
- Inventory updates are validated before saving
- Restock requests are generated through email notifications

---

## Professional Summary

SmartStock API is a practical and well-structured inventory management backend solution that combines inventory tracking, supplier management, low-stock alerts, and secure API access. It is a strong example of modern Django-based backend development and is suitable for presentation to stakeholders, hiring teams, or project reviewers.

---

## Future Enhancements

Possible future improvements include:

- User role-based access control
- Dashboard analytics for stock trends
- CSV or Excel import/export
- Advanced reporting and notifications
- Deployment to cloud platforms such as Render or Railway
