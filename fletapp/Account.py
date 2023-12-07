import flet as ft

def get_user_status(user): 
    if user is None:
        return "Guest"
    else:
        return user  # You may want to replace this with the actual check for logged-in users
    
def page_builder(self, user):
    user_status = user

    if user_status == "Guest":
        return guest_content(self)
    else:
        return user_content(self)

def guest_content(self):
    return ft.Column([
        ft.Text("Please log in to the system\n\n", color="#737373", size=14),
        ft.Row([
            ft.ElevatedButton("Login",
                bgcolor="red",
                color="white",
                width=120,
                on_click=lambda e: self.page.go('/login'),
            ),
        ], alignment=ft.MainAxisAlignment.CENTER),
    ])

def user_content(self):
    return ft.Column([
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

def logout(self):
    self.page.client_storage.clear()
    self.user = None
    self.page.update()

class AccountMain(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.user = page.client_storage.get("email")

    def build(self):
        user_status = get_user_status(self.user)
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
                content=ft.Container(
                    ft.Column(
                        [
                            ft.Row([
                                ft.Text("Account", color="#000000", size=28, weight=ft.FontWeight.BOLD,),
                            ], alignment=ft.MainAxisAlignment.CENTER),
                            ft.Text(f"{user_status} mode", color="#000000", size=20, weight=ft.FontWeight.BOLD),
                            page_builder(self,user_status),  # Pass the user to the method
                        ],
                        width=350,
                    )
                )
            )
        )
