import flet
import helpers

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

    if e.control.selected_index == 0:
        page.go("/length")
        page.views.append(length_view(page)) 
    elif e.control.selected_index == 1:
        page.go("/weight")
        page.views.append(weight_view(page))
    elif e.control.selected_index == 2:
        page.go("/data")
        page.views.append(data_view(page))
    
    page.update()


def navBar(page):
    return flet.NavigationBar(
        on_change=lambda e: navigationHandler(e, page),
        destinations=[
            flet.NavigationBarDestination(icon=flet.icons.SOCIAL_DISTANCE_OUTLINED, label="Length"),
            flet.NavigationBarDestination(icon=flet.icons.MONITOR_WEIGHT_OUTLINED, label="Weight"),
            flet.NavigationBarDestination(icon=flet.icons.DATA_USAGE_OUTLINED, label="Data")
        ],
        selected_index=helpers.get_current_page(page)
) 



def length_view(page: flet.Page):

    def convertLength(e):
        cm.value , inc.value, ft.value, mi.value, kl.value = helpers.oneLengthToOther(cm.value,inc.value, ft.value, mi.value, kl.value)
        page.update()

    def emptyLengthInputs(e):
        cm.value  = ""
        inc.value = ""
        ft.value  = ""
        mi.value  = ""
        kl.value  = ""
        page.update()

    inc = helpers.create_text_field(page, "Inch")
    cm  = helpers.create_text_field(page, "Centimetre")
    ft  = helpers.create_text_field(page, "Foot")
    mi  = helpers.create_text_field(page, "Mile")
    kl  = helpers.create_text_field(page, "Kilometre")
                

    return flet.View(
            "/length",
            controls=[
                helpers.error_label,
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
    
    gram  = helpers.create_text_field(page,"Gram")
    kilo  = helpers.create_text_field(page, "Kilogram")
    pound = helpers.create_text_field(page, "Pound")
    ounce = helpers.create_text_field(page, "Ounce")

        
    return flet.View(
        "/weight",
        [
            helpers.error_label,
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

    byte      = helpers.create_text_field(page, "Byte")
    megabyte  = helpers.create_text_field(page, "Megabyte")
    gigabyte  = helpers.create_text_field(page, "Gigabyte")
    terabyte  = helpers.create_text_field(page, "Terabyte")

    
    return flet.View(
        "/data",
            [
            helpers.error_label,
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