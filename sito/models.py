from django.db import models
from cloudinary.models import CloudinaryField


class Apartment(models.Model):
    index = models.IntegerField("Numero Appartamento (1/2/3)", default=1, unique=True)
    name_it = models.CharField(
        "Nome Appartamento (in italiano)", max_length=1000, default=""
    )
    name_en = models.CharField(
        "Nome Appartamento (in inglese)", max_length=1000, default=""
    )
    short_descr_it = models.TextField("Descrizione Breve (in italiano)")
    short_descr_en = models.TextField("Descrizione Breve (in inglese)")
    key_features_it = models.TextField(
        "Caratteristiche Chiave (una linea per ciascuna) in italiano"
    )
    key_features_en = models.TextField(
        "Caratteristiche Chiave (una linea per ciascuna) in inglese"
    )
    full_descr_it = models.TextField("Descrizione Completa (in italiano)")
    full_descr_en = models.TextField("Descrizione Completa (in inglese)")
    max_people = models.CharField(
        "Numero Massimo Persone", max_length=1000, default="5"
    )

    def __str__(self):
        return f"<Appartamento {self.index}, {self.name_it}>"


class ApartmentImage(models.Model):
    apartment = models.ForeignKey(
        Apartment, on_delete=models.CASCADE, related_name="images"
    )
    image = CloudinaryField("Apartment Image")
    caption = models.CharField(
        "Titolo immagine (opzionale)", max_length=255, blank=True, null=True
    )

    def __str__(self):
        return f"<Image for {self.apartment.name_it}>"


class WelcomeInfo(models.Model):
    italian = models.TextField("Descrizione in italiano")
    english = models.TextField("Descrizione in inglese")
    background_img = CloudinaryField("Background Image")

    def __str__(self):
        return "<Informazioni di benvenuto>"


