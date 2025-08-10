import flet as ft
from views.home import home_view




def main(page: ft.Page):
    def router(route):
        page.clean()
        if page.route == "/":
            home_view(page)
        #elif page.route == "/login":
            #login_view(page)

    page.on_route_change = router
    page.go(page.route)

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir="assets", port=8550)