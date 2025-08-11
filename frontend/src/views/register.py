# frontend/src/views/register.py
import flet as ft
from service.api import api_request
from service.auth_context import auth_context
from service.validate import validate_register
import asyncio

def register_view(page: ft.Page):
    cedula_field = ft.TextField(label="Cedula", autofocus=True)
    name_field = ft.TextField(label="Nombre")
    surname_field = ft.TextField(label="Apellido")
    email_field = ft.TextField(label="Correo Electrónico")
    password_field = ft.TextField(label="Contraseña", password=True)
    confirm_password_field = ft.TextField(label="Confirmar Contraseña", password=True)

    if auth_context.is_authenticated():
        page.go("/dashboard")
        return 

    async def register(e):
        cedula = cedula_field.value
        name = name_field.value
        surname = surname_field.value
        email = email_field.value
        password = password_field.value

        # Enviar datos al backend
        response = await api_request(
            endpoint="/register",
            method="POST",
            json={  
                "cedula": cedula,
                "nombre": name,
                "apellido": surname,
                "email": email,
                "password": password
            }
        )


        # Verificar respuesta
        if response.get("success"):
            page.snack_bar = ft.SnackBar(
                ft.Text("Registro exitoso. Ahora puedes iniciar sesión."),
                open=True
            )
            page.go("/login")  # ✅ redirige al login

        else:
            # Mostrar error general
            error_msg = response.get("error", "Error al registrar usuario.")
            page.snack_bar = ft.SnackBar(
                ft.Text(error_msg),
                open=True
            )

        page.update()

    
    def validate(e):
        errors = validate_register(
            cedula_field.value,
            name_field.value,
            surname_field.value,
            email_field.value,
            password_field.value,
            confirm_password_field.value
        )
        
        if errors:
            show_errors(errors)
            return
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(register(e))

        # ✅ Ejecuta la función async. Solo llama a register si todo está validado

    def show_errors(errors: dict):
        cedula_field.error_text = errors.get("cedula")
        name_field.error_text = errors.get("nombre")
        surname_field.error_text = errors.get("apellido")
        email_field.error_text = errors.get("email")
        password_field.error_text = errors.get("password")
        page.update()
    
    controles = [
            ft.Text("Registro", style=ft.TextStyle(size=24)),
            cedula_field,
            name_field,
            surname_field,
            email_field,
            password_field,
            confirm_password_field,
            ft.ElevatedButton("Registrarse", on_click=validate),
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