from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """For category admin-panel"""

    list_display = ('id', 'name', 'slug', 'created', 'updated', 'published', 'get_image')
    list_display_links = ('id', 'name')
    list_editable = ('published', )
    list_filter = ('published', 'created', 'updated')

    def get_image(self, category):
        if category.image:
            url = category.image.url
        else:
            url = "https://fisnikde.com/wp-content/uploads/2019/01/broken-image.png"
        return mark_safe(f'<img src="{url}" width="75px">')

    get_image.short_description = 'Image'
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """For product admin-panel"""

    list_display = (
        'id', 'name', 'slug', 'category', 'price', 'quantity', 'created', 'updated', 'published', 'get_image')
    list_display_links = ('id', 'name')
    list_editable = ('published', )
    list_filter = ('published', 'created', 'updated')
    search_fields = ('name', 'description')

    def get_image(self, product):
        if product.image:
            url = product.image.url
        else:
            url = "https://fisnikde.com/wp-content/uploads/2019/01/broken-image.png"

        return mark_safe(f'<img src="{url}" width="75px">')

    get_image.short_description = 'Image'
    prepopulated_fields = {'slug': ('name', 'category')}
