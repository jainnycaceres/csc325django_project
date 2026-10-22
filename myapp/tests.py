from django.test import TestCase
from django.urls import reverse


class ViewTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertContains(response, "<h1>Welcome to the home page!</h1>", html=True)
        self.assertContains(
            response,
            "<p>This is a simple Django application.</p>",
            html=True,
        )
        self.assertContains(response, "<p>Enjoy your stay!</p>", html=True)

    def test_about_page(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertContains(response, "<h1>About Page</h1>", html=True)
        self.assertContains(
            response,
            "<p>This is the about page of the simple Django application.</p>",
            html=True,
        )
