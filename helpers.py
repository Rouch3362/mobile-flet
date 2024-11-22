import flet
from typing import List
from api_calls import send_request
# these blocks of codes are shit don't look at it just scrol til you see these ------ ( but it works :) )

def oneLengthToOther(cm,inc,ft,mi,kl):
    
    if cm: 
        inc = str(round(float(cm) / 2.54, 2))
        ft  = str(float(cm) / 30.48)
        mi  = str(float(cm) / 160900)
        kl  = str(float(cm) / 100000)
    
    elif inc:
        cm  = str(round(float(inc) * 2.54, 2))
        ft  = str(round(float(inc) / 12, 2))
        mi  = str(float(inc) / 63360)
        kl  = str(float(inc) / 39370)

    elif ft:
        cm  = str(round(float(ft) * 30.48, 2))
        inc = str(round(float(ft) * 12, 2))
        mi  = str(float(ft) / 5280)
        kl  = str(float(ft) / 3281)

    elif mi:
        cm  = str(round(float(mi) * 160900, 2))
        inc = str(round(float(mi) * 63360, 2))
        ft  = str(round(float(mi) * 5280, 2))
        kl  = str(round(float(mi) * 1.609, 2))

    elif kl:
        cm  = str(round(float(kl) * 100000, 2))
        inc = str(round(float(kl) * 39370, 2))
        ft  = str(round(float(kl) * 3281, 2))
        mi  = str(round(float(kl) / 1.609, 2))


    return cm, inc, ft, mi, kl
    
    

def oneWeightToOther(gram,kilo,pound,ounce):
    if gram:
        kilo  = str(round(float(gram) / 1000 ,4))
        pound = str(round(float(gram) / 4536 ,4))
        ounce = str(round(float(gram) / 2835 ,4))

    elif kilo:
        gram  = str(round(float(kilo) * 1000 ,4))
        pound = str(round(float(kilo) * 2205 ,4))
        ounce = str(round(float(kilo) * 35274 ,4))

    elif pound:
        gram  = str(round(float(pound) * 4536 ,4))
        kilo  = str(round(float(pound) / 2.205 ,4))
        ounce = str(round(float(pound) * 16 ,4))

    elif ounce:
        print('uf')
        gram  = str(round(float(ounce) * 28.34952 ,4))
        kilo  = str(round(float(ounce) * 0.02835 ,4))
        pound = str(round(float(ounce) / 16 ,4))

    return gram, kilo, pound, ounce



def oneDataToOthers(byte, megabyte, gigabyte, terabyte):
    if byte:
        megabyte = str(float(byte) / 1e+6)
        gigabyte = str(float(byte) / 1e+9)
        terabyte = str(float(byte) / 1e+12)
    elif megabyte:
        byte = str(round(float(megabyte) * 1e+6, 2))
        gigabyte = str(round(float(megabyte) / 1024, 2))
        terabyte = str(round(float(megabyte) / 1e+6, 2))
    elif gigabyte:
        byte = str(round(float(gigabyte) * 1e+9, 2))
        megabyte = str(round(float(gigabyte) * 1024, 2))
        terabyte = str(round(float(gigabyte) / 1024, 2))

    elif terabyte:
        byte = str(round(float(terabyte) * 1e+12, 2))
        megabyte = str(round(float(terabyte) * 1e+6, 2))
        gigabyte = str(round(float(terabyte) * 1024, 2))

    return byte, megabyte, gigabyte, terabyte



def oneCurrencyToOther(page, usd, irr, eur, cny):
    result = None
    if usd:
        result = send_request(page, "usd", ["irr", "eur", "cny"], usd)
        result.insert(0, usd)
    elif irr:
        result = send_request(page, "irr", ["usd", "eur", "cny"], irr)
        result.insert(1, irr)
    elif eur:
        result = send_request(page, "eur", ["usd", "irr", "cny"], eur)
        result.insert(2, eur)
    elif cny:
        result = send_request(page, "cny", ["usd", "irr", "eur"], cny)
        result.insert(3, cny)


    if result == None:
        return usd, irr, eur, cny

    usd = round(float(result[0]), 2)
    irr = round(float(result[1]), 2)
    eur = round(float(result[2]), 2)
    cny = round(float(result[3]), 2)

    return usd, irr, eur, cny
#----------------------------------------


def copy_to_clipboard(text, page: flet.Page):
    page.set_clipboard(text)
    snack_bar = flet.SnackBar(flet.Text("Copied To Clipboard"))
    page.overlay.append(snack_bar)
    snack_bar.open = True
    page.update()



def get_current_page(page: flet.Page):
    match page.route:
        case "/length":
            return 0
        case "/weight":
            return 1
        case "/data":
            return 2
        case "/currency":
            return 3
        
# Label to display errors


def show_error(page, text):
    snack_bar = flet.SnackBar(
        flet.Text(value=text, color=flet.colors.WHITE, text_align=flet.TextAlign.CENTER), 
        bgcolor=flet.colors.RED,
        show_close_icon=True,
        close_icon_color=flet.colors.WHITE)
    page.overlay.append(snack_bar)
    snack_bar.open = True
    page.update()




def create_text_field(page, label, inputCleaner):
    text_field = flet.TextField(border_radius=12, label=label, content_padding=flet.padding.Padding(15,2,15,2), input_filter=flet.NumbersOnlyInputFilter())

    copy_button = flet.IconButton(
        icon=flet.icons.COPY_ROUNDED,
        on_click=lambda _: copy_to_clipboard(text_field.value, page)
    )

    text_field.suffix = copy_button


    return text_field



def check_for_invalid_input(inputs: List[str], page):
    for i in inputs:
        if i != "" and float(i) == 0.0:
            show_error(page, "the number must be greater than 0")
            return True