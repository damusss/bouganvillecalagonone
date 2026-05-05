from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

from .models import ContactsInfo, WelcomeInfo, Apartment, Labels, CalaGononeInfo
from .model_collapse import CTXContactInfo, CTXWelcomeInfo, CTXApartment, CTXLabels, CTXCalaGononeInfo


SECONDARY_COLOR = "purple-600"


def parse_bold(string):
    return string.replace("<>", "<b>").replace("</>", "</b>")


def parse_date(string):
    if "-" not in string:
        return string
    year, month, day = string.split("-")
    return f"{day}/{month}/{year}"


def submit_request(request):
    if request.method != "POST":
        return redirect("/")

    option = request.POST.get("options")
    start_date = parse_date(request.POST.get("start-date"))
    end_date = parse_date(request.POST.get("end-date"))
    adults = request.POST.get("adults")
    children = request.POST.get("children")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    url = request.POST.get("url")
    lang = request.POST.get("lang")
    message = request.POST.get("message")
    language = "inglese" if lang == "en" else "italiana"
    try:
        print("mail result: ", send_mail(
            subject=f"Nuova Richiesta Da {email}",
            message=f"""
            Nuova Richiesta Disponibilità:

            Appartamento: {option}
            Check in: {start_date}, Check out: {end_date}
            Adulti: {adults}, Bambini: {children}

            Telefono: {phone}
            Email: {email}
            Messaggio: {message}

            Il sito era in lingua {language} quando la richiesta è stata inviata.
            """,
            from_email=settings.EMAIL_FROM_USER,
            recipient_list=[settings.EMAIL_END_USER],
            fail_silently=False,
        ))
        messages.success(
            request,
            "Your aviability request was successfully submitted!"
            if lang == "en"
            else "La tua richiesta di disponibilità è stata inviata con successo!",
        )
    except Exception as e:
        messages.error(
            request,
            f"An error occurred: {str(e)}"
            if lang == "en"
            else f"C'è stato un errore: {str(e)}",
        )

    return redirect(request.META.get("HTTP_REFERER", url))


def site_main(request, english, page, aid=None, url=""):
    lang = "en" if english else "it"
    ctx = {
        "lang": lang,
        "current_page": page,
        "secondary_col": SECONDARY_COLOR,
        "it_redirect": f"{url}",
        "en_redirect": f"{url}{'/' if url != '/' else ''}en",
        "redirect": f"{url}{'/' if url != '/' else ''}{lang}",
    }
    add_labels(ctx, english, page)
    ctx["conf"] = {
        "p_font": "Poppins",
        "h_font": "Courgette"
    }
    func = ADD_DATA.get(page, None)
    if func:
        func(ctx, english)
    if aid is not None:
        apartment = get_apartment_data(aid, english)
        ctx["apartment"] = apartment
    return render(request, f"sito/{page}.html", ctx)


def add_labels(ctx, english, page):
    lang = "en" if english else "it"
    model = Labels.objects.all()[0]
    labels = CTXLabels(
        model.page_title,
        model.business_name,
        form_check_in=model.form_check_in,
        form_check_out=model.form_check_out,
    )
    labels.page_title = getattr(model, f"page_title_{page}_it")
    for name in [
        "section_calagonone",
        "section_home",
        "section_contacts",
        "view_apartments",
        "book",
        "details",
        "location_directions",
        "quick_book",
        "contacts",
        "phone",
        "location",
        "call",
        "prices",
        "taxes",
        "cancelation",
        "rubbish",
        "form_apartment",
        "form_children",
        "form_adults",
        "form_people",
        "form_submit",
        "form_email",
        "form_phone",
        "form_message",
        "form_email_ph",
        "form_phone_ph",
        "form_message_ph",
        "in_evidenza",
        "full_descr",
        "other_apartments",
        "apartment_not_available",
        "where_are_we",
        "view_map",
    ]:
        setattr(labels, name, getattr(model, f"{name}_{lang}"))
    ctx["labels"] = labels


