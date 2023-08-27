from rest_framework import serializers
from crud.models.user import UserProfile
from django.core.exceptions import ValidationError
from datetime import datetime


class UserProfileSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source="get_country_display", read_only=True)
    gender = serializers.CharField(source="get_gender_display", read_only=True)
    age = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "first_name",
            "last_name",
            "contact_number",
            "email_id",
            "gender",
            "dob",
            "age",
            "country",
            "country_name",
        ]
        read_only_fields = ["id"]

    def validate_contact_number(self, value):
        if len(str(value)) != 10:
            raise ValidationError("Contact length should be exactly 10 characters.")
        return value

    def get_age(self, obj):
        current_year = datetime.now().year
        return current_year - obj.dob.year

    def create(self, validated_data):
        user = UserProfile.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.contact_number = validated_data.get("contact_number", instance.contact_number)
        instance.email_id = validated_data.get("email_id", instance.email_id)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.dob = validated_data.get("dob", instance.dob)
        instance.country = validated_data.get("country", instance.country)
        instance.save()
        return instance
