from django.contrib import admin
from .models import Company, Banner, Service, About, Worker


# Register your models here.
@admin.register(Company)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['tag']
    list_filter = ['tag']
    search_fields = ['tag']


@admin.register(Service)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


@admin.register(About)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Worker)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_filter = ['full_name']
    search_fields = ['full_name']
