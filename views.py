import flet
import helpers


buttonStyle = flet.ButtonStyle(bgcolor=flet.colors.BLUE_400, color=flet.colors.WHITE)


def convertButton(convertFunction):
    return flet.TextButton(
        text="Convert",
        on_click=convertFunction,
        width=300,
        height=50,
        style=buttonStyle,
    )


def navBar(page, navigation_handler):
    return flet.NavigationBar(
        on_change=lambda e: navigation_handler(e.control.selected_index),
        destinations=[
            flet.NavigationBarDestination(icon=flet.icons.SOCIAL_DISTANCE_OUTLINED, label="Length"),
            flet.NavigationBarDestination(icon=flet.icons.MONITOR_WEIGHT_OUTLINED, label="Weight"),
            flet.NavigationBarDestination(icon=flet.icons.DATA_USAGE_OUTLINED, label="Data"),
            flet.NavigationBarDestination(icon=flet.icons.CURRENCY_EXCHANGE_OUTLINED, label="Currency"),
        ],
    )



def length_view(page: flet.Page):
    def convertLength(e):
        error = helpers.check_for_invalid_input([cm.value, inc.value, ft.value, mi.value, kl.value], page)
        if error:
            return
        cm.value, inc.value, ft.value, mi.value, kl.value = helpers.oneLengthToOther(
            cm.value, inc.value, ft.value, mi.value, kl.value
        )
        page.update()

    def emptyLengthInputs(e):
        cm.value = inc.value = ft.value = mi.value = kl.value = ""
        page.update()

    cm = helpers.create_text_field(page, "Centimetre", emptyLengthInputs)
    inc = helpers.create_text_field(page, "Inch", emptyLengthInputs)
    ft = helpers.create_text_field(page, "Foot", emptyLengthInputs)
    mi = helpers.create_text_field(page, "Mile", emptyLengthInputs)
    kl = helpers.create_text_field(page, "Kilometre", emptyLengthInputs)

    return flet.Column(
        controls=[
            cm, inc, ft, mi, kl,
            convertButton(convertLength),
        ],
        alignment=flet.MainAxisAlignment.CENTER,
        horizontal_alignment=flet.CrossAxisAlignment.CENTER,
        spacing=30,
        height=600
    )



def weight_view(page: flet.Page):
    def convertWeight(e):
        error = helpers.check_for_invalid_input([gram.value, kilo.value, pound.value, ounce.value], page)
        if error:
            return
        gram.value, kilo.value, pound.value, ounce.value = helpers.oneWeightToOther(
            gram.value, kilo.value, pound.value, ounce.value
        )
        page.update()

    def emptyWeightInputs(e):
        gram.value = kilo.value = pound.value = ounce.value = ""
        page.update()

    gram = helpers.create_text_field(page, "Gram", emptyWeightInputs)
    kilo = helpers.create_text_field(page, "Kilogram", emptyWeightInputs)
    pound = helpers.create_text_field(page, "Pound", emptyWeightInputs)
    ounce = helpers.create_text_field(page, "Ounce", emptyWeightInputs)

    return flet.Column(
        controls=[
            gram, kilo, pound, ounce,
            convertButton(convertWeight),
        ],
        alignment=flet.MainAxisAlignment.CENTER,
        horizontal_alignment=flet.CrossAxisAlignment.CENTER,
        spacing=30,
        height=600
    )



def data_view(page: flet.Page):
    def convertData(e):
        error = helpers.check_for_invalid_input([byte.value, megabyte.value, gigabyte.value, terabyte.value], page)
        if error:
            return
        byte.value, megabyte.value, gigabyte.value, terabyte.value = helpers.oneDataToOthers(
            byte.value, megabyte.value, gigabyte.value, terabyte.value
        )
        page.update()

    def emptyDataInputs(e):
        byte.value = megabyte.value = gigabyte.value = terabyte.value = ""
        page.update()

    byte = helpers.create_text_field(page, "Byte", emptyDataInputs)
    megabyte = helpers.create_text_field(page, "Megabyte", emptyDataInputs)
    gigabyte = helpers.create_text_field(page, "Gigabyte", emptyDataInputs)
    terabyte = helpers.create_text_field(page, "Terabyte", emptyDataInputs)

    return flet.Column(
        controls=[
            byte, megabyte, gigabyte, terabyte,
            convertButton(convertData),
        ],
        alignment=flet.MainAxisAlignment.CENTER,
        horizontal_alignment=flet.CrossAxisAlignment.CENTER,
        spacing=30,
        height=600
    )


def currency_view(page: flet.Page):
    api_token = page.client_storage.get("api_token")

    def convertCurrency(e):
        try:
            usd.value, irr.value, eur.value, cny.value = helpers.oneCurrencyToOther(
                api_token, usd.value, irr.value, eur.value, cny.value
            )
        except Exception as e:
            helpers.show_error(page, f"{e.error_code} : {e.error_message}")
        page.update()

    def emptyCurrencyInputs(e):
        usd.value = irr.value = eur.value = cny.value = ""
        page.update()

    usd = helpers.create_text_field(page, "US Dollar", emptyCurrencyInputs)
    irr = helpers.create_text_field(page, "Iranian Rial", emptyCurrencyInputs)
    eur = helpers.create_text_field(page, "Euro", emptyCurrencyInputs)
    cny = helpers.create_text_field(page, "Chinese Yuan", emptyCurrencyInputs)

    return flet.Column(
        controls=[
            usd, irr, eur, cny,
            convertButton(convertCurrency),
        ],
        alignment=flet.MainAxisAlignment.CENTER,
        horizontal_alignment=flet.CrossAxisAlignment.CENTER,
        spacing=30,
        height=600
    )
