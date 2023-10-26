import flet as ft
from flet import *
# from flet_route import Params,Basket
import math

def main(page : Page):
    page.title="Login and Register"
    page.bgcolor="black"
    page.window_width = 350


    signup = Container(

        alignment=alignment.center,
        gradient=LinearGradient(
            rotation=math.pi / 3,
            colors=["#86e3ce","#d0e6a5","#ffde95","#fa897b","#ccabd8"],
            ),
        width=320,
        height=750,
        bgcolor="#ffffff",
        border_radius=10,
        content=Column(
            width=320,
            controls=[
                Container(
                    width=48,
                    height = 40,
                    border_radius = 10,
                    margin=margin.only(left=15,top=10),
                    content=IconButton(
                        icon_color ="#000000",
                        icon=icons.ARROW_BACK_IOS_NEW_SHARP,
                        style=ButtonStyle(
                            side= {
                                MaterialState.DEFAULT : border.BorderSide(1, colors.GREY)
                            },
                    
                        )
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=70,right=10,top=20),
                    content=Text(
                        "Create Account",
                        size=24,
                        weight="W700",
                        color="#000000"

                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=15,right=10,top=20),
                    alignment=alignment.center,
                    content=Text(
                        "Please enter your information below in order to create a new account",
                        text_align="center",
                        size=14,
                        color="#000000",

                    )
                ),
                Container( #for user
                    width=300,
                    margin=margin.only(left=10,right=10,top=20),
                    content=Column(
                        controls=[
                            TextField(
                                label="Username",
                                border_radius=40,
                                border_color=colors.BLACK,
                                focused_border_color=colors.ORANGE_700,
                                text_style=TextStyle(
                                    color="#000000",
                                )
                            )
                        ]
                    )
                ),
                Container(  #for email
                    width=300,
                    margin=margin.only(left=10,right=10,top=10),
                    content=Column(
                        controls=[
                            TextField(
                                label="E-mail",
                                border_radius=40,
                                border_color=colors.BLACK,
                                focused_border_color=colors.ORANGE_700,
                                text_style=TextStyle(
                                    color="#000000",
                                )
                            )
                        ]
                    )
                ),
                Container(  #for password 
                    width=300,
                    margin=margin.only(left=10,right=10,top=10),
                    content=Column(
                        controls=[
                            TextField(
                                label="Password",
                                border_radius=40,
                                border_color=colors.BLACK,
                                focused_border_color=colors.ORANGE_700,
                                text_style=TextStyle(
                                    color="#000000",
                                )
                            )
                        ]
                    )
                ),
                Container(  #for confirm password 
                    width=300,
                    margin=margin.only(left=10,right=10,top=10),
                    content=Column(
                        controls=[
                            TextField(
                                label="Confirm Password",
                                border_radius=40,
                                border_color=colors.BLACK,
                                focused_border_color=colors.ORANGE_700,
                                text_style=TextStyle(
                                    color="#000000",
                                )
                            )
                        ]
                    )
                ),
                Container(
                    width=300,
                    margin=ft.margin.only(left=10,right=10,top=15), 
                    content=ft.TextButton(
                        "Sign Up" ,
                        width=300,
                        height=50,
                        style=ft.ButtonStyle(
                            color="#ffffff",
                            bgcolor=ft.colors.ORANGE_700,
                            shape={}
                        )
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=10,right=10,top=5),
                    alignment=alignment.center,
                    content=TextButton(
                        "Already have an account? Login",
                    
                        )

                    
                ),

                
            ]

        ),
    )
    

    
    page.add(signup)

app(target=main)