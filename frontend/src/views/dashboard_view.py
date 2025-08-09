import flet as ft
from services.auth_context import auth_context

def create_dashboard_view(page: ft.Page, role: str):
    # Función para cerrar sesión
    def logout(e):
        page.session.remove("token")
        auth_context.logout()
        page.go("/login")
    
    # Crear barra de navegación
    appbar = ft.AppBar(
        title=ft.Text(f"Panel de {role.capitalize()}"),
        actions=[
            ft.IconButton(ft.Icons.NOTIFICATIONS),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Perfil"),
                    ft.PopupMenuItem(text="Cerrar sesión", on_click=logout)
                ]
            )
        ]
    )
    
    # Contenido principal
    content = ft.Column(
        controls=[
            ft.Text(f"Bienvenido, {auth_context.user_data['nombre']}!", size=24),
            ft.Text(f"Rol: {role.capitalize()}"),
            ft.FilledButton(
                text="Ver componentes disponibles",
                icon=ft.Icons.INVENTORY_2,
                on_click=lambda _: page.go("/components")
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )
    
    # Crear vista
    view = ft.View(
        route=f"/dashboard/{role}",
        appbar=appbar,
        controls=[content]
    )
    
    return view