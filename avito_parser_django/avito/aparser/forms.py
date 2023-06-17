from django import forms

from .models import Task
from .models import Product
from .models import Region
from .models import City


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'url',
            'status',
        )
        widgets = {
            'title': forms.TextInput,
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'currency',
            'url',
            'published_date',
        )
        widgets = {
            'title': forms.TextInput,
            'currency': forms.TextInput,
        }


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = (
            'name',
            'url_path',
            'kod_region',
        )
        widgets = {
            'name': forms.TextInput,
        }


# 'kod_region', 'name', 'url_path'

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = (
            'name',
            'url_path',
            'parent_id',
        )
        widgets = {
            'name': forms.TextInput,
        }