def add_contact_info(ctx, english):
    if "contact" in ctx:
        return
    lang = "en" if english else "it"
    model = ContactsInfo.objects.all()[0]
    contact_info = CTXContactInfo(
        model.mail, model.phone, model.address, model.cap_and_town
    )
    contact_info.phone_strip = (
        contact_info.phone.replace("+", "").replace(" ", "").strip()
    )
    for name in [
        "region_and_country",
        "tassa_di_soggiorno",
        "prices",
        "cancelation",
        "rubbish",
        "privacy",
    ]:
        setattr(
            contact_info,
            name,
            parse_bold(getattr(model, f"{name}_{lang}")).replace("\n", "<br>"),
        )
    ctx["contact"] = contact_info


def add_data_home(ctx, english):
    welcome = WelcomeInfo.objects.all()[0]
    info = CTXWelcomeInfo(welcome.background_img)
    if english:
        description = welcome.english
    else:
        description = welcome.italian
    split = description.split("\n")
    info.descr1 = parse_bold(split[0])
    if len(split) > 1:
        info.descr2 = parse_bold(split[-1])
    add_apartments(ctx, english)
    ctx["welcome"] = info
    ctx["panorama_iter"] = list(range(0, 7))
    ctx["panorama_count"] = 7


def add_apartments(ctx, english):
    apartments = Apartment.objects.all()
    apartments = [get_apartment_data(apartment, english) for apartment in apartments]
    ctx["apartments"] = apartments


def add_data_calagonone(ctx, english):
    infos = CalaGononeInfo.objects.all()
    street_directions = None
    view_map = None
    info_ctxs = []
    for model_info in infos:
        info = CTXCalaGononeInfo()
        if english:
            info.title = model_info.title_en
            info.descr = model_info.description_en
        else:
            info.title = model_info.title_it
            info.descr = model_info.description_it
        if model_info.name_id == "street_directions":
            street_directions = info
        elif model_info.name_id == "view_map":
            view_map = info
        else:
            info_ctxs.append(info)
    ctx["infos"] = info_ctxs
    ctx["street_directions"] = street_directions
    ctx["view_map"] = view_map


def add_data_contacts(ctx, english):
    add_contact_info(ctx, english)
    add_apartments(ctx, english)


def add_data_apartment(ctx, english):
    add_apartments(ctx, english)


def get_apartment_data(aid, english):
    if isinstance(aid, int):
        apartment = get_object_or_404(Apartment, index=aid)
    else:
        apartment = aid
    ctx = CTXApartment(apartment.index, max_people=apartment.max_people)
    ctx.descr = apartment.short_descr_it
    ctx.full_descr = apartment.full_descr_it
    ctx.name = apartment.name_it
    key_features = apartment.key_features_it
    if english:
        ctx.descr = apartment.short_descr_en
        ctx.full_descr = apartment.full_descr_en
        ctx.name = apartment.name_en
        key_features = apartment.key_features_en
    ctx.descr = parse_bold(ctx.descr)
    ctx.full_descr = parse_bold(ctx.full_descr)
    if "(" in ctx.name:
        ctx.name = ctx.name.split("(")[0]
    ctx.key_features = [
        item.strip()
        for item in parse_bold(key_features).strip().split("\n")
        if item.strip()
    ]
    ctx.images = apartment.images.all()  # type: ignore
    ctx.available = apartment.available
    return ctx


ADD_DATA = {
    "home": add_data_home,
    "calagonone": add_data_calagonone,
    "contacts": add_data_contacts,
    "apartment": add_data_apartment,
}


def view_home(request):
    return site_main(request, False, "home", url="/")


def view_home_en(request):
    return site_main(request, True, "home", url="/")


def view_home_it(request):
    return HttpResponseRedirect("/")


def view_calagonone(request):
    return site_main(request, False, "calagonone", url="/calagonone")


def view_calagonone_en(request):
    return site_main(request, True, "calagonone", url="/calagonone")


def view_calagonone_it(request):
    return HttpResponseRedirect("/calagonone")


def view_contacts(request):
    return site_main(request, False, "contacts", url="/contacts")


def view_contacts_en(request):
    return site_main(request, True, "contacts", url="/contacts")


def view_contacts_it(request):
    return HttpResponseRedirect("/contacts")


def view_apartment(request, aid):
    return site_main(request, False, "apartment", aid, url=f"/apartment-{aid}")


def view_apartment_en(request, aid):
    return site_main(request, True, "apartment", aid, url=f"/apartment-{aid}")


def view_apartment_it(request, aid):
    return HttpResponseRedirect(f"/apartment-{aid}")
