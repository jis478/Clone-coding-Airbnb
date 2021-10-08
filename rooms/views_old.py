from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, Paginator
from . import models


def all_rooms(request):
    # manual way
    # page = int(request.GET.get("page", 1))  # Query dictionary
    # print(page)
    # page = int(page or 1)
    # pagesize = 10
    # limit = pagesize * page
    # offset = limit - 10
    # rooms = models.Room.objects.all()[offset:limit]
    # # page_count = len(rooms) // pagesize
    # page_count = ceil(models.Room.objects.count() // pagesize)
    # return render(
    #     request,
    #     "rooms/home.html",
    #     context={"rooms": rooms, "page": page, "page_count": page_count, "page_range": range(1,page_count)},
    # )

    #paginator
    pagesize = 10
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, pagesize, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")
