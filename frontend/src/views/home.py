# frontend/src/views/home.py
import flet as ft
from service.auth_context import auth_context

def home_view(page: ft.Page):
    if auth_context.is_authenticated():
        page.go("/dashboard")
        return 
    
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