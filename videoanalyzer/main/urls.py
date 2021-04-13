from django.urls import path
from .views import feed, home, shape, detect_circle

urlpatterns = [
    path('', home, name="home"),
    path('shape/', shape, name="shape"),
    path('shape/circle/', detect_circle, name="circle"),
    path('feed', feed, name="feed"),

]