# MyPortfolio (Django)

This project includes a contact form that saves messages and sends an email notification.

## Setup (Windows)

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Run the server:

```bash
python manage.py runserver
```

5. Open the site at `http://127.0.0.1:8000/`, submit the contact form, and check your email inbox.

## Notes

- Contact form submissions are saved to the database.
- The app sends a notification email when contact messages are submitted, if email settings are configured.
