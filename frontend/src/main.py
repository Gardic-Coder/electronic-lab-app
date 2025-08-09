import flet as ft
from services.auth_context import auth_context
from views.auth.login_view import create_login_view
from views.auth.register_view import create_register_view
from views.dashboard_view import create_dashboard_view

def main(page: ft.Page):
    # Configuración inicial
    page.title = "Gestión de Laboratorio Electrónico"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0
    
    # Verificar si hay token almacenado
    token = page.session.get("token")
    if token:
        # Aquí deberías verificar el token con el backend
        # Por simplicidad, asumimos que es válido
        auth_context.token = token
        
        # Obtener datos del usuario (en una app real, esto vendría del backend)
        auth_context.user_data = {
            "nombre": "Usuario Demo",
            "rol": "estudiante"  # Esto debería venir de la API
        }
        
        # Redirigir a dashboard según rol
        page.go(f"/dashboard/{auth_context.user_data['rol']}")
    else:
        page.go("/login")
    
    # Definir rutas
    def route_change(route):
        page.views.clear()
        
        if page.route == "/login":
            page.views.append(create_login_view(page))
        elif page.route == "/register":
            page.views.append(create_register_view(page))
        elif page.route.startswith("/dashboard/"):
            role = page.route.split("/")[-1]
            page.views.append(create_dashboard_view(page, role))
        else:
            page.views.append(create_login_view(page))
        
        page.update()
    
    # Manejar eventos de retroceso
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
    
    # Configurar manejadores de eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    # Manejar logout
    def handle_logout():
        page.session.remove("token")
        auth_context.logout()
        page.go("/login")
    
    auth_context.on_logout = handle_logout
    
    # Cargar vista inicial
    page.go(page.route)

# Iniciar aplicación
if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER, port=5000)