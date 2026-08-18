from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django_ratelimit.decorators import ratelimit

from .forms import ContactForm
from .models import ContactMessage


def get_client_ip(request):
    """Extract client IP address from request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR', '127.0.0.1')


@require_http_methods(["GET", "POST"])
@ratelimit(key='ip', rate=settings.PORTFOLIO_CONTACT_RATE_LIMIT, method='POST')
def home(request):
    """Render the homepage and handle contact form submissions."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            message_body = (
                f"Name: {cleaned['name']}\n"
                f"Email: {cleaned['email']}\n"
                f"Subject: {cleaned['subject']}\n\n"
                f"Message:\n{cleaned['message']}"
            )

            email_sent = False
            email_error = None
            
            try:
                send_mail(
                    subject=f"Portfolio Contact: {cleaned['subject']}",
                    message=message_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.PORTFOLIO_CONTACT_EMAIL],
                    fail_silently=False,
                )
                email_sent = True
                messages.success(request, 'Your message has been sent successfully. I will respond within 24-48 hours.')
            except Exception as e:
                email_error = str(e)
                messages.warning(request, 'Your message was saved, but the email could not be sent right now. I will still see your message.')

            # Create contact message record with actual email status
            client_ip = get_client_ip(request)
            ContactMessage.objects.create(
                name=cleaned['name'],
                email=cleaned['email'],
                subject=cleaned['subject'],
                message=cleaned['message'],
                email_sent=email_sent,
                email_error=email_error,
                ip_address=client_ip,
            )
            return redirect('/#contact')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})


@require_http_methods(["GET"])
def animation_showcase(request):
    """Render the modern portfolio animation showcase page."""
    return render(request, 'animation_showcase.html')
