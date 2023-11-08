import flet as ft
import requests
from urllib.parse import urlparse

def main(page: ft.Page):
    page.title = "Flet Main Page"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    youparams = "watermelon"

    def route_change(route):
        # CLEAR ALL PAGE
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                ft.AppBar(title=ft.Text("Home Page", size=30,
                    color="white"
                    ),
                    bgcolor="red500",
                    ),
                    # PAGE ROUTE IS PATH YOU URL HERE
                    ft.Text(page.route),
                    ft.ElevatedButton(
                        "Go to Second Page",
                        on_click=lambda _: page.go(f"/secondpage/{youparams}")
                        )
                    ]
                    )
            )
        # GET PARAM FROM HOME PAGE
        param = page.route
        # THIS IS GET VALUE AFTER /secondpage/THIS RES HERE
        res = urlparse(param).path.split("/")[-1]
        print(f"test res is : {res}")
        
        if page.route == f"/secondpage/{res}":
            page.views.append(
                ft.View(
                # IF URL ACCESS HERE THEN PUSH TO VIEW HERE
                f"/secondpage/{res}",
                [
                    # LIKE BEFORE
                    # RENDER YOU PAGE HERE
                    ft.AppBar(title=ft.Text("SECOND PAGE", 
                        color="white",
                        size=30),
                        bgcolor="blue500",
                        ),
                    # PAGE ROUTE IS PATH YOU URL HERE
                    ft.Text(page.route),
                    ft.Text(f"you params is {res}"),
                    ft.ElevatedButton(
                        "BACK TO HOME PAGE",
                        on_click=lambda _: page.go("/")
                        )

                    ]
                    )
                )
    page.update()

    def view_pop(view):
        page.views.pop()
        myview = page.views[-1]
        page.go(myview.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    p = ft.TemplateRoute(page.route)
    if p.match("/second/:id"):
        print("you here ", p.id)
    else:
        print("whatever")

ft.app(target=main)
