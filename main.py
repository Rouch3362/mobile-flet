import flet
import views

def main(page: flet.Page):
    page.title = "Unit Converter"

    if page.client_storage.get("api_token") == None:
        def on_submit(e):
            page.client_storage.set("api_token", input_field.value)
            modal.open = False
            page.update()

        input_field = flet.TextField(label="Enter API Token:", autofocus=True)

        modal = flet.AlertDialog(
            title=flet.Text("User Input"),
            content=flet.Column(
                [
                    input_field,
                    flet.ElevatedButton("Submit", on_click=on_submit),
                ],
                tight=True,
            ),
            modal=True,
        )

        # Shows the modal dialog when the app opens
        modal.open = True
        page.overlay.append(modal)


    def show_error(text):
        snack_bar = flet.SnackBar(
            flet.Text(value=text, color=flet.colors.WHITE, text_align=flet.TextAlign.CENTER), 
            bgcolor=flet.colors.RED,
            show_close_icon=True,
            close_icon_color=flet.colors.WHITE
        )
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    page.views.append(views.length_view(page))
    page.navigation_bar = views.navBar(page)
    title = flet.Row([flet.Text("Unit Convertor", weight=flet.FontWeight.W_500, size=28, text_align=flet.TextAlign.CENTER)],alignment=flet.MainAxisAlignment.CENTER)
    page.overlay.append(title)

    page.update()

flet.app(main)