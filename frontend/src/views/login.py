# frontend/src/views/login.py
import flet as ft
from service.api import api_request
from service.auth_context import auth_context
from service.validate import validate_login
import asyncio


def login_view(page: ft.Page):
    identifier_field = ft.TextField(label="Correo o Cedula", autofocus=True)
    password_field = ft.TextField(label="Contraseña", password=True)

    if auth_context.is_authenticated():
        page.go("/dashboard")
        return 

    async def login(e):
        identifier = identifier_field.value
        password = password_field.value

        # Enviar datos al backend
        response = await api_request(
            endpoint="/login",
            method="POST",
            json={  # ✅ corregido
                "identifier": identifier,
                "password": password
            }
        )


        # Verificar respuesta
        if response.get("success"):
            user_data = response.get("user")
            token = response.get("token")

            # Guardar sesión
            auth_context.login(token, user_data)

            # Redirigir al dashboard
            page.go("/dashboard")
        else:
            # Mostrar error general
            page.snack_bar = ft.SnackBar(
                ft.Text("Credenciales incorrectas o usuario no encontrado."),
                open=True
            )
        page.update()
    
    def validate(e):

        errors = validate_login(
            identifier_field.value,
            password_field.value
        )
        
        if errors:
            show_errors(errors)
            return
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(login(e))

        #asyncio.create_task(login(e))  # ✅ Ejecuta la función async. Solo llama a login si todo está validado

    def show_errors(errors: dict):
        identifier_field.error_text = errors.get("identifier")
        password_field.error_text = errors.get("password")
        page.update()


    
    controles = [
            ft.Text("Inicio de Sesión", style=ft.TextStyle(size=24)),
            identifier_field,
            password_field,
            ft.ElevatedButton("Iniciar Sesión", on_click=validate),
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
    