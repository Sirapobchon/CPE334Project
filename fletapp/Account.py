import flet as ft

def type(self):
    if self.user == None:
        print("GUEST")
    else:
        print("{self.user['email']}")

class AccountMain(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.user = page.client_storage.get("email")
    
    def build(self):
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
                #rotation=math.pi / 4,
            ),
            width=800,
            height=2000,
            expand=True, 
            content = ft.Container(  
                ft.Column(
                    [
                        ft.Row([
                            ft.Text("Account", color = "#000000" ,size=28, weight=ft.FontWeight.BOLD,),
                            ], alignment=ft.MainAxisAlignment.CENTER),
                        # ft.Text("Account", color = "#000000" ,size=28, weight=ft.FontWeight.BOLD, alignment = ft.alignment.center),
                        ft.Text("Guess mode", color = "#000000" , size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("Please log in to the system\n\n", color = "#737373", size=14),
                        #type(self),
                        #print(self.user),
                        ft.Row([
                            ft.ElevatedButton("login",
                                bgcolor = "red", 
                                color="white",
                                width=120,
                                on_click=lambda e: self.page.go('/login'),),
                            ], alignment=ft.MainAxisAlignment.CENTER,),
                        # ft.Text("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"),           

                        # ft.ElevatedButton("login",bgcolor = "red", color="white",
                        #            on_click = login_button, width=120),
                        # name_field, 
                        # email_field,
                        # password_field,
                        # ft.Row([update_button, logout_button], alignment="spaceBetween")
                    ],
                    
                    width = 350,
                )
            )
        )
    )