class Labels(models.Model):
    page_title = models.CharField("Titolo Pagina Base", max_length=1000, default="")
    business_name = models.CharField("Nome Residenza", max_length=1000, default="")

    page_title_home_it = models.CharField(
        "Titolo Pagina home (IT)", max_length=1000, default=""
    )
    page_title_home_en = models.CharField(
        "Titolo Pagina home (EN)", max_length=1000, default=""
    )
    page_title_calagonone_it = models.CharField(
        "Titolo Pagina calagonone (IT)", max_length=1000, default=""
    )
    page_title_calagonone_en = models.CharField(
        "Titolo Pagina calagonone (EN)", max_length=1000, default=""
    )
    page_title_contacts_it = models.CharField(
        "Titolo Pagina contacts (IT)", max_length=1000, default=""
    )
    page_title_contacts_en = models.CharField(
        "Titolo Pagina contacts (EN)", max_length=1000, default=""
    )
    page_title_apartment_it = models.CharField(
        "Titolo Pagina apartment (IT)", max_length=1000, default=""
    )
    page_title_apartment_en = models.CharField(
        "Titolo Pagina home (EN)", max_length=1000, default=""
    )

    section_home_it = models.CharField(
        "Etichetta Sezione home (IT)", max_length=1000, default=""
    )
    section_home_en = models.CharField(
        "Etichetta Sezione home (EN)", max_length=1000, default=""
    )
    section_calagonone_it = models.CharField(
        "Etichetta Sezione calagonone (IT)", max_length=1000, default=""
    )
    section_calagonone_en = models.CharField(
        "Etichetta Sezione calagonone (EN)", max_length=1000, default=""
    )
    section_contacts_it = models.CharField(
        "Etichetta Sezione contacts (IT)", max_length=1000, default=""
    )
    section_contacts_en = models.CharField(
        "Etichetta Sezione contacts (EN)", max_length=1000, default=""
    )

    location_directions_it = models.CharField(
        "Etichetta Come Arrivare (IT)", max_length=1000, default=""
    )
    location_directions_en = models.CharField(
        "Etichetta Come Arrivare (EN)", max_length=1000, default=""
    )
    view_apartments_it = models.CharField(
        "Etichetta per 'guarda gli appartamenti' (IT)", max_length=1000, default=""
    )
    view_apartments_en = models.CharField(
        "Etichetta per 'guarda gli appartamenti' (EN)", max_length=1000, default=""
    )
    book_it = models.CharField(
        "Etichetta per 'prenota' (IT)", max_length=1000, default=""
    )
    book_en = models.CharField(
        "Etichetta per 'prenota' (EN)", max_length=1000, default=""
    )
    details_it = models.CharField(
        "Etichetta per 'dettagli appartamento' (IT)", max_length=1000, default=""
    )
    details_en = models.CharField(
        "Etichetta per 'dettagli appartamento' (EN)", max_length=1000, default=""
    )

    quick_book_it = models.CharField(
        "Titolo sezione 'prenota' (info e contatti) (IT)", max_length=1000, default=""
    )
    quick_book_en = models.CharField(
        "Titolo sezione 'prenota' (info e contatti) (EN)", max_length=1000, default=""
    )
    contacts_it = models.CharField(
        "Titolo sezione 'contatti' (info e contatti) (IT)", max_length=1000, default=""
    )
    contacts_en = models.CharField(
        "Titolo sezione 'contatti' (info e contatti) (EN)", max_length=1000, default=""
    )
    phone_it = models.CharField("'telefono' (IT)", max_length=1000, default="")
    phone_en = models.CharField("'telefono' (EN)", max_length=1000, default="")
    location_it = models.CharField("'residenza' (IT)", max_length=1000, default="")
    location_en = models.CharField("'residenza' (EN)", max_length=1000, default="")
    call_it = models.CharField("'chiama' (IT)", max_length=1000, default="")
    call_en = models.CharField("'chiama' (EN)", max_length=1000, default="")

    form_apartment_it = models.CharField(
        "'scegli appartamento' Form (IT)", max_length=1000, default=""
    )
    form_apartment_en = models.CharField(
        "'scegli appartamento' Form (EN)", max_length=1000, default=""
    )
    form_check_in = models.CharField("Check in Form", max_length=1000, default="")
    form_check_out = models.CharField("Check out Form", max_length=1000, default="")
    form_adults_it = models.CharField("Adulti Form (IT)", max_length=1000, default="")
    form_adults_en = models.CharField("Adulti Form (EN)", max_length=1000, default="")
    form_children_it = models.CharField(
        "Bambini Form (IT)", max_length=1000, default=""
    )
    form_children_en = models.CharField(
        "Bambini Form (EN)", max_length=1000, default=""
    )
    form_people_it = models.CharField(
        "'Persone' Form (IT)", max_length=1000, default=""
    )
    form_people_en = models.CharField(
        "'Persone' Form (EN)", max_length=1000, default=""
    )
    form_submit_it = models.CharField("Invia Form (IT)", max_length=1000, default="")
    form_submit_en = models.CharField("Invia Form (EN)", max_length=1000, default="")
    form_email_it = models.CharField("Email Form (IT)", max_length=1000, default="")
    form_email_en = models.CharField("Email Form (EN)", max_length=1000, default="")
    form_phone_it = models.CharField("Phone Form (IT)", max_length=1000, default="")
    form_phone_en = models.CharField("Phone Form (EN)", max_length=1000, default="")
    form_message_it = models.CharField("Message Form (IT)", max_length=1000, default="")
    form_message_en = models.CharField("Message Form (EN)", max_length=1000, default="")

    form_email_ph_it = models.CharField(
        "Placeholder Email Form (IT)", max_length=1000, default=""
    )
    form_email_ph_en = models.CharField(
        "Placeholder Email Form (EN)", max_length=1000, default=""
    )
    form_phone_ph_it = models.CharField(
        "Placeholder Phone Form (IT)", max_length=1000, default=""
    )
    form_phone_ph_en = models.CharField(
        "Placeholder Phone Form (EN)", max_length=1000, default=""
    )
    form_message_ph_it = models.CharField(
        "Placeholder Message Form (IT)", max_length=1000, default=""
    )
    form_message_ph_en = models.CharField(
        "PlaceholderMessage Form (EN)", max_length=1000, default=""
    )

    prices_it = models.CharField(
        "Etichetta 'prezzi e condizioni' (IT)", max_length=1000, default=""
    )
    prices_en = models.CharField(
        "Etichetta 'prezzi e condizioni' (EN)", max_length=1000, default=""
    )
    taxes_it = models.CharField("Etichetta 'tasse' (IT)", max_length=1000, default="")
    taxes_en = models.CharField("Etichetta 'tasse' (EN)", max_length=1000, default="")
    cancelation_it = models.CharField(
        "Etichetta 'cancellazione' (IT)", max_length=1000, default=""
    )
    cancelation_en = models.CharField(
        "Etichetta 'cancellazione' (EN)", max_length=1000, default=""
    )
    rubbish_it = models.CharField(
        "Etichetta 'rifiuti' (IT)", max_length=1000, default=""
    )
    rubbish_en = models.CharField(
        "Etichetta 'rifiuti' (EN)", max_length=1000, default=""
    )

    in_evidenza_it = models.CharField(
        "Etichetta 'in evidenza' (IT)", max_length=1000, default=""
    )
    in_evidenza_en = models.CharField(
        "Etichetta 'in evidenza' (EN)", max_length=1000, default=""
    )
    full_descr_it = models.CharField(
        "Etichetta 'descrizione' appartamento (IT)", max_length=1000, default=""
    )
    full_descr_en = models.CharField(
        "Etichetta 'descrizione' appartamento (EN)", max_length=1000, default=""
    )
    other_apartments_it = models.CharField(
        "Etichetta 'altri appartamenti' (IT)", max_length=1000, default=""
    )
    other_apartments_en = models.CharField(
        "Etichetta 'altri appartamenti' (IT)", max_length=1000, default=""
    )


class CalaGononeInfo(models.Model):
    title_it = models.CharField(max_length=1000)
    title_en = models.CharField(max_length=1000)
    description_it = models.TextField()
    description_en = models.TextField()

    def __str__(self):
        return f"<Informazioni per Cala Gonone dal titolo {self.title_it}>"


class ContactsInfo(models.Model):
    mail = models.CharField("e-mail", max_length=1000)
    phone = models.CharField("Telefono", max_length=1000, default="")
    address = models.CharField("Via", max_length=1000)
    cap_and_town = models.CharField("CAP e nome paese", max_length=1000)
    region_and_country_it = models.CharField(
        "Regione e stato (in italiano)", max_length=1000
    )
    region_and_country_en = models.CharField(
        "Regione e stato (in inglese)", max_length=1000
    )
    tassa_di_soggiorno_it = models.TextField(
        "Tassa di soggiorno (in italiano)",
    )
    tassa_di_soggiorno_en = models.TextField(
        "Tassa di soggiorno (in inglese)",
    )
    prices_it = models.TextField("Prezzi e condizioni (IT)", default="")
    prices_en = models.TextField("Prezzi e condizioni (EN)", default="")
    cancelation_it = models.TextField("Cancellazione (IT)", default="")
    cancelation_en = models.TextField("Cancellazione (EN)", default="")
    rubbish_it = models.TextField("Rifiuti (IT)", default="")
    rubbish_en = models.TextField("Rifiuti (EN)", default="")
    privacy_it = models.TextField("Privacy Policy (IT)", default="")
    privacy_en = models.TextField("Privacy Policy (EN)", default="")

    def __str__(self):
        return "<Informazioni Generali>"
