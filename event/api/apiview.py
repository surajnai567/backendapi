import logging
import json

from event.models import Event
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializer import EventSerializer, Events
from user.models import User

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from drf_yasg import openapi
from .swaggerresponse import PostCredential, CreateEventParmas, PostParmAllEvent

logger = logging.getLogger(__name__)


class CreateEventApiView(APIView):
    user_response = openapi.Response('response description', Events)
    @swagger_auto_schema(request_body=CreateEventParmas, responses={200:'"status": "Successfull !!", "userData": "successfully created event"}',
                                                                  201:'"status": "UnSuccessfull !!", "userData": "wrong credentials"'})
    def post(self, request):
        post_data = json.loads(request.body.decode('utf-8'))
        username = post_data.get('username')
        token = post_data.get('token')
        user = User.objects.filter(username=username, token=token).all()
        if len(user):
            image = post_data.get('image')
            des = post_data.get('description')
            start_date = post_data.get('start_dttime')
            end_date = post_data.get('end_dttime')
            is_private = post_data.get('is_private')
            location = post_data.get('location')
            capacity = post_data.get('capacity')
            title = post_data.get('title')
            event = Event(host_id = user[0],image=image, description=des, start_dttime=start_date,
                          end_dttime=end_date, is_private=is_private,
                          location=location, capacity=capacity, title=title)
            event.save()
            return JsonResponse({"code": 200, "status": "Successfull !!", "userData": "successfully created event"})

        return JsonResponse({"code": 201, "status": "UnSuccessfull !!", "userData": "wrong credentials"})


class MyEventApiView(APIView):
    def post(self, request):
        post_data = json.loads(request.body.decode('utf-8'))
        email = post_data.get('email')
        token = post_data.get('token')
        user = User.objects.filter(email=email, token=token).all()
        if len(user):
            events = Event.objects.filter(user_id=user[0]).all()
            data = EventSerializer(events, many=True).data
            return JsonResponse({"code": 200, "status": "Successful !!", "userData": data})
        return JsonResponse({"code": 200, "status": "UnSuccessful !!", "userData": "wrong credentials"})


class TodayEventApiView(APIView):
    def post(self, request):
        post_data = json.loads(request.body.decode('utf-8'))
        email = post_data.get('email')
        token = post_data.get('token')
        date = post_data.get('date')
        user = User.objects.filter(email=email, token=token).all()
        if len(user):
            events = Event.objects.filter(user_id=user[0], start_date=date).all()
            data = EventSerializer(events, many=True).data
            return JsonResponse({"code": 200, "status": "Successful !!", "userData": data})
        return JsonResponse({"code": 200, "status": "UnSuccessful !!", "userData": "wrong credentials"})


class AllEvents(APIView):
    user_response = openapi.Response('return list of events', Events)
    @swagger_auto_schema(request_body=PostParmAllEvent, responses={200:user_response,
                                                                 201:'"status": "UnSuccessful !!", "userData": "wrong credentials"'})
    def post(self, request):
        post_data = json.loads(request.body.decode('utf-8'))
        username = post_data.get('username')
        token = post_data.get('token')
        title = post_data.get('title')
        user = User.objects.filter(username=username, token=token).all()
        if len(user):
            if title is not None and title != '':
                events = Event.objects.filter(title__contains=title).all()
            else:
                events = Event.objects.all()
            data = Events(events, many=True).data
            for d in data:
                user = User.objects.filter(id=d['host_id']).all()[0]
                d['hosted_by'] = user.username
            return JsonResponse({"code": 200, "status": "Successful !!", "userData": data})
        return JsonResponse({"code": 201, "status": "UnSuccessful !!", "userData": "wrong credentials"})


class GetEventById(APIView):
    user_response = openapi.Response('response description', EventSerializer)
    @swagger_auto_schema(request_body=PostCredential, responses={200: user_response})
    def post(self, request, id):
        post_data = json.loads(request.body.decode('utf-8'))
        username = post_data.get('username')
        token = post_data.get('token')
        user = User.objects.filter(username=username, token=token)
        if len(user):
            event = Event.objects.filter(id=id).all()
            if len(event):
                data = EventSerializer(event[0]).data
                return JsonResponse({"data": data})
            else:
                return JsonResponse({"data": {}})
        else:
            return JsonResponse({"data": "wrong credentials"})


class GetEventBYUser(APIView):
    user_response = openapi.Response('response description', EventSerializer)
    @swagger_auto_schema(request_body=PostCredential, responses={200: user_response})
    def post(self, request, username):
        post_data = json.loads(request.body.decode('utf-8'))
        usernam = post_data.get('username')
        token = post_data.get('token')
        user = User.objects.filter(username=usernam, token=token)
        if len(user):
            insterested_user = User.objects.filter(username=username)
            data = []
            eve = insterested_user[0].events
            for e in eve:
                data.append(Event.objects.filter(id=e).all()[0])

            data_post = EventSerializer(data, many=True).data
            for d in data_post:
                user = User.objects.filter(id=d['host_id']).all()[0]
                d['hosted_by'] = user.username

            return JsonResponse({"data": data_post})

        else:
            return JsonResponse({"data": "wrong credentials"})



##############
def get(self, request, id):
    if request.method == 'GET':
        event = Event.objects.filter(id=id).all()
        if len(event):
             data = EventSerializer(event[0]).data
             return JsonResponse({"data": data})
        else:
            return JsonResponse({"data": {}})
