from django.urls import path
from example.views import user_list


urlpatterns = [
    path('', user_list, name='user_list'),
]