from django.urls import reverse
from rest_framework import status
from .test_setup import UserProfileSetUp
from crud.models.user import UserProfile


class UserProfileTests(UserProfileSetUp):
    def test_create_user(self):
        url = reverse("user-profile")
        data = {
            "first_name": "Emma",
            "last_name": "Frost",
            "contact_number": "9876543222",
            "email_id": "emma123@email.com",
            "gender": "F",
            "dob": "2001-01-22",
            "country": "AU",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_bad_request(self):
        url = reverse("user-profile")
        data = {
            "first_name": "Emma",
            "last_name": "Frost",
            "contact_number": "9876543222000",
            "email_id": "emma123@email.com",
            "gender": "F",
            "dob": "2001-01-22",
            "country": "AU",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user(self):
        url = reverse("user-profile")
        response = self.client.get(url, format="json")
        data = {
            "id": response.data[0]["id"],
            "first_name": "Emma",
            "last_name": "Frost",
            "contact_number": "9876543224",
            "email_id": "emma123@email.com",
            "gender": "F",
            "dob": "2001-01-22",
            "country": "AU",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_bad_request(self):
        url = reverse("user-profile")
        response = self.client.get(url, format="json")
        data = {
            "id": response.data[0]["id"],
            "first_name": "Emma",
            "last_name": "Frost",
            "contact_number": "987654",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user_fail(self):
        url = reverse("user-profile")
        response = self.client.get(url, format="json")
        data = {
            "id": 900,
            "first_name": "Emma",
            "last_name": "Frost",
            "contact_number": "9876543224",
            "email_id": "emma123@email.com",
            "gender": "F",
            "dob": "2001-01-22",
            "country": "AU",
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_all_user(self):
        url = reverse("user-profile")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
