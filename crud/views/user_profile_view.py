from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from crud.models.user import UserProfile
from crud.serializers.user_profile_serializer import UserProfileSerializer
from django_crud.common_functions.utils.data_processing import (
    format_response,
    format_serializer_response,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserProfileAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        id = request.data.get("id", None)
        if id:
            user_details = get_object_or_404(UserProfile, id=id)
            serializer = UserProfileSerializer(user_details, many=False)
        else:
            user_details = UserProfile.objects.all()
            serializer = UserProfileSerializer(user_details, many=True)
        return Response(format_response(serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(format_serializer_response(serializer, True), status=status.HTTP_201_CREATED)
        return Response(format_serializer_response(serializer), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.data.get("id", None)
        instance = get_object_or_404(UserProfile, id=pk)
        serializer = UserProfileSerializer(instance=instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(format_serializer_response(serializer, True))
        return Response(format_serializer_response(serializer), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.data.get("id", None)
        instance = get_object_or_404(UserProfile, id=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
