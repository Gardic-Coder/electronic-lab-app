import flet as ft

def login_view(page: ft.Page):
    def login(e):
        # Aquí iría la lógica de inicio de sesión
        print("Iniciar sesión")
    
    controles = [
            ft.Text("Inicio de Sesión", style=ft.TextStyle(size=24)),
            ft.TextField(label="Correo o Cedula", autofocus=True),
            ft.TextField(label="Contraseña", password=True),
            ft.ElevatedButton("Iniciar Sesión", on_click=login),
            ft.TextButton("¿No tienes una cuenta? Regístrate", on_click=lambda e: page.go("/register")),
            ft.ElevatedButton("Volver al Inicio", on_click=lambda e: page.go("/"))
            ]

    view = ft.View(
        route="/login",
        controls=controles,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        appbar=ft.AppBar(title=ft.Text("Iniciar Sesión"))
    )

    return view
    