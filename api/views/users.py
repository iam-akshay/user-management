from rest_framework.views import APIView
from api.models.users import User
from api.serializers.users import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import IntegrityError

from rest_framework.permissions import IsAuthenticated


class UsersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args):
        """
        Get all users
        """
        users = User.objects.all()
        users = UserSerializer(users, many=True)

        return Response(data={"users": users.data}, status=status.HTTP_200_OK)

    def post(self, request, *args):
        """
        Create user
        """
        data = request.data
        user_data = {
            "email": data.get("email"),
            "password": data.get("password"),
            "is_admin": data.get("is_admin", False),
            "is_staff": data.get("is_staff", False),
        }
        try:
            user = User.objects.create_staffuser(**user_data)
            user = UserSerializer(user)
            return Response(
                {"message": "User created successfully", "data": user.data},
                status=status.HTTP_201_CREATED,
            )
        except IntegrityError:
            return Response(
                {"error": f"Email already exists"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        except Exception as err:
            return Response(
                {"error": f"Failed to create user: {err}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id, *args):
        """
        Get Particular user
        """
        user = User.objects.filter(id=id).first()
        if not user:
            return Response(
                data={"error": "User not found"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        user = UserSerializer(user)

        return Response(data=user.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        """
        Delete particular user based on id
        """
        user = User.objects.filter(id=id)
        if not user:
            return Response(
                data={"error": "User not found"},
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )
        user = user.delete()
        user = UserSerializer(data=user)
        return Response(
            data={"message": "User delete successfully!", "user": user.data},
            status=status.HTTP_204_NO_CONTENT,
        )
