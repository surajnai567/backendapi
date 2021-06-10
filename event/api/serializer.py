from rest_framework.serializers import ModelSerializer
from event.models import Event


class EventSerializer(ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'


class Events(ModelSerializer):
	class Meta:
		model = Event
		fields = '__all__'
		#fields = ['start_dttime', 'end_dttime', 'user_id', 'attending_user']