from flet import *
from homepage import Home
#from todo import main
from tobuy_new import ToBuyMain
from calculator_new2 import Calculator
from signup import SignupMain
from login import LoginMain
from forgetpass import ForgetMain

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
        '/tobuy': View(
            route='/tobuy/',
            controls=[
                ToBuyMain(page)
            ]
        ),
        '/calculator': View(
            route='/calculator/',
            controls=[
                Calculator(page)
            ]
        ),
        '/signup': View(
            route='/signup/',
            controls=[
                SignupMain(page)
            ]
        ),
        '/login': View(
            route='/login/',
            controls=[
                LoginMain(page)
            ]
        ),
        '/forgetpass': View(
            route='/forgetpass/',
            controls=[
                ForgetMain(page)
            ]
        ),
        
    }