from math import ceil
from django.shortcuts import render
from . import models


def all_rooms(request):
    page = int(request.GET.get("page", 1))  # Query dictionary
    # print(page)
    # page = int(page or 1)
    pagesize = 10
    limit = pagesize * page
    offset = limit - 10
    rooms = models.Room.objects.all()[offset:limit]
    # page_count = len(rooms) // pagesize
    page_count = ceil(models.Room.objects.count() // pagesize)
    return render(
        request,
        "rooms/home.html",
        context={"rooms": rooms, "page": page, "page_count": page_count, "page_range": range(1,page_count)},
    )
