from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def home(request):
    """Render the portfolio page."""
    return render(request, 'index.html')


def animation_showcase(request):
    """Render the modern portfolio animation showcase page."""
    return render(request, 'animation_showcase.html')
