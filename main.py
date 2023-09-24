import flet as ft

def main(page: ft.Page):
    page.title = "Flet Page"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

ft.app(target=main)