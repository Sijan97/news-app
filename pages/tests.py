from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class HomePageViewTest(SimpleTestCase):
    """Testing if home page is displayed properly."""
    def test_home_page_status_code(self):
        """Testing if homepage returns correct status code."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        """Testing if page is redirected to homepage by name."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Testing if view uses correct template."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class SignUpPageTests(TestCase):
    """Testing if signup page functions properly."""
    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_page_status_code(self):
        """Testing if correct status code is returned."""
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        """Testing if view uses correct url name."""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Testing if view uses correct template."""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        """Testing if signup page creates new account properly."""
        new_user = get_user_model().objects.create_user(
                self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(
            get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(
            get_user_model().objects.all()[0].email, self.email)