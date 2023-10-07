import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Flet Page"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

ft.app(target=main)