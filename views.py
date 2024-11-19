import flet
import helpers

buttonStyle = flet.ButtonStyle(
    bgcolor=flet.colors.BLUE_400,
    color=flet.colors.WHITE,
)

def convertButton(convertFunction):
    return flet.TextButton(
        text="Convert", 
        on_click=convertFunction,
        width=300,
        height=50,
        style=buttonStyle,
        visible=True
        )



def validate_input(e: flet.ControlEvent,page):
    if not e.control.value.isdigit():  # Check if the input is not numeric
        error_label.value = "Please enter a valid number"
        error_label.color = flet.colors.RED
        print(e.target[0])
    else:
        error_label.value = ""
    page.update()


# Label to display errors
error_label = flet.Text(value="", color=flet.colors.RED)

def navigationHandler(e,page: flet.Page):
    if e.control.selected_index == 0:
        page.views.clear()
        page.views.append(length_view(page)) 
    elif e.control.selected_index == 1:
        page.views.clear()
        page.views.append(weight_view(page))
    elif e.control.selected_index == 2:
        page.views.clear()
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
        selected_index=0
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

    inc = flet.TextField(on_change=lambda e: validate_input(e, page),label="Inch")
    cm = flet.TextField(on_change=lambda e: validate_input(e, page),label="Centimetre", on_focus=emptyLengthInputs)
    ft = flet.TextField(on_change=lambda e: validate_input(e, page),label="Foot", on_focus=emptyLengthInputs)
    mi = flet.TextField(on_change=lambda e: validate_input(e, page),label="Mile", on_focus=emptyLengthInputs)
    kl = flet.TextField(on_change=lambda e: validate_input(e, page),label="Kilometre", on_focus=emptyLengthInputs)
                

    return flet.View(
            "/length",
            controls=[
                error_label,
                cm,
                inc,
                ft,
                mi,
                kl,
                convertButton(convertLength)]
                ,
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

    gram  = flet.TextField(on_change=lambda e: validate_input(e, page),label="Gram", on_focus=emptyWeightInputs)
    kilo  = flet.TextField(on_change=lambda e: validate_input(e, page),label="Kilogram", on_focus=emptyWeightInputs)
    pound = flet.TextField(on_change=lambda e: validate_input(e, page),label="Pound", on_focus=emptyWeightInputs)
    ounce  = flet.TextField(on_change=lambda e: validate_input(e, page),label="Ounce", on_focus=emptyWeightInputs)

        
    return flet.View(
        "/weight",
        [
            error_label,
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

    byte  = flet.TextField(on_change=lambda e: validate_input(e, page),label="Byte", on_focus=emptyDataInputs)
    megabyte  = flet.TextField(on_change=lambda e: validate_input(e, page),label="Megabyte", on_focus=emptyDataInputs)
    gigabyte = flet.TextField(on_change=lambda e: validate_input(e, page),label="Gigabyte", on_focus=emptyDataInputs)
    terabyte  = flet.TextField(on_change=lambda e: validate_input(e, page),label="Terabyte", on_focus=emptyDataInputs)

    
    return flet.View(
        "/data",
            [
            error_label,
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