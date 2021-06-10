from django.urls import path
from user.api.apiview import UserRegisterView, UserLogin, \
	UpdateUser,ForgetPassword, UpdatePassword, AddFollowers,\
	Followers,Following, AddMyAttending, test, GetUserById, \
	GetUserByUsername, UnFollow
from event.api.apiview import CreateEventApiView, MyEventApiView,\
	TodayEventApiView, AllEvents, GetEventById, GetEventBYUser


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
	path('user/register', UserRegisterView.as_view()),
	path('user/<int:id>', GetUserById.as_view()),
	path('user/login', UserLogin.as_view(),),
	path('user/forget-password', ForgetPassword.as_view(),),
	path('user/update-password', UpdatePassword.as_view(),),
	path('user/update-user', UpdateUser.as_view(),),
	path('event', CreateEventApiView.as_view(),),
	path('event/<int:id>', GetEventById.as_view(), ),
	path('event/retrieve', AllEvents.as_view(),),
	path('event/<event_id>/attend', AddMyAttending.as_view(),),
	path('event/<username>/attending', GetEventBYUser.as_view(),),


	#path('my-event', MyEventApiView.as_view(),),
	#path('today-event', TodayEventApiView.as_view(),),
	#path('all-event', AllEvents.as_view(),),

	path('user/<str:username>/follow', AddFollowers.as_view(),),
	path('user/<str:username>/un-follow', UnFollow.as_view(),),
	path('user/<str:username>/followers', Followers.as_view(),),
	path('user/<str:username>/following', Following.as_view(),),
	path('user/retrieve', GetUserByUsername.as_view(),),


	path('', test,),
	path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

