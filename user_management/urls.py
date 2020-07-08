from django.urls import path
from user_management import views
app_name = 'user_management'
urlpatterns = [
    path('activity', views.UserActivityListApiView.as_view()),
]