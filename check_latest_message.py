import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from view.models import ContactMessage

try:
    m = ContactMessage.objects.latest('created_at')
    print("=" * 50)
    print("LATEST MESSAGE")
    print("=" * 50)
    print(f"Name: {m.name}")
    print(f"Email: {m.email}")
    print(f"Subject: {m.subject}")
    print(f"Message: {m.message}")
    print(f"Created: {m.created_at}")
    print()
    print("MESSAGE DELIVERY:")
    print(f"  Email Sent: {m.email_sent}")
    print(f"  Email Error: {m.email_error if m.email_error else 'None'}")
    print("=" * 50)
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
