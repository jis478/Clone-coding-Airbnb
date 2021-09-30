from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

class PhotoInline(admin.TabularInline):
    
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline, )

    fieldsets = (
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "beds",
        "bedrooms",
        "baths",
        "guests",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_avg",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "roomtype",
        "amenities",
        "facilities",
        "house_rules",
        "country",
        "city",
    )

    search_fields = ("=city", "^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    raw_id_fields = ("host", )

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    # count_amenities.short_description = "Hello"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Model Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f"<img width ='50px' src='{obj.file.url}'>")

    get_thumbnail.short_description = "THUMBNAIL"
