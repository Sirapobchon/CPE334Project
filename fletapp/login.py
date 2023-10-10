import flet as ft
import math

def main(page : ft.Page):
    #page.theme_mode = ft.ThemeMode.LIGHT
    page.title="Login and Register"

    login = ft.SafeArea(ft.Container(
        #image_src="signinbg.jpg",
        
        #image_fit=ImageFit.NONE,
        #expand=True,
        alignment=ft.alignment.center,
        gradient=ft.LinearGradient(
            rotation=math.pi / 3,
            colors=["#86e3ce","#d0e6a5","#ffde95","#fa897b","#ccabd8"],
            ),

        #bgcolor="#ffffff",
        border_radius=10,
        content=ft.Column(
            width = 320,
            controls=[
                #Container(
                    #content=Image(
                        #src=signinbg.jpg"
                    #)
                #),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=170,right=10,top=10),
                    content=ft.TextButton(
                        "Create Account",
                        style=ft.ButtonStyle(
                            color="#7D7C7C"
                        )
                    )
                ),
                ft.Container(
                    width =300,
                    margin=ft.margin.only(left=90,right=10,top=20),
                    content=ft.Text(
                        "WELCOME",
                        #text_align="center",
                        size=24,
                        color="#000000",
                        weight="w700"
                    )
                ),
                ft.Container(
                    width =300,
                    margin=ft.margin.only(left=100,right=10,top=5),
                    content=ft.Text(
                        "LifeHack!",
                        size=24,
                        color="#000000",
                        weight="w700"
                    )
                ),
                ft.Container(
                 width =300,
                    margin=ft.margin.only(left=65,right=10,top=20),
                    content=ft.Text(
                        "Hack your life by lifeHack",
                        #text_align="center",
                        size=15,
                        color="#000000"   
                    )
                ),
                ft.Container(
                    theme=ft.Theme(color_scheme_seed=ft.colors.BLACK),
                    theme_mode=ft.ThemeMode.LIGHT,
                    width=300,  
                    margin=ft.margin.only(left=10,right=10,top=20), 
                    content=ft.Column(
                        controls=[
                            ft.TextField(
                                
                                label="User Name or E-mail",
                                
                                text_style = ft.TextStyle(
                                    size=14,
                                    color="#000000",
                                ),
                                border_radius=40,
                                border_color=ft.colors.BLACK,
                                focused_border_color=ft.colors.ORANGE_700,
                            )
                        ]
                    )
                ),
                ft.Container(
                    theme=ft.Theme(color_scheme_seed=ft.colors.BLACK),
                    theme_mode=ft.ThemeMode.LIGHT,
                    width =300,  
                    margin=ft.margin.only(left=10,right=10,top=5), 
                    content=ft.Column(
                        controls=[
                            ft.TextField(
                                label="Password",
                                text_style = ft.TextStyle(
                                    size=14,
                                    color="#000000",
                                ),
                                password=True,
                                can_reveal_password=True,
                                
                                border_radius=40,
                                border_color=ft.colors.BLACK,
                                focused_border_color=ft.colors.ORANGE_700,
                            )
                        ]
                    )
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=150,right=10,top=5), 
                    content=ft.TextButton(
                        "Forgot Password?" ,
                        style=ft.ButtonStyle(

                        )
                    )
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=20,right=10,top=5,bottom=20), 
                    content=ft.TextButton(
                        "Login" ,
                        width=300,
                        height=50,
                        style=ft.ButtonStyle(
                            color="#ffffff",
                            bgcolor=ft.colors.ORANGE_700,
                            shape={}
                        )
                    )
                )
            ]
        ),
    )
)

    page.add(login)

ft.app(target=main)