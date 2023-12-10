import flet as ft
import pyrebase
import json

fireconfig = {}
fireconfig = json.load(open('fletapp/firebase/firebaseConfig.json', 'r'))
firebase = pyrebase.initialize_app(fireconfig)
db = firebase.database()

def page_builder(self):
    if self.user is None:
        return guest_content(self)
    else:
        return user_content(self)

def guest_content(self):
    return ft.Column([
        ft.Text(
            f"Guest mode", 
            color="#000000", 
            size=20, 
            weight=ft.FontWeight.BOLD
        ),
        ft.Text(
            "Please log in to the system or sign up for an account.\n\n", 
            color="#737373",
            size=14),
        ft.Row([
            ft.ElevatedButton("Login",
                bgcolor="red",
                color="white",
                width=120,
                on_click=lambda e: self.page.go('/login'),
            ),
            ft.ElevatedButton("Sign Up",
                bgcolor="green",
                color="white",
                width=120,
                on_click=lambda e: self.page.go('/signup'),
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),
    ])


def user_content(self):
    try:
        user_data = db.child('users').child(self.user).get().val()
        if user_data and 'username' in user_data and user_data['username'] != "":
            username = user_data['username']
        else:
            username = self.user_email
        return ft.Column([
            ft.Text(
                f"Welcome, {username}", 
                color="#000000", 
                size=20, 
                weight=ft.FontWeight.BOLD
            ),
            ft.Text("Edit Account Information", color="#737373", size=14),
            ft.Row([
                ft.ElevatedButton("Logout",
                    bgcolor="blue",
                    color="white",
                    width=120,
                    on_click=lambda e: logout(self),
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ])
    except Exception as e:
        self.page.client_storage.clear()
        self.user = None
        return ft.Column([
            ft.Text(f"Error retrieving user data: {e}", color="#FF0000", size=16),
            ft.Text("Please log in again", color="#FF0000", size=16),
            ft.Row([
                ft.ElevatedButton("Login",
                    bgcolor="red",
                    color="white",
                    width=120,
                    on_click=lambda e: self.page.go('/login'),
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ])

def logout(self):
    self.page.client_storage.clear()
    self.user = None
    page_builder.update()
    self.page.update()

class AccountMain(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.user = page.client_storage.get("user_id")
        self.user_email = page.client_storage.get("user_email")

    def build(self):
        maincontain = ft.Container(
            ft.Column(
                [
                    ft.Row([
                        ft.Text("Account", color="#000000", size=28, weight=ft.FontWeight.BOLD,),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Container(
                        page_builder(self),  # Pass the user to the method
                        margin=ft.margin.only(left=20,right=20),
                    ),
                ],
                width=320,
            )
        )
        return ft.SafeArea(
            ft.Container(
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[
                        "#ddf7f1",
                        "#f2f8e6",
                        "#fff5e1",
                        "#feddda",
                        "#f1e7f5",
                    ],
                    tile_mode=ft.GradientTileMode.MIRROR,
                ),
                width=800,
                height=2000,
                expand=True,
                content=maincontain,
            )
        )
