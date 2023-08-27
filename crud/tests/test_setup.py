from rest_framework.test import APITestCase
from crud.models.user import UserProfile
from django.contrib.auth.models import User
from django.urls import reverse


class UserProfileSetUp(APITestCase):
    def setUp(self):
        self.user = {"username": "admin", "password": "admin"}
        self.register = reverse("register")
        response = self.client.post(self.register, self.user, format="json")
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

        UserProfile.objects.create(
            first_name="Jhon",
            last_name="Doe",
            contact_number="9876543210",
            email_id="fake123@email.com",
            gender="M",
            dob="2001-01-26",
            country="IN",
        )

        UserProfile.objects.create(
            first_name="Black",
            last_name="Mark",
            contact_number="9876543230",
            email_id="fake127@email.com",
            gender="M",
            dob="2001-01-26",
            country="IN",
        )
        super().setUp()

    def tearDown(self):
        return super().tearDown()
