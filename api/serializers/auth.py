from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.models.users import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom Toekn Obtain Pair Serializer class"""

    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)

        # Set users details in token payload
        token["user_id"] = user.id
        token["email"] = user.email

        return token

    def validate(self, attrs):
        validate_data = super().validate(attrs)
        validate_data.update(
            {"user": {"id": self.user.id, "email": self.user.email}}
        )
        return validate_data
