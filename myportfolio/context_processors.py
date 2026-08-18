"""Template context processors for the project.

This module provides a `whatsapp_url` context processor which builds a
WhatsApp "wa.me" link using values from settings and `urllib.parse.quote`.

The processor exposes a single variable in templates:
- `whatsapp_url`: a full URL string (or empty string if no number configured)

Usage: add 'myportfolio.context_processors.whatsapp_url' to
`TEMPLATES[...]['OPTIONS']['context_processors']` in `settings.py`.
"""
from urllib.parse import quote
from django.conf import settings


def whatsapp_url(request):
    """Return context with `whatsapp_url` built from settings.

    - `WHATSAPP_NUMBER` should be the international number without a leading
      `+` and without spaces (e.g. `919876543210`).
    - `WHATSAPP_DEFAULT_MESSAGE` is URL-encoded and appended as the `text`
      query parameter for the wa.me link.
    """
    number = getattr(settings, "WHATSAPP_NUMBER", "") or ""
    message = getattr(settings, "WHATSAPP_DEFAULT_MESSAGE", "") or ""

    if not number:
        return {"whatsapp_url": ""}

    # Normalize: remove spaces and any leading '+' just in case
    normalized = number.strip().lstrip("+").replace(" ", "")
    encoded = quote(message)
    url = f"https://wa.me/{normalized}?text={encoded}"

    return {"whatsapp_url": url}
