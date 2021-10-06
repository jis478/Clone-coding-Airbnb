from django.shortcuts import render
from . import models


def all_rooms(request):
    page = int(request.GET.get("page", 1)) # Query dictionary
    limit = 10 * page
    offset = limit - 10
    rooms = models.Room.objects.all()[offset:limit]
    return render(request, "rooms/home.html", context={"rooms": rooms})
