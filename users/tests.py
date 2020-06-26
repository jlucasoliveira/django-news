from django.test import SimpleTestCase, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.


class HomePageTests(SimpleTestCase):

    def test_home_page_status(self) -> None:
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_by_url_name(self) -> None:
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        response = self.client.get(reverse('pages:home'))
        self.assertTemplateUsed(response, 'pages/home.html')


class SignUpTests(TestCase):
    username = 'newuser'
    email = f'{username}@email.com'

    def test_signup_page_status_code(self) -> None:
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self) -> None:
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)

    def test_views_uses_correct_template(self) -> None:
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_signup_form(self) -> None:
        new_user = get_user_model().objects.create_user(
            self.username,
            self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
