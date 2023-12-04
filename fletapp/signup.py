import flet as ft
import math
import pyrebase
import json

fireconfig = json.load(open('fletapp/firebase/firebaseConfig.json', 'r'))
firebase = pyrebase.initialize_app(fireconfig)
auth = firebase.auth()

# Variable 
dlg = ft.AlertDialog(
    title=ft.Text("Please enter the same password",
        size=16,
        color="#C70039",
        text_align="center",
    ), on_dismiss=lambda self: (
        print("Dialog dismissed!"),
        setattr(self.page, "theme_mode", ft.ThemeMode.SYSTEM),
        self.page.update()
    )
)
password_len_dlg= ft.AlertDialog(
    title=ft.Text("Please enter password at least 6 characters",
        size=16,
        color="#C70039",
        text_align="center",
    ), on_dismiss=lambda self: (
        print("Dialog dismissed!"),
        setattr(self.page, "theme_mode", ft.ThemeMode.SYSTEM),
        self.page.update()
    )
)
success_dlg = ft.AlertDialog(
    title=ft.Text("Sign up sucessfully",
        size=16,
        color="#539165",
        text_align="center",
    ), on_dismiss=lambda self: (
        print("Success Dialog dismissed!"),
        setattr(self.page, "theme_mode", ft.ThemeMode.SYSTEM),
        self.page.update()
    )
)
wrong_dlg = ft.AlertDialog(
    
    title=ft.Text("User already exists",
        size=16,
        color="#C70039",
        text_align="center",
    ), on_dismiss=lambda self: (
        print("Wrong Dialog dismissed!"),
	    setattr(self.page, "theme_mode", ft.ThemeMode.SYSTEM),
        self.page.update()
    )
)
empty_email_dlg = ft.AlertDialog(
    
    title=ft.Text("Please fill all of your information",
        size=16,
        color="#C70039",
        text_align="center",
    ), on_dismiss=lambda self: (
        print("Empty email dismissed!"),
	    setattr(self.page, "theme_mode", ft.ThemeMode.SYSTEM),
        self.page.update()
    )
)
fill_everything_dlg=ft.AlertDialog(
    
    title=ft.Text("Please Input Email",
        size=16,
        color="#C70039",
        text_align="center",
    ), on_dismiss=lambda self: (
        print("Empty email dismissed!"),
	    setattr(self.page, "theme_mode", ft.ThemeMode.SYSTEM),
        self.page.update()
    )
) 




def open_dlg(self):
    self.page.theme_mode=ft.ThemeMode.LIGHT,
    self.page.dialog = dlg
    dlg.open = True
    self.page.update()
def open_success_dlg(self):
    self.page.theme_mode=ft.ThemeMode.LIGHT,
    self.page.dialog = success_dlg
    success_dlg.open = True
    self.page.update()
def open_wrong_dlg(self):
    self.page.theme_mode=ft.ThemeMode.LIGHT,
    self.page.dialog = wrong_dlg
    wrong_dlg.open = True
    self.page.update()    
def open_password_len_dlg(self):
    self.page.theme_mode=ft.ThemeMode.LIGHT,
    self.page.dialog = password_len_dlg
    password_len_dlg.open = True
    self.page.update()   
def open_empty_email_dlg(self):
    self.page.theme_mode=ft.ThemeMode.LIGHT,
    self.page.dialog = empty_email_dlg
    empty_email_dlg.open = True
    self.page.update()   
def open_fill_everything_dlg(self):
    self.page.theme_mode=ft.ThemeMode.LIGHT,
    self.page.dialog = fill_everything_dlg
    fill_everything_dlg.open = True
    self.page.update()   


def create(self):
    if self.Email.value =="" :       
        open_empty_email_dlg(self)
    elif len(self.password_1.value ) <6:
        #print(len(self.password_1.value))
        open_password_len_dlg(self)

    elif self.password_1.value == self.password_2.value: #and password_1 != auth.get_account_info(Email.value):
        try:
            auth.create_user_with_email_and_password(
                self.Email.value, self.password_1.value)
            open_success_dlg(self)
        except:
            #self.page.add(ft.SafeArea(ft.Container(ft.Text("Wrong username or password"))))
            #self.page.update()
            open_wrong_dlg(self)
    elif self.Email.value =="" : 
            if self.password_1.value and self.password_2.value  =="":
                open_fill_everything_dlg(self)
            else:
                open_empty_email_dlg(self)
    #elif self.Email.value and self.password_1.value and self.password_2.value =="" : 
            #open_
    else:
        open_dlg(self)
        self.update()


