from rest_framework.serializers import ModelSerializer
from user.models import User


class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ['id','fname', 'lname','username','email','description','followers','following', 'image', 'description','token','dob','events']


class UserSerializerCustom(ModelSerializer):
	class Meta:
		model = User
		fields = ['id']



class FollowSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = ['fname', 'lname', 'description', 'username', 'email','image']
