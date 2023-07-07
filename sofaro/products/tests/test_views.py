from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from products.models import Hotels, Product, Comment, Score
from users.forms import BookingForm, CommentForm, ScoreForm

class UsersTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='27062018aq@gmail.com')
        self.user.set_password('321675')
        self.user.save()

        Hotels.objects.create(
            country="Турция",
            title="Hotel 19"
        )
        Product.objects.create(
            title="Product 19",
            country="Турция",
            price=4000,
            price_usd=1400
        )
        self.client = Client()
        self.client.login(username="tester", password="1")


    