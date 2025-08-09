import flet as ft
from services.api import api_request

def create_register_view(page: ft.Page):
    # Controles
    cedula_field = ft.TextField(
        label="Cédula",
        keyboard_type=ft.KeyboardType.NUMBER,
        autofocus=True,
        expand=True
    )
    
    nombre_field = ft.TextField(
        label="Nombre",
        expand=True
    )
    
    apellido_field = ft.TextField(
        label="Apellido",
        expand=True
    )
    
    email_field = ft.TextField(
        label="Correo Institucional",
        keyboard_type=ft.KeyboardType.EMAIL,
        expand=True
    )
    
    password_field = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        expand=True
    )
    
    confirm_password_field = ft.TextField(
        label="Confirmar Contraseña",
        password=True,
        can_reveal_password=True,
        expand=True
    )
    
    error_message = ft.Text(color="red", visible=False)
    loading_indicator = ft.ProgressRing(visible=False)
    
    # Botón de registro
    register_button = ft.ElevatedButton(
        text="Registrarse",
        icon=ft.Icons.APP_REGISTRATION,
        on_click=lambda e: handle_register(e),
        expand=True
    )
    
    # Manejador de registro
    def handle_register(e):
        # Mostrar indicador de carga
        loading_indicator.visible = True
        error_message.visible = False
        page.update()
        
        # Obtener datos del formulario
        cedula = cedula_field.value
        nombre = nombre_field.value
        apellido = apellido_field.value
        email = email_field.value
        password = password_field.value
        confirm_password = confirm_password_field.value
        
        # Validar campos
        if not all([cedula, nombre, apellido, email, password, confirm_password]):
            show_error("Por favor complete todos los campos")
            return
        
        # Validar contraseñas
        if password != confirm_password:
            show_error("Las contraseñas no coinciden")
            return
        
        # Crear payload
        payload = {
            "cedula": cedula,
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "password": password,
            "rol": "estudiante"  # Rol por defecto
        }
        
        # Hacer solicitud al backend
        response = api_request(
            "/register",
            method="POST",
            json=payload
        )
        
        if response and response.status_code == 201:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("¡Registro exitoso! Por favor inicia sesión"),
                open=True
            )
            page.go("/login")
        else:
            error_msg = "Error en el registro"
            if response and response.json().get("detail"):
                error_msg = response.json()["detail"]
            show_error(error_msg)
    
    def show_error(message):
        loading_indicator.visible = False
        error_message.value = message
        error_message.visible = True
        page.update()
    
    # Crear vista
    view = ft.View(
        route="/register",
        controls=[
            ft.AppBar(title=ft.Text("Laboratorio de Electrónica")),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Registro de Usuario", 
                                size=24, 
                                weight="bold",
                                text_align=ft.TextAlign.CENTER),
                        ft.Divider(),
                        cedula_field,
                        ft.Row(
                            controls=[nombre_field, apellido_field],
                            spacing=10
                        ),
                        email_field,
                        ft.Row(
                            controls=[password_field, confirm_password_field],
                            spacing=10
                        ),
                        ft.Row(
                            controls=[
                                loading_indicator,
                                register_button
                            ],
                            alignment=ft.MainAxisAlignment.END
                        ),
                        error_message,
                        ft.Row(
                            controls=[
                                ft.Text("¿Ya tienes cuenta?"),
                                ft.TextButton(
                                    text="Inicia sesión aquí",
                                    on_click=lambda _: page.go("/login")
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                ),
                padding=ft.padding.symmetric(horizontal=30, vertical=20),
                expand=True
            )
        ]
    )
    
    return view