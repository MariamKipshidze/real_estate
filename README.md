# Real Estate

This is a Django-based Real Estate project designed to manage property listings, user interactions, and more. Below are the steps to set up and run the project locally.

## Prerequisites

- Python 3.12.9
- pip (Python package installer)

### Installing Python and pip

If you don't have Python and pip installed, follow these steps:

#### On Windows:
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer and check "Add Python to PATH"
3. After installation, verify by running in Command Prompt:
   ```bash
   python --version
   pip --version
   ```

#### On macOS/Linux:
Python usually comes pre-installed. To check:
```bash
python3 --version
pip3 --version
```

If not installed, use your package manager:
- macOS (using Homebrew): `brew install python`
- Ubuntu/Debian: `sudo apt-get install python3 python3-pip`

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MariamKipshidze/real_estate.git
   cd real_estate
   ```

2. **Set up a virtual environment** (recommended):

   #### Using Python's venv:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

   #### Using Anaconda:
   ```bash
   conda create --name real_estate_env python=3.12.9
   conda activate real_estate_env
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

   For local development:
   ```bash
   python manage.py runserver
   ```

   For server deployment (accessible to other devices on network):
   ```bash
   python3 manage.py runserver 0.0.0.0:8000
   ```

7. **Access the project**:
   - Local: Open `http://127.0.0.1:8000/` in your browser
   - Network: Use your server's IP address with port 8000
   - Admin panel: Access at `/admin/` path (e.g., `http://127.0.0.1:8000/admin/`)

# Production Deployment

For production deployment, we recommend using Gunicorn as the application server with Nginx as a reverse proxy. Here's how to set it up:

1. **Update/upgrade system**:
   
   ```bash
   sudo apt-get update
   sudo apt-get upgrade
   ```
2. **Create virtual env**:
   
   ```bash
   sudo apt-get install python3-venv
   python3 -m venv env
   
   # activate virtual env
   source env/bin/activate
   ```
3. **Clone project**:

   ```bash
   git clone https://github.com/MariamKipshidze/real_estate.git
   ```
4. **Install Nginx**:

   ```bash
   sudo apt-get install -y nginx
   ```

5. **Install gunicorn**:

   ```bash
   pip install gunicorn
   ```
6. **Install supervisor**:

   ```bash
   sudo apt-get install supervisor
   ```
   
