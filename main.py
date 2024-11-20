import flet
import views

def main(page: flet.Page):
    page.title = "Unit Converter"

    


    page.views.append(views.length_view(page))
    page.navigation_bar = views.navBar(page)
    page.update()

flet.app(main)