from flet import *
from homepage import Home
#from todo import main
#import tobuy
#import signup
from login import LoginMain

def views(page):
    return {
        '/': View(
            route='/',
            controls=[
                Home(page)
            ]
        ),
        
        '/todo': View(
            route='/todo/',
            controls=[
                #main(page)
            ]
        ),
        '/thirdpage': View(
            route='/thirdpage/',
            controls=[
                #tobuy.tobuy(page)
            ]
        ),
        '/signup': View(
            route='/signup/',
            controls=[
                #signup.signup(page)
            ]
        ),
        '/login': View(
            route='/login/',
            controls=[
                LoginMain(page)
            ]
        )
    }