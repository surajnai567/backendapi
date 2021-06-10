from rest_framework import serializers


class PostCredentialUser(serializers.Serializer):
    """Your data serializer, define your fields here."""
    username = serializers.CharField(required=True)
    token = serializers.CharField(required=True)


class AttendEventParams(serializers.Serializer):
    username = serializers.CharField(required=True)
    token = serializers.CharField(required=True)
    event_id = serializers.IntegerField(required=True)


class UpdatePasswordParams(serializers.Serializer):
    email = serializers.CharField(required=True)
    otp = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class ForgetPasswordParams(serializers.Serializer):
    email = serializers.CharField(required=True)


class UserUpdateParams(serializers.Serializer):
    token = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    fname = serializers.CharField(required=True)
    lname = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    image = serializers.URLField()


class UserLoginParams(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserRegisterParmas(serializers.Serializer):
    email = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    fname = serializers.CharField(required=True)
    lname = serializers.CharField(required=True)
    mobile = serializers.CharField()
    password = serializers.CharField(required=True)


class UserRetriveUsername(serializers.Serializer):
    """Your data serializer, define your fields here."""
    username = serializers.CharField(required=True)
    token = serializers.CharField(required=True)
    user_search = serializers.CharField(required=True)






