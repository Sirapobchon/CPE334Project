import flet
from flet import *
import math

def main(page : Page):
    page.title="Login and Register"
    page.bgcolor="black"

    login = Container(
        width=320,
        height=750,
        #image_src="signinbg.jpg",
        
        #image_fit=ImageFit.NONE,
        #expand=True,
        gradient=LinearGradient(
            rotation=math.pi / 3,
            colors=["#86e3ce","#d0e6a5","#ffde95","#fa897b","#ccabd8"],
            ),

        #bgcolor="#ffffff",
        border_radius=10,
        content=Column(
            width = 320,
            controls=[
                #Container(
                    #content=Image(
                        #src=signinbg.jpg"
                    #)
                #),
                Container(
                    width=300,
                    margin=margin.only(left=170,right=10,top=10),
                    content=TextButton(
                        "Create Account",
                        style=ButtonStyle(
                            color="#7D7C7C"
                        )
                    )
                ),
                Container(
                    width =300,
                    margin=margin.only(left=90,right=10,top=20),
                    content=Text(
                        "WELCOME",
                        #text_align="center",
                        size=24,
                        color="#000000",
                        weight="w700"
                    )
                ),
                Container(
                    width =300,
                    margin=margin.only(left=100,right=10,top=5),
                    content=Text(
                        "LifeHack!",
                        size=24,
                        color="#000000",
                        weight="w700"
                    )
                ),
                Container(
                 width =300,
                    margin=margin.only(left=65,right=10,top=20),
                    content=Text(
                        "Hack your life by lifeHack",
                        #text_align="center",
                        size=15,
                        color="#000000"   
                    )
                ),
                Container(
                  width =300,  
                  margin=margin.only(left=10,right=10,top=20), 
                  content=Column(
                      controls=[
                            TextField(
                                label="User Name or E-mail",
                                text_style = TextStyle(
                                    size=14,
                                    color="#000000",
                                ),
                                border_radius=40,
                                border_color=colors.BLACK,
                                focused_border_color=colors.ORANGE_700,
                            )
                        ]
                    )
                ),
                Container(
                  width =300,  
                  margin=margin.only(left=10,right=10,top=5), 
                  content=Column(
                      controls=[
                            TextField(
                                label="Password",
                                text_style = TextStyle(
                                    size=14,
                                    color="#000000",
                                ),
                                password=True,
                                can_reveal_password=True,
                                
                                border_radius=40,
                                border_color=colors.BLACK,
                                focused_border_color=colors.ORANGE_700,
                            )
                        ]
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=150,right=10,top=5), 
                    content=TextButton(
                        "Forgot Password?" ,
                        style=ButtonStyle(

                        )
                    )
                ),
                Container(
                    width=300,
                    margin=margin.only(left=20,right=10,top=5), 
                    content=TextButton(
                        "Login" ,
                        width=300,
                        height=50,
                        style=ButtonStyle(
                            color="#ffffff",
                            bgcolor=colors.ORANGE_700,
                            shape={}

                        )

                    )
                )
            ]



        

        ),

    )
    signup = Container(
        width=320,
        height=750,
        bgcolor="#ffffff",
        border_radius=10,
        content=Column(
        

        ),
    )


    body = Container(
        height=800,
        content=Row(
            controls=[
                login,
                signup,

            ]
        ),
        #padding=padding.only(left=300)

    )
    page.add(body)

app(target=main)