from flet import *
import flet as ft
from homepage import Home
#from todo import main
from tobuy_new import ToBuyMain
from calculator_new2 import Calculator
from signup import SignupMain
from login import LoginMain
from forgetpass import ForgetMain

class ChangeNav(ft.UserControl):
    def __init__(self, page, selected_index):
        super().__init__()
        self.page = page
        self.index = selected_index

    def changetab(self):
        destinations = ['/', '/tobuy', '/', '/calculator', '/login']
        destination_url = destinations[self.index]
        self.page.go(destination_url)

    def build(self):
        print(self.index)  # Note: This print statement should be inside the build method
        return None  # You need to return something from the build method, even if it's None

def navBar(selectedIndex):
    return ft.NavigationBar(bgcolor="#fe96a5", selected_index=selectedIndex,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.CHECK),
            ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG),
            ft.NavigationDestination(icon=ft.icons.HOME),
            ft.NavigationDestination(icon=ft.icons.CALCULATE),
            ft.NavigationDestination(icon=ft.icons.PERSON),
        ],
        on_change=lambda e: ChangeNav(e.page, e.control.selected_index).changetab(),
    )

def views(page):
    return {
        '/': View(
            route='/',
            controls=[
                Home(page)
            ]
        ),
        
        '/todo': View(
            route='/todo/',
            controls=[
                #main(page)
            ]
        ),
        '/tobuy': View(
            route='/tobuy/',
            controls=[
                ToBuyMain(page)
            ]
        ),
        '/calculator': View(
            route='/calculator/',
            controls=[
                Calculator(page)
            ],
            navigation_bar=navBar(3)
        ),
        '/signup': View(
            route='/signup/',
            controls=[
                SignupMain(page)
            ]
        ),
        '/login': View(
            route='/login/',
            controls=[
                LoginMain(page)
            ]
        ),
        '/forgetpass': View(
            route='/forgetpass/',
            controls=[
                ForgetMain(page)
            ]
        ),
        
    }