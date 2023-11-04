import flet as ft
import math

#firebase cloud
from firebase_admin import credentials
cred = credentials.Certificate("./firebase/serviceAccountKey.json")

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

import pyrebase
firebase = pyrebase.initialize_app(fireconfig)
auth = firebase.auth()
#db = firestore.client()

def main(page : ft.Page):
    #page.theme_mode = ft.ThemeMode.LIGHT
    page.title="Login"
    page.bgcolor ="#86e3ce"
    page.padding = 0
    page.window_width = 350
    
    success_dlg = ft.AlertDialog(
        title=ft.Text("Sign in sucessfully",
                      
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
    def open_success_dlg(e):
        page.dialog = success_dlg
        success_dlg.open = True
        page.update()
    def open_wrong_dlg(e):
        page.dialog = wrong_dlg
        wrong_dlg.open = True
        page.update()    
#############################################################################
    def post(e):
        try:
            auth.sign_in_with_email_and_password(
                Email.value, password.value)
            open_success_dlg(e)
        except:
            page.add(ft.SafeArea(ft.Container(ft.Text("Wrong username or password"))))
            page.update()
            open_wrong_dlg(e)
    page.update()
##############################################################################
    
    Email = ft.TextField(
        label="E-mail",
        text_style=ft.TextStyle(
            size=14,
            color="#000000",
        ),
        border_radius=40,
        border_color=ft.colors.BLACK,
        focused_border_color=ft.colors.ORANGE_700,
    )

    password = ft.TextField(
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

    def forgetpass(e):
        print("Forget Password")
    page.update()

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
        height=800,
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
                    content = ft.Column(
                        controls=[Email],
                    ),
                    
                ),
                ft.Container(
                    theme=ft.Theme(color_scheme_seed=ft.colors.BLACK),
                    theme_mode=ft.ThemeMode.LIGHT,
                    width =300,  
                    margin=ft.margin.only(left=10,right=10,top=5), 
                    content=ft.Column(
                        controls=[password],
                    )
                ),
                ft.Container(
                    width=300,
                    margin=ft.margin.only(left=150,right=10,top=5), 
                    content=ft.TextButton(
                        "Forgot Password?" ,
                        style=ft.ButtonStyle(

                        ),
                        on_click=forgetpass,
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
                        ),
                        on_click=post,
                    )
                )
            ]
        ),
    )
)

    page.add(login)

ft.app(target=main)