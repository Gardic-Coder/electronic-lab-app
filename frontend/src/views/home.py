import flet as ft

def home_view(page: ft.Page):
    page.title = "Home"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    controles = [
            ft.Text("Laboratorio de Electronica", style=ft.TextStyle(size=24)),
            ft.ElevatedButton("Iniciar Sesión", on_click=lambda e: page.go("/login")),
            ft.ElevatedButton("Registrarse", on_click=lambda e: page.go("/register"))
            ]

    view = ft.View(
        route="/",
        controls=controles,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        appbar=ft.AppBar(title=ft.Text("Home"))
    )

    return view