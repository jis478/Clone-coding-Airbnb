from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [path("1", views.room_detail, name="detail")]
