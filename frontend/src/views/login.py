import flet as ft

def view_login(page: ft.Page):
    page.title = "Iniciar Sesión"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def login():
        # Aquí iría la lógica de inicio de sesión
        print("Iniciar sesión")
    
    controles = [
            ft.Text("Inicio de Sesión", style=ft.TextStyle(size=24)),
            ft.TextField(label="Correo o Cedula", autofocus=True),
            ft.TextField(label="Contraseña", password=True),
            ft.ElevatedButton("Iniciar Sesión", on_click=login)
            ]

    view = ft.View(
        route="/login",
        controls=[controles]
    )

    return view
    