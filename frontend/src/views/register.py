import flet as ft

def register_view(page: ft.Page):
    def register(e):
        # Aquí iría la lógica de registro
        print("Registrarse")
    
    controles = [
            ft.Text("Registro", style=ft.TextStyle(size=24)),
            ft.TextField(label="Cedula", autofocus=True),
            ft.TextField(label="Nombre", autofocus=True),
            ft.TextField(label="Apellido", autofocus=True),
            ft.TextField(label="Correo Electrónico"),
            ft.TextField(label="Contraseña", password=True),
            ft.ElevatedButton("Registrarse", on_click=register),
            ft.TextButton("¿Ya tienes una cuenta? Inicia Sesión", on_click=lambda e: page.go("/login")),
            ft.ElevatedButton("Volver al Inicio", on_click=lambda e: page.go("/"))
            ]

    view = ft.View(
        route="/register",
        controls=controles,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        appbar=ft.AppBar(title=ft.Text("Registrarse"))
    )

    return view