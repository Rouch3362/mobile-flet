import flet
import views
import time

def main(page: flet.Page):
    page.title = "Unit Converter"

    # Check for API token
    if page.client_storage.get("api_token") is None:
        def on_submit(e):
            page.client_storage.set("api_token", input_field.value)
            modal.open = False
            page.update()

        input_field = flet.TextField(label="Enter API Token:", autofocus=True)

        modal = flet.AlertDialog(
            title=flet.Text("User Input"),
            content=flet.Column(
                [input_field, flet.ElevatedButton("Submit", on_click=on_submit)],
                tight=True,
            ),
            modal=True,
        )
        modal.open = True
        page.overlay.append(modal)

    
    content_container = flet.Container()

    def fade_in(element, duration=0.5):
        steps = 10
        step_duration = duration / steps
        opacity = 0.0
    
        for _ in range(steps):
            opacity += 1 / steps
            element.opacity = opacity
            page.update()
            time.sleep(step_duration)

    
    def navigation_handler(selected_index):
        if selected_index == 0:
            content_container.content = views.length_view(page)
        elif selected_index == 1:
            content_container.content = views.weight_view(page)
        elif selected_index == 2:
            content_container.content = views.data_view(page)
        elif selected_index == 3:
            content_container.content = views.currency_view(page)
        
        fade_in(content_container)

        page.update()

   
    page.navigation_bar = views.navBar(page, navigation_handler)

    
    content_container.content = views.length_view(page)
    
    title = flet.Row([flet.Text("Unit Convertor", weight=flet.FontWeight.W_500, size=28, text_align=flet.TextAlign.CENTER)],alignment=flet.MainAxisAlignment.CENTER)
    page.overlay.append(title)
    
    page.add(content_container)


flet.app(target=main, assets_dir="assets")
