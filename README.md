# Real Estate

This is a Django-based Real Estate project designed to manage property listings, user interactions, and more. Below are the steps to set up and run the project locally.

## Prerequisites

- Python 3.12.9
- pip (Python package installer)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MariamKipshidze/real_estate.git
   cd real_estate
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create and apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (admin account):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user.

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the project**:
   Open your browser and go to `http://127.0.0.1:8000/` to view the project. Use the admin panel at `http://127.0.0.1:8000/admin/` to manage the site.
```
