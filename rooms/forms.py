from django import forms
from django.db.models.constraints import CheckConstraint
from django.db.models.fields import CharField
from django.forms.widgets import CheckboxSelectMultiple
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere")
    price = forms.IntegerField(initial=False)
    country = CountryField(default="KR").formfield()
    room_type = forms.ModelChoiceField(
        queryset=models.RoomType.objects.all(), required=False, empty_label="Any Kind"
    )
    guests = forms.IntegerField(required=False)
    bedrooms = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelChoiceField(required=False, queryset=models.Amenity.objects.all(), widget=forms.CheckboxSelectMultiple)
    facilities = forms.ModelChoiceField(required=False, queryset=models.Facility.objects.all(), widget=forms.CheckboxSelectMultiple)
