from dataclasses import dataclass
import typing


@dataclass
class CTXLabels:
    page_title_base: str = ""
    business_name: str = ""
    page_title: str = ""

    section_home: str = ""
    section_calagonone: str = ""
    section_contacts: str = ""

    location_directions: str = ""
    view_apartments: str = ""
    book: str = ""
    details: str = ""

    quick_book: str = ""
    contacts: str = ""
    phone: str = ""
    location: str = ""
    call: str = ""

    prices: str = ""
    taxes: str = ""
    cancelation: str = ""
    rubbish: str = ""

    form_apartment: str = ""
    form_check_in: str = ""
    form_check_out: str = ""
    form_adults: str = ""
    form_children: str = ""
    form_people: str = ""
    form_submit: str = ""
    form_email: str = ""
    form_phone: str = ""
    form_message: str = ""
    form_email_ph: str = ""
    form_phone_ph: str = ""
    form_message_ph: str = ""

    in_evidenza: str = ""
    full_descr: str = ""
    other_apartments: str = ""
    apartment_not_available: str = ""
    read_more: str = ""
    read_less: str = ""
    gallery: str = ""

    where_are_we: str = ""
    view_map: str = ""


@dataclass
class CTXApartment:
    index: int = -1
    name: str = ""
    descr: str = ""
    key_features: typing.Any = None
    full_descr: str = ""
    images: typing.Any = None
    max_people: str = ""
    available: bool = True


@dataclass
class CTXSimpleApartm:
    index: int = -1
    name: str = ""
    available: bool = True
    max_people: str = ""


@dataclass
class CTXContactInfo:
    email: str = ""
    phone: str = ""
    address: str = ""
    cap_and_town: str = ""
    region_and_country: str = ""
    tassa_di_soggiorno: str = ""
    phone_strip: str = ""
    prices: str = ""
    cancelation: str = ""
    rubbish: str = ""
    privacy: str = ""


@dataclass
class CTXWelcomeInfo:
    image: typing.Any = None
    descr1: str = ""
    descr2: str = ""


@dataclass
class CTXCalaGononeInfo:
    title: str = ""
    descr: str = ""
    nameid: str = ""
    images: typing.Any = None
