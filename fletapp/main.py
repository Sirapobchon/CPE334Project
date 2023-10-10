import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Flet Main Page"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    mainsafe = ft.SafeArea(ft.Text("Hello, Flet!"))
    
    page.add(
        mainsafe
    )


ft.app(target=main)
