from django.contrib import admin
from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from .models import (
    WelcomeInfo,
    CalaGononeInfo,
    CalaGononeImage,
    ContactsInfo,
    Apartment,
    ApartmentImage,
    Labels,
)

admin.site.register([WelcomeInfo, ContactsInfo, Labels])


class ApartmentImageInline(SortableTabularInline):
    model = ApartmentImage
    extra = 1


@admin.register(Apartment)
class ApartmentAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ApartmentImageInline]


class CalaGononeImageInLine(SortableTabularInline):
    model = CalaGononeImage
    extra = 1


@admin.register(CalaGononeInfo)
class CalaGononeInfoAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [CalaGononeImageInLine]
