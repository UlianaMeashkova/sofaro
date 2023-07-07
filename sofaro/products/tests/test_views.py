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
            title="Hotel 1"
        )
        Product.objects.create(
            title="Product 1",
            country="Турция",
            price=4000,
            price_usd=1400
        )
        self.client = Client()
        self.client.login(username="27062018aq@gmail.com", password="321675")


    def test_index(self):

        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_hotels(self):

        response = self.client.get(reverse("hotels", kwargs={"country": "Турция"}))
        self.assertEqual(response.status_code, 200)

    def test_booking_GET(self):

        response = self.client.get(reverse("booking"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], BookingForm)

    def test_booking_POST(self):

        response = self.client.post(reverse("booking"), {
            "first_name": "Tester",
            "last_name": "Tester",
            "email": "27062018aq@gmail.com",
            "password": "321675",
            "age": 18
        })

        self.assertEqual(response.status_code, 200)

    def test_good_book(self):

        response = self.client.get(reverse("goodBook"))
        self.assertEqual(response.status_code, 200)

    def test_contacts(self):

        response = self.client.get(reverse("contacts"))
        self.assertEqual(response.status_code, 200)

    def test_users(self):

        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Profiles view")

    def test_comment_GET(self):

        response = self.client.get(reverse("comment", kwargs={"hotel_id": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], CommentForm)

    def test_comment_POST(self):

        response = self.client.post(reverse("comment", kwargs={"hotel_id": 1}), {
            "name": "Tester",
            "email": "test@test.com",
            "body": "Test message...",
        })
        comment = Comment.objects.first()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(comment.id, 1)
        self.assertEqual(comment.post.id, 1)
        self.assertEqual(comment.body, "Test message...")

    def test_score_GET(self):

        response = self.client.get(reverse("score", kwargs={"hotel_id": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], ScoreForm)
    
    def test_score_POST(self):

        product = Product.objects.get(id=1)
        self.assertEqual(product.get_score(), 0)

        response = self.client.post(reverse("score", kwargs={"hotel_id": 1}), {
            "value": 5,
        })
        score = Score.objects.first()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(product.get_score(), 5.0)
    


    
