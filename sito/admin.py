from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse
from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from django.http import HttpRequest
from .models import (
    WelcomeInfo,
    CalaGononeInfo,
    CalaGononeImage,
    ContactsInfo,
    Apartment,
    ApartmentImage,
    Labels,
    MoreConfig,
    HomePanoramaImage,
    HouseImage,
)


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


class SingletonModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request: HttpRequest) -> bool:
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def changelist_view(self, request, extra_context=None):
        obj = self.model.objects.first()
        if obj:
            url = reverse(
                f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change",
                args=[obj.id],
            )
            return redirect(url)
        else:
            url = reverse(
                f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_add"
            )
            return redirect(url)


@admin.register(Labels)
class LabelsAdmin(SingletonModelAdmin): ...


@admin.register(MoreConfig)
class MoreConfigAdmin(SingletonModelAdmin): ...


class HomePanoramaImageInline(SortableTabularInline):
    model = HomePanoramaImage
    extra = 1


class HouseImageInLine(SortableTabularInline):
    model = HouseImage
    extra = 1


@admin.register(WelcomeInfo)
class WelcomeInfoAdmin(SortableAdminBase, SingletonModelAdmin):
    inlines = [HouseImageInLine, HomePanoramaImageInline]


@admin.register(ContactsInfo)
class ContactsInfoAdmin(SingletonModelAdmin): ...
