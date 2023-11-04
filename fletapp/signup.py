import flet as ft
from flet import *
# from flet_route import Params,Basket
import math
import pyrebase
from fastapi import FastAPI

fireconfig = {
    "apiKey": "AIzaSyDqZPzZ_U_DqJkcQFXpUeFGtvFLCo9AFEg",
    "authDomain": "project334-cdc82.firebaseapp.com",
    "databaseURL": "https://project334-cdc82-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "project334-cdc82",
    "storageBucket": "project334-cdc82.appspot.com",
    "messagingSenderId": "829383491724",
    "appId": "1:829383491724:web:de3ba959db852dfb7bfba9",
    "measurementId": "G-0DJK0YKSJ5"
    }

firebase = pyrebase.initialize_app(fireconfig)
auth = firebase.auth()

def main(page : Page):
    page.title="Register"
    page.bgcolor="black"
    page.bgcolor ="#86e3ce"
    page.window_width = 350
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    dlg = ft.AlertDialog(
        #Container(
            #margin=margin.only(left=70,right=10,top=20),
            content=ft.Text("Please enter the same password",
                      size=16,
                      color="#C70039",
                      text_align="center",
                      ), on_dismiss=lambda e: print("Dialog dismissed!")
        #)
    )
    success_dlg = ft.AlertDialog(
        title=ft.Text("Sign up sucessfully",
                      
                      size=16,
                      color="#539165",
                      text_align="center",
                      ), on_dismiss=lambda e: print("Success Dialog dismissed!")
    )
    wrong_dlg = ft.AlertDialog(
        title=ft.Text("Wrong username or password",
                      
                      size=16,
                      color="#C70039",
                      text_align="center",
                      ), on_dismiss=lambda e: print("Wrong Dialog dismissed!")
    )
    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
    def open_success_dlg(e):
        page.dialog = success_dlg
        success_dlg.open = True
        page.update()
    def open_wrong_dlg(e):
        page.dialog = wrong_dlg
        wrong_dlg.open = True
        page.update()    
#####################################################################################
    def create(e):
        if password_1.value == password_2.value : #and password_1 != auth.get_account_info(Email.value):
            try:
                auth.create_user_with_email_and_password(
                    Email.value, password_1.value)
                open_success_dlg(e)
            except:
                page.add(ft.SafeArea(ft.Container(ft.Text("Wrong username or password"))))
                page.update()
                open_wrong_dlg(e)
        #elif 
        else:
            open_dlg(e)
    page.update()
####################################################################################

    Email = TextField(
        label="Email",
        border_radius=40,
        border_color=colors.BLACK,
        focused_border_color=colors.ORANGE_700,
        text_style=TextStyle(
        color="#000000",
        )
    ) 

    password_1 = TextField(
        label="Password",
        border_radius=40,
        border_color=colors.BLACK,
        focused_border_color=colors.ORANGE_700,
        password=True,
        can_reveal_password=True,
        text_style=TextStyle(
        color="#000000",
        )
    )

    password_2 = TextField(
        label="Confirm Password",
        border_radius=40,
        border_color=colors.BLACK,
        focused_border_color=colors.ORANGE_700,
        password=True,
        can_reveal_password=True,
        text_style=TextStyle(
            color="#000000",
        )
    )

    signup = Container(

        alignment=alignment.center,
        gradient=LinearGradient(
            rotation=math.pi / 3,
            colors=["#86e3ce","#d0e6a5","#ffde95","#fa897b","#ccabd8"],
            ),
        width=600,
        height=800,
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
                        controls=[Email]
                    )
                ),
                Container(  #for password 
                    width=300,
                    margin=margin.only(left=10,right=10,top=10),
                    content=Column(
                        controls=[password_1]
                    )
                ),
                Container(  #for confirm password 
                    width=300,
                    margin=margin.only(left=10,right=10,top=10),
                    content=Column(
                        controls=[password_2]
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
                        ),
                        on_click=create,
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