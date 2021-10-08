from django.views.generic import ListView
from . import models


class Homeview(ListView):

    """Homeview model definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "name"
    page_kwarg = "page"
    template_name = "rooms/home.html"
