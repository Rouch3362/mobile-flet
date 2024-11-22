import flet
import views

def main(page: flet.Page):
    page.title = "Unit Converter"

    


    page.views.append(views.length_view(page))
    page.navigation_bar = views.navBar(page)
    title = flet.Row([flet.Text("Unit Convertor", weight=flet.FontWeight.W_500, size=28, text_align=flet.TextAlign.CENTER)],alignment=flet.MainAxisAlignment.CENTER)
    page.overlay.append(title)

    page.update()

flet.app(main)