class SignupMain(ft.UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.Email = ft.TextField(
            label="Email",
            border_radius=40,
            border_color=ft.colors.BLACK,
            focused_border_color=ft.colors.ORANGE_700,
            text_style=ft.TextStyle(
                color="#000000",
            )
        )

        self.password_1 = ft.TextField(
            label="Password",
            border_radius=40,
            border_color=ft.colors.BLACK,
            focused_border_color=ft.colors.ORANGE_700,
            password=True,
            can_reveal_password=True,
            text_style=ft.TextStyle(
            color="#000000",
            )
        ) 

        self.password_2 = ft.TextField(
            label="Confirm Password",
            border_radius=40,
            border_color=ft.colors.BLACK,
            focused_border_color=ft.colors.ORANGE_700,
            password=True,
            can_reveal_password=True,
            text_style=ft.TextStyle(
            color="#000000",
            )
        )
    
    def build(self):

        return ft.SafeArea(
        ft.Container(
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                rotation=math.pi / 3,
                colors=["#86e3ce","#d0e6a5","#ffde95","#fa897b","#ccabd8"],
                ),
            width=600,
            height=800,
            theme=ft.Theme(color_scheme_seed=ft.colors.BLACK),
		    theme_mode=ft.ThemeMode.LIGHT,
            bgcolor="#ffffff",
            border_radius=10,
            content=ft.Column(
                width=320,
                controls=[
                    ft.Container(
                        width=48,
                        height = 40,
                        border_radius = 10,
                        margin=ft.margin.only(top=20),
                        content=ft.IconButton(
                            icon_color ="#000000",
                            icon=ft.icons.ARROW_BACK_IOS_NEW_SHARP,
                            on_click=lambda e: self.page.go('/login'),  
                            style=ft.ButtonStyle(
                                side= {
                                    ft.MaterialState.DEFAULT : ft.border.BorderSide(1, ft.colors.GREY)
                                },
                            )
                        )
                    ),
                    ft.Container(
                        width=300,
                        margin=ft.margin.only(left=70,right=10,top=20),
                        content=ft.Text(
                            "Create Account",
                            size=24,
                            weight="W700",
                            color="#000000"

                        )
                    ),
                    ft.Container(
                        width=300,
                        margin=ft.margin.only(left=15,right=10,top=20),
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            "Please enter your information below in order to create a new account",
                            text_align="center",
                            size=14,
                            color="#000000",

                        )
                    ),
                    ft.Container( #for user
                        width=300,
                        margin=ft.margin.only(left=10,right=10,top=20),
                        content=ft.Column(
                            controls=[
                                ft.TextField(
                                    label="Username",
                                    border_radius=40,
                                    border_color=ft.colors.BLACK,
                                    focused_border_color=ft.colors.ORANGE_700,
                                    text_style=ft.TextStyle(
                                    color="#000000",
                                    )
                                )
                            ]
                        )
                    ),
                    ft.Container(  #for email
                        width=300,
                        margin=ft.margin.only(left=10,right=10,top=10),
                        content=ft.Column(
                            controls=[self.Email]
                        )
                    ),
                    ft.Container(  #for password 
                        width=300,
                        margin=ft.margin.only(left=10,right=10,top=10),
                        content=ft.Column(
                            controls=[self.password_1]
                        )
                    ),
                    ft.Container(  #for confirm password 
                        width=300,
                        margin=ft.margin.only(left=10,right=10,top=10),
                        content=ft.Column(
                            controls=[self.password_2]
                        )
                    ),
                    ft.Container(
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
                            on_click=lambda e: create(self),
                        )
                    ),
                    ft.Container(
                        width=300,
                        margin=ft.margin.only(left=10,right=10,top=5),
                        alignment=ft.alignment.center,
                        content=ft.TextButton(
                            "Already have an account? Login",
                            on_click=lambda e: self.page.go('/login'),  
                            )          
                    ),

                
                ]

            ),
        ),
    )                         
    

    