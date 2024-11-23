import flet
import views

def main(page: flet.Page):
    page.title = "Unit Converter"

    
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
    page.update()

flet.app(main)