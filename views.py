import flet
import helpers
from api_calls import send_request


buttonStyle = flet.ButtonStyle(
    bgcolor=flet.colors.BLUE_400,
    color=flet.colors.WHITE,
)

copyIcon = flet.icons.COPY_ROUNDED


def convertButton(convertFunction):
    return flet.TextButton(
        text="Convert", 
        on_click=convertFunction,
        width=300,
        height=50,
        style=buttonStyle,
        visible=True
        )


def navigationHandler(e,page: flet.Page):
    page.views.clear()
    clicked_tab = e.control.selected_index
    if clicked_tab == 0:
        page.go("/length")
        page.views.append(length_view(page)) 
    elif clicked_tab == 1:
        page.go("/weight")
        page.views.append(weight_view(page))
    elif clicked_tab == 2:
        page.go("/data")
        page.views.append(data_view(page))
    elif clicked_tab == 3:
        page.go("/currency")
        page.views.append(currency_view(page))
    
    page.update()


def navBar(page):
    return flet.NavigationBar(
        on_change=lambda e: navigationHandler(e, page),
        destinations=[
            flet.NavigationBarDestination(icon=flet.icons.SOCIAL_DISTANCE_OUTLINED, label="Length"),
            flet.NavigationBarDestination(icon=flet.icons.MONITOR_WEIGHT_OUTLINED, label="Weight"),
            flet.NavigationBarDestination(icon=flet.icons.DATA_USAGE_OUTLINED, label="Data"),
            flet.NavigationBarDestination(icon=flet.icons.CURRENCY_EXCHANGE_OUTLINED , label="Currency")
        ],
        selected_index=helpers.get_current_page(page)
) 



def length_view(page: flet.Page):

    def convertLength(e):
        error = helpers.check_for_invalid_input([
            cm.value, inc.value, ft.value, mi.value, kl.value
        ],page)
        if error:
            return
        
        cm.value , inc.value, ft.value, mi.value, kl.value = helpers.oneLengthToOther(cm.value,inc.value, ft.value, mi.value, kl.value)
        page.update()

    def emptyLengthInputs(e):
        cm.value  = ""
        inc.value = ""
        ft.value  = ""
        mi.value  = ""
        kl.value  = ""
        page.update()

    inc = helpers.create_text_field(page, "Inch", emptyLengthInputs)
    cm  = helpers.create_text_field(page, "Centimetre", emptyLengthInputs)
    ft  = helpers.create_text_field(page, "Foot", emptyLengthInputs)
    mi  = helpers.create_text_field(page, "Mile", emptyLengthInputs)
    kl  = helpers.create_text_field(page, "Kilometre", emptyLengthInputs)
                

    return flet.View(
            "/length",
            controls=[
                cm,
                inc,
                ft,
                mi,
                kl,
                convertButton(convertLength)],
                padding=20,
                vertical_alignment=flet.MainAxisAlignment.CENTER,
                horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                spacing=30,
                appbar=navBar(page)
        )




def weight_view(page: flet.Page):
    def convertWeight(e):
        error = helpers.check_for_invalid_input([
            gram.value, kilo.value, pound.value, ounce.value
        ],page)
        if error:
            return
        gram.value, kilo.value, pound.value, ounce.value = helpers.oneWeightToOther(
            gram.value,
            kilo.value,
            pound.value,
            ounce.value
        )
        page.update()


    def emptyWeightInputs(e):
        gram.value  = ""
        kilo.value  = ""
        pound.value = ""
        ounce.value = ""
        page.update()
    
    gram  = helpers.create_text_field(page,"Gram", emptyWeightInputs)
    kilo  = helpers.create_text_field(page, "Kilogram", emptyWeightInputs)
    pound = helpers.create_text_field(page, "Pound", emptyWeightInputs)
    ounce = helpers.create_text_field(page, "Ounce", emptyWeightInputs)

        
    return flet.View(
        "/weight",
        [
            gram,
            kilo,
            pound,
            ounce,            
            convertButton(convertWeight)
        ],
        padding=20,
        vertical_alignment=flet.MainAxisAlignment.CENTER,
        horizontal_alignment=flet.CrossAxisAlignment.CENTER,
        spacing=30,
        appbar=navBar(page)
        )



def data_view(page: flet.Page):
    def convertData(e):
        error = helpers.check_for_invalid_input([
            byte.value, megabyte.value, gigabyte.value, terabyte.value
        ],page)
        if error:
            return
        byte.value, megabyte.value, gigabyte.value, terabyte.value = helpers.oneDataToOthers(
            byte.value,
            megabyte.value,
            gigabyte.value,
            terabyte.value
        )
        page.update()


    def emptyDataInputs(e):
        byte.value  = ""
        megabyte.value  = ""
        gigabyte.value = ""
        terabyte.value = ""
        page.update()

    byte      = helpers.create_text_field(page, "Byte", emptyDataInputs)
    megabyte  = helpers.create_text_field(page, "Megabyte", emptyDataInputs)
    gigabyte  = helpers.create_text_field(page, "Gigabyte", emptyDataInputs)
    terabyte  = helpers.create_text_field(page, "Terabyte", emptyDataInputs)

    
    return flet.View(
        "/data",
            [
            byte,
            megabyte,
            gigabyte,
            terabyte,
            convertButton(convertData)
            ],
            padding=20,
            vertical_alignment=flet.MainAxisAlignment.CENTER,
            horizontal_alignment=flet.CrossAxisAlignment.CENTER,
            spacing=30,
            appbar=navBar(page)
            )



def currency_view(page: flet.Page):


    def convertCurrency(e):
        try:
            usd.value, irr.value, eur.value, cny.value = helpers.oneCurrencyToOther(
                usd.value, 
                irr.value, 
                eur.value, 
                cny.value)
        except Exception as e:
            helpers.show_error(page, f"{e.error_code} : {e.error_message}")
        page.update()

    def emptyCurrencyInputs(e):
        usd.value = ""
        irr.value = ""
        eur.value = ""
        cny.value = ""
        page.update()

    usd = helpers.create_text_field(page, "US Dollar", emptyCurrencyInputs)
    irr = helpers.create_text_field(page, "Iranian Rial", emptyCurrencyInputs)
    eur = helpers.create_text_field(page, "Euro", emptyCurrencyInputs)
    cny = helpers.create_text_field(page, "Chinese Yuan", emptyCurrencyInputs)


    return flet.View(
        "/currency",
            [
            usd,
            irr,
            eur,
            cny,
            convertButton(convertCurrency)
            ],
            padding=20,
            vertical_alignment=flet.MainAxisAlignment.CENTER,
            horizontal_alignment=flet.CrossAxisAlignment.CENTER,
            spacing=30,
            appbar=navBar(page)
    )