from django.urls import path, include
from django.conf.urls import url
from hallInfo import views

urlpatterns=[
    path('info',views.signin,name="info"),
]