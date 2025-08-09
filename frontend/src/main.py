import flet as ft

def main(page: ft.Page):
    page.title = "Electronic Lab"
    page.add(ft.Text("¡Hola desde Flet!"))

ft.app(target=main)