from django.urls import path
from . import views

app_name = "rooms"

# Function based view
# urlpatterns = [path("<int:pk>", views.room_detail, name="detail")]

# Class based view
urlpatterns = [path("<int:pk>", views.RoomDetail.as_view(), name="detail")]
