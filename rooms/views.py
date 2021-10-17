from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from django_countries import countries
from . import models, forms


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


# values to be recevied from the form
# values to be sent to the form
# def search(request):
# city = request.GET.get("city", "Anywhere")
# city = str.capitalize(city)
# country = request.GET.get("country", "KR")
# room_type = int(request.GET.get("room_type", 0))
# room_types = models.RoomType.objects.all()
# amenities = models.Amenity.objects.all()
# facilities = models.Facility.objects.all()

# guests = request.GET.get("guests", "0")  ## error!
# # print("geee", guests)  # why return None?
# # print(type(guests))
# # print(guests)
# bedrooms = int(request.GET.get("bedrooms", 0))
# beds = int(request.GET.get("beds", 0))
# price = int(request.GET.get("price", 0))
# baths = int(request.GET.get("baths", "0"))
# # print("baths", baths)

# instant_book = bool(request.GET.get("instant_book", False))
# superhost = bool(request.GET.get("superhost", False))

# selected_amenities = request.GET.getlist("amenities")
# selected_facilities = request.GET.getlist("facilities")

# print(selected_amenities)

# options = {
#     "countries": countries,
#     "room_types": room_types,
#     "amenities": amenities,
#     "facilities": facilities,
# }
# forms = {
#     "selected_city": city,
#     "selected_country": country,
#     "selected_room_type": room_type,
#     "price": price,
#     "guests": guests,
#     "bedrooms": bedrooms,
#     "beds": beds,
#     "baths": baths,
#     "instant_book": instant_book,
#     "superhost": superhost,
#     "selected_amenities": selected_amenities,
#     "selected_facilities": selected_facilities,
# }

# filter_args = {}

# if city != "Anywhere":  # exclude default
#     filter_args["city__startswith"] = city

# filter_args["country"] = country

# if room_type != 0:
#     filter_args["room_type__pk__exact"] = room_type  # room_type is a foreign key

# if price != 0:
#     filter_args["price__lte"] = price

# if guests != 0:
#     filter_args["price__gte"] = guests

# if bedrooms != 0:
#     filter_args["bedrooms__gte"] = bedrooms

# if beds != 0:
#     filter_args["beds__gte"] = beds

# if baths != 0:
#     filter_args["baths__gte"] = baths

# if instant_book is True:
#     filter_args["instant_book"] = True

# if superhost is True:
#     filter_args["host__superhost"] = True

# if len(selected_amenities) > 0:
#     for a in selected_amenities:
#         filter_args["amenities__pk"] = int(a)

# if len(selected_facilities) > 0:
#     for f in selected_facilities:
#         filter_args["facilities__pk"] = int(f)

# print(filter_args)

# rooms = models.Room.objects.filter(**filter_args)

# return render(
#     request,
#     "rooms/search.html",
#     context={**options, **forms, "rooms": rooms}
#     # context={"city": city, "countries": countries, "room_types": room_types},
# )


def search(request):
    form = forms.SearchForm(request.GET)
    return render(
        request,
        "rooms/search.html",
        context={"form": form}
        # context={"city": city, "countries": countries, "room_types": room_types},
    )
