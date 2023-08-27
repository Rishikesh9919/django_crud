from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from crud.serializers.user_serializer import UserSerializer
from django_crud.common_functions.utils.data_processing import format_serializer_response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class RegisterUserAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data["username"])
            refresh = RefreshToken.for_user(user)
            token_obj = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return Response(token_obj, status=status.HTTP_200_OK)
        return Response(format_serializer_response(serializer), status=status.HTTP_400_BAD_REQUEST)
