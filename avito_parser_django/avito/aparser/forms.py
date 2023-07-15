from django import forms

from .models import Task
from .models import Product
from .models import Region
from .models import City
from .models import Category


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
            'kod_region',
        )
        widgets = {
            'name': forms.TextInput,
        }


# 'kod_region', 'name', 'slug'

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = (
            'name',
            'region',
        )
        widgets = {
            'name': forms.TextInput,
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'cat_kod',
            'name',
            'parent_kod',
        )
        widgets = {
            'name': forms.TextInput,
        }
