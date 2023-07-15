from django.contrib import admin

from .forms import TaskForm
from .models import Task
from .forms import ProductForm
from .models import Product
from .forms import RegionForm
from .models import Region
from .forms import CityForm
from .models import City
from .forms import CategoryForm
from .models import Category


PRICE_FILTER_STEPS = 10


class PriceFilter(admin.SimpleListFilter):
    title = 'Цена'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        # Вытащить полный список цен
        prices = [c.price for c in model_admin.model.objects.all()]
        prices = list(filter(None, prices))
        if not prices:
            return

        # TODO: найти "кластера цен", то есть такие интервалы, внутри которых точно есть продукты!

        # Побить его на 10 интервалов
        max_price = max(prices)
        chunk = int(max_price / PRICE_FILTER_STEPS)
        print(f'max_price = {max_price}, chunk = {chunk}')

        intervals = [
            (f'{chunk * i},{chunk * (i + 1)}', f'{chunk * i} - {chunk * (i + 1)}')
            for i in range(PRICE_FILTER_STEPS)
        ]
        return intervals

    def queryset(self, request, queryset):
        choice = self.value() or ''
        if not choice:
            return queryset
        choice = choice.split(',')
        if not len(choice) == 2:
            return queryset
        price_from, price_to = choice
        return queryset.distinct().filter(price__gte=price_from, price__lt=price_to)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'task', 'price', 'currency', 'url')  # , 'published_date'
    list_filter = (
        'currency',
        # 'published_date',
        'task',
        PriceFilter,
    )
    # 'published_date',
    form = ProductForm
    list_per_page = 150


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'url', 'status')
    list_filter = ('status',)
    form = TaskForm


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'kod_region', 'name') #, 'slug'
    # list_filter = ('status', )
    form = RegionForm


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'region_id') #'slug',
    # list_filter = ('status', )
    form = CityForm

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'parent_kod') #'slug',
    # list_filter = ('status', )
    form = CategoryForm

# from django.contrib import admin
#
# from .forms import ProductForm
# from .models import Product
#
#
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     #title = models.TextField(verbose_name='Заголовок')
#     list_display = ('pk', 'title', 'task', 'price', 'currency', 'published_date', 'url')
#     list_filter = (
#         'currency',
#         'published_date',
#         'task',
#         #PriceFilter,
#     )
#
#     form = ProductForm
#     list_per_page = 150
#
