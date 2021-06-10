
from rest_framework import serializers


class PostCredential(serializers.Serializer):
   """Your data serializer, define your fields here."""
   username = serializers.CharField()
   token = serializers.CharField()


class CreateEventParmas(serializers.Serializer):
   username = serializers.CharField(required=True)
   token = serializers.CharField()
   image = serializers.URLField()
   title = serializers.CharField(max_length=300)
   description = serializers.CharField(max_length=300)
   location = serializers.CharField(max_length=300)
   is_private = serializers.BooleanField()
   start_dttime = serializers.DateTimeField()
   end_dttime = serializers.DateTimeField()
   capacity = serializers.IntegerField()


class EventByIDParams(serializers.Serializer):
   username = serializers.CharField(required=True)
   token = serializers.CharField(required=True)


class PostParmAllEvent(serializers.Serializer):
   username = serializers.CharField(required=True)
   token = serializers.CharField(required=True)
   title = serializers.CharField()
