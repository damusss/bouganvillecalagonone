from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("submit-booking/", views.submit_request, name="submit_request"),
    path("", views.view_home),
    path("it", views.view_home_it),
    path("en", views.view_home_en),
    path("calagonone/", views.view_calagonone),
    path("calagonone/it", views.view_calagonone_it),
    path("calagonone/en", views.view_calagonone_en),
    path("contacts", views.view_contacts),
    path("contacts/it", views.view_contacts_it),
    path("contacts/en", views.view_contacts_en),
    path("apartment-<int:aid>", views.view_apartment),
    path("apartment-<int:aid>/en", views.view_apartment_en),
    path("apartment-<int:aid>/it", views.view_apartment_it),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
