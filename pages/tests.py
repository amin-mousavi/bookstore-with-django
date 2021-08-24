from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView


class HomePageViewTest(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.resp = self.client.get(url) 

    def test_home_page_status_code(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.resp, 'pages/home.html')

    def test_home_page_contain_correct(self):
        self.assertContains(self.resp, 'HomePage')
    
    def test_home_page_contain_incorrect(self):
        self.assertNotContains(self.resp, 'Hi there! this is a incorrect content')

    def test_home_page_url_resolve_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
################################################################################################
class AboutPageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, 'pages/about.html')

    def test_about_page_correct_contain(self):
        self.assertContains(self.response, 'About Page')

    def test_about_page_incorrect_contain(self):
        self.assertNotContains(self.response, 'Hi there! this is an incorrect content')

    def test_about_page_view(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
