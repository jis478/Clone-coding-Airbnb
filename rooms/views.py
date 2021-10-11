from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from . import models


class Homeview(ListView):

    """Homeview model definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "name"
    page_kwarg = "page"
    template_name = "rooms/room_list.html"


# # Function based view
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#     except models.Room.DoesNotExist:
#         # return redirect(reverse("core:home"))
#         raise Http404()
#     return render(request, "rooms/detail.html", context={"room": room})


class RoomDetail(DetailView):
    model = models.Room
    template_name = "rooms/room_detail.html"
