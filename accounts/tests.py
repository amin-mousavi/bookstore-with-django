from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignUpView

class CustomUserTests(TestCase):

    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username = 'test',
            email = 'test@email.com',
            password = 'test1234',
        )

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            username = 'superusertest',
            email = 'superuser@email.com',
            password = 'superuser1234',
        )

        self.assertEqual(user.username, 'superusertest')
        self.assertEqual(user.email, 'superuser@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

class SignUpTest(TestCase):
    
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! this is a sample text.')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form , CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)

    
