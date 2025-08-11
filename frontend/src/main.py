# frontend/src/main.py
import flet as ft
from views.login import login_view
from views.home import home_view
from views.register import register_view
from views.dashboard import dashboard_view
from views.dashboards.encargado import encargado_view
from views.dashboards.admin import admin_view
from views.dashboards.estudiante import estudiante_view

def main(page: ft.Page):
    
    # Configurar la vista inicial
    def route_change(e):
        page.views.clear()

        if e.route == "/":
            page.views.append(home_view(page))

        elif e.route == "/login":
            page.views.append(login_view(page))

        elif e.route == "/register":
            page.views.append(register_view(page))
        
        elif e.route == "/dashboard":
            page.views.append(dashboard_view(page))

        elif e.route == "/dashboard/Admin":
            page.views.append(admin_view(page))

        elif e.route == "/dashboard/encargado":
            page.views.append(encargado_view(page))

        elif e.route == "/dashboard/estudiante":
            page.views.append(estudiante_view(page))
            
        else:
            page.views.append(home_view(page))
        
        page.update()
    
    # Manejar eventos de retroceso
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        page.update()


    # Configurar manejadores de eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Cargar vista inicial
    page.go(page.route)

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550)