import flet as ft
from service.auth_context import auth_context

def admin_view(page: ft.Page):
    if not auth_context.is_authenticated():
        page.go("/login")
        return 
    
    def logout(e):
        auth_context.logout()
        page.go("/")

    user = auth_context.user_data

    if user['rol'] != 'admin':
        page.go("/dashboard")
        return

    controles = [
            ft.Text("Bienvenido al Dashboard de Admin", style=ft.TextStyle(size=24)),
            ft.Text(f"Bienvenido {user['nombre']}"),
            ft.ElevatedButton("Cerrar sesión", on_click=logout)
            ]

    view = ft.View(
        route="/dashboard/Admin",
        controls=controles,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        appbar=ft.AppBar(title=ft.Text("Dashboard Admin"))
    )

    return view