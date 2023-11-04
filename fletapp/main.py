import flet as ft
import views as views_handle

def main(page: ft.Page):
    
    #defining the fonts
    page.fonts = {
        "SF Pro": "https://raw.githubusercontent.com/google/fonts/master/ofl/sfprodisplay/SFProDisplay-Bold.ttf",
    }
    
    #defining the window size
    page.window_max_width = 410
    page.window_width = 800
    page.window_max_height = 800
    page.window_height = 800

    page.title = "Project 334 Appication"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.HIDDEN
    page.padding = 0
    page.bgcolor = "#ddf7f1"

    page.navigation_bar = ft.NavigationBar(bgcolor = "#fe96a5",selected_index=2,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.CHECK, ),
            ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG, ),
            ft.NavigationDestination(icon=ft.icons.HOME, ),
            ft.NavigationDestination(icon=ft.icons.CALCULATE, ),
            ft.NavigationDestination(icon=ft.icons.PERSON, ),
        ]
    )

    def route_change(route):
        print(page.route)
        # CLEAR ALL PAGE
        page.views.clear()
        page.views.append(
            views_handle.views(page)[page.route],
        )
        page.navigation_bar.selected_index = 2
        page.update()
            
    page.on_route_change = route_change
    page.go('/')

ft.app(target = main)