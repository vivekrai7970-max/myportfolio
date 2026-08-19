from django.test import TestCase, Client
from django.test.utils import override_settings

class PortfolioRoutesTests(TestCase):
    def setUp(self):
        """Set up test client with secure=True to handle SSL redirects."""
        self.client = Client()

    @override_settings(DEBUG=True)
    def test_home_page_is_animation_showcase(self):
        """Root route loads the animation showcase page."""
        response = self.client.get('/', secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Scroll to view more')
        self.assertContains(response, 'href="/portfolio/#projects"')
        self.assertContains(response, 'href="/portfolio/#contact"')

    @override_settings(DEBUG=True)
    def test_portfolio_page_accessible_at_portfolio_route(self):
        """Portfolio page accessible at /portfolio/."""
        response = self.client.get('/portfolio/', secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Vivek Ray')
        self.assertContains(response, 'Contact Details')
        self.assertNotContains(response, 'Prefer to reach out directly?')
        self.assertNotContains(response, 'contactForm')
        self.assertNotContains(response, 'Send Message')

    @override_settings(DEBUG=True)
    def test_animation_showcase_route_loads(self):
        """Animation showcase also accessible at /animation/."""
        response = self.client.get('/animation/', secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Scroll to view more')


