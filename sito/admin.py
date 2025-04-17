from django.contrib import admin

from .models import WelcomeInfo, CalaGononeInfo, ContactsInfo, Apartment, ApartmentImage, Labels

admin.site.register([WelcomeInfo, CalaGononeInfo, ContactsInfo, Labels])

class ApartmentImageInline(admin.StackedInline):  # StackedInline: vertical, TabularInline: idk
    model = ApartmentImage
    extra = 1

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    inlines = [ApartmentImageInline]
