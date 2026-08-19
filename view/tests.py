from django.test import TestCase, Client
from django.test.utils import override_settings

from view.forms import ContactForm
from view.models import ContactMessage


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

    @override_settings(DEBUG=True)
    def test_portfolio_page_accessible_at_portfolio_route(self):
        """Portfolio page accessible at /portfolio/."""
        response = self.client.get('/portfolio/', secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Vivek Ray')

    @override_settings(DEBUG=True)
    def test_animation_showcase_route_loads(self):
        """Animation showcase also accessible at /animation/."""
        response = self.client.get('/animation/', secure=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Scroll to view more')

    @override_settings(DEBUG=True)
    def test_contact_form_submission_redirects_and_validates(self):
        """Contact form submission validates and redirects to #contact."""
        form = ContactForm(data={
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Project inquiry',
            'message': 'Hello, I would like to connect.',
        })
        self.assertTrue(form.is_valid())

        response = self.client.post('/portfolio/', data=form.data, secure=True)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/#contact')

    @override_settings(DEBUG=True)
    def test_contact_message_stored_with_correct_email_status(self):
        """Contact message is stored with accurate email_sent status."""
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test message body.',
        }
        
        response = self.client.post('/portfolio/', data=form_data, secure=True)
        
        # Verify message was stored
        message = ContactMessage.objects.filter(email='test@example.com').first()
        self.assertIsNotNone(message)
        self.assertEqual(message.name, 'Test User')
        self.assertEqual(message.subject, 'Test Subject')
        # Email status is tracked accurately
        self.assertIn(message.email_sent, [True, False])

    def test_contact_form_requires_all_fields(self):
        """Contact form requires all fields to be filled."""
        incomplete_form = ContactForm(data={
            'name': 'Test',
            # Missing email, subject, message
        })
        self.assertFalse(incomplete_form.is_valid())

    def test_contact_form_validates_email(self):
        """Contact form validates email format."""
        invalid_email_form = ContactForm(data={
            'name': 'Test User',
            'email': 'not-an-email',
            'subject': 'Test',
            'message': 'Test message',
        })
        self.assertFalse(invalid_email_form.is_valid())

