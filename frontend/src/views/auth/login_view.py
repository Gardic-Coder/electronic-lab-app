import flet as ft
from services.api import api_request
from services.auth_context import auth_context

def create_login_view(page: ft.Page):
    # Controles
    email_field = ft.TextField(
        label="Correo Institucional",
        keyboard_type=ft.KeyboardType.EMAIL,
        autofocus=True,
        expand=True
    )
    
    password_field = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        expand=True
    )
    
    error_message = ft.Text(color="red", visible=False)
    loading_indicator = ft.ProgressRing(visible=False)
    
    # Botón de login
    login_button = ft.ElevatedButton(
        text="Iniciar Sesión",
        icon=ft.Icons.LOGIN,
        on_click=lambda e: handle_login(e),
        expand=True
    )
    
    # Manejador de login
    def handle_login(e):
        # Mostrar indicador de carga
        loading_indicator.visible = True
        error_message.visible = False
        page.update()
        
        # Obtener datos del formulario
        email = email_field.value
        password = password_field.value
        
        # Validar campos
        if not email or not password:
            show_error("Por favor complete todos los campos")
            return
        
        # Hacer solicitud al backend
        response = api_request(
            "/login",
            method="POST",
            json={
                "identifier": email,
                "password": password
            }
        )
        
        if response and response.status_code == 200:
            token = response.json().get("access_token")
            user_data = response.json().get("user")
            
            # Guardar en contexto de autenticación
            auth_context.login(token, user_data)
            
            # Guardar token en sesión
            page.session.set("token", token)
            
            # Redirigir según rol
            if user_data["rol"] == "estudiante":
                page.go("/dashboard/student")
            elif user_data["rol"] == "encargado":
                page.go("/dashboard/staff")
            elif user_data["rol"] == "admin":
                page.go("/dashboard/admin")
        else:
            error_msg = "Credenciales inválidas"
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
        route="/login",
        controls=[
            ft.AppBar(title=ft.Text("Laboratorio de Electrónica")),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Inicio de Sesión", 
                                size=24, 
                                weight="bold",
                                text_align=ft.TextAlign.CENTER),
                        ft.Divider(),
                        email_field,
                        password_field,
                        ft.Row(
                            controls=[
                                loading_indicator,
                                login_button
                            ],
                            alignment=ft.MainAxisAlignment.END
                        ),
                        error_message,
                        ft.Row(
                            controls=[
                                ft.Text("¿No tienes cuenta?"),
                                ft.TextButton(
                                    text="Regístrate aquí",
                                    on_click=lambda _: page.go("/register")
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