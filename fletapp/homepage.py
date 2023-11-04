# importing the library
from flet import *
import flet as ft
import datetime 
import threading as th
import time

class TimeLine(ft.UserControl):
  def __init__(self):
    super().__init__()
    self.now = datetime.datetime.now()
    self.date = self.now.strftime("%A, %B, %d")
    self.time = self.now.strftime("%H:%M")

    self.field_date = ft.Text(
      self.date,
      text_align= TextAlign.CENTER,
      color = 'Black',
      size = 24,
      weight = 'bold',
    )

    
    self.field_time = ft.Text(
      self.time,
      color = 'Black',
      weight = '300',
      size = 30,
      # weight = 'bold',
    )
  
  def update_datetime(self):
    while True:
      time.sleep(1)
      self.now = datetime.datetime.now()
      self.date = self.now.strftime("%A, %B %d")
      self.time = self.now.strftime("%H:%M:%S")
      self.field_date.value = self.date
      self.field_time.value = self.time
      self.field_date.update()
      self.field_time.update()

  def did_mount(self):
    th.Thread(target = self.update_datetime).start()
    
  def build(self):
    return ft.Container(
      ft.Column([
        ft.Container(
          self.field_date,
          alignment = ft.alignment.center
        ),
      ft.Container(
        self.field_time,
          alignment = ft.alignment.center,
          margin = ft.margin.only(top = 10),
        )
      ],spacing = 0),
      width = 300,
      height = 100,
      alignment = ft.alignment.center
      )
  

class home(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page


  def build(self):
    return ft.Container(
  ft.Stack([
    ft.Container(
      alignment=ft.alignment.center,
      width=395,
      height=640,
      top=70,
      
      bgcolor='#FFFBEB',
      border_radius=ft.border_radius.only(30, 30,30,30)
    ),

    ft.Container(
      margin = ft.margin.only(left=10),
      content = ft.Text ("Hello!", color='#FFFFFF', size = 30, weight = "bold",),
    ),

    ft.Container(
      margin = ft.margin.only(left=10),
      top=40,
      content = ft.Text ("have a nice day", color='#FFFFFF', size = 15,)
    ),

    ft.Container(
      
      content = TimeLine(),
      alignment=ft.alignment.center,
      top=90,
      width=345,
      left=25,
      height=115,
      gradient = ft.LinearGradient(
        begin = ft.alignment.top_left,
        end = ft.alignment.bottom_right,
        colors = ['#86E3CE','#D6E6A5','#FFDD94','#FA897B','#CCABD8']
      ),
      blur=ft.Blur(10, 12, ft.BlurTileMode.REPEATED),
      padding=ft.padding.only(0, 15, 0, 15),
      border_radius=10,
      
    ),

    ft.Container(
      width = 162,
      height = 200, 
      top = 220,
      left = 25,
      alignment = ft.alignment.center,
      padding = ft.padding.all(10),
      gradient = ft.LinearGradient(
        begin = ft.alignment.top_left,
        end = ft.alignment.bottom_right,
        colors = ['#86E3CE','#D6E6A5','#FFDD94','#FA897B','#CCABD8']
      ), 
      border_radius= ft.border_radius.all(30),
      content = ft.Column([

        ft.Column([
          ft.Row([
            ft.Image(src = "assets/check-box_icon-icons.com_72816.png", 
                 width = 70, height = 90),
          ], alignment=ft.MainAxisAlignment.CENTER),

          ft.Row([
            ft.Text(value = "To Do List",
                color = "black",
                size = 15,
                weight = 'bold',
                style = ft.ButtonStyle(color = "white",
                                       padding = 10)
            ),
          ], alignment=ft.MainAxisAlignment.CENTER),
        ], spacing = 1),
        
        ft.Column([
          ft.Text(value = "'To Do List' is like a time management tool with a lot more fun built in.",
                color = "#424949",
                size = 11,
                style = ft.ButtonStyle(color = "white",
                                       padding = 10)
                ),
        ]),       
    ], spacing = 7), 
    ),
    
    ft.Container(
      width = 162,
      height = 200, 
      top = 220,
      left = 208,
      alignment = ft.alignment.center,
      padding = ft.padding.all(10),
      gradient = ft.LinearGradient(
        begin = ft.alignment.top_left,
        end = ft.alignment.bottom_right,
        colors = ['#86E3CE','#D6E6A5','#FFDD94','#FA897B','#CCABD8']
      ), 
      border_radius= ft.border_radius.all(30),
      content = ft.Column([

        ft.Column([
          ft.Row([
            ft.Image(
                 src = "assets/2849824-basket-buy-market-multimedia-shop-shopping-store_107977.png", 
                 width = 90, height = 90),
                 ], alignment=ft.MainAxisAlignment.CENTER),
        
          ft.Row([
            ft.Text(value = "Shopping List",
                color = "black",
                size = 15,
                weight = 'bold',
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ], spacing = 1),
        
        ft.Text(value = "A shopping list: the only list that makes your wallet shed a tear",
                color = "#424949",
                size = 11,
                style = ft.ButtonStyle(color = "white",
                                       padding = 10)
                ),
                
    ], spacing = 7), 
    ),

    ft.Container(
      width = 162,
      height = 200, 
      top = 430,
      left = 25,
      alignment = ft.alignment.center,
      padding = ft.padding.all(10),
      gradient = ft.LinearGradient(
        begin = ft.alignment.top_left,
        end = ft.alignment.bottom_right,
        colors = ['#86E3CE','#D6E6A5','#FFDD94','#FA897B','#CCABD8']
      ), 
      border_radius= ft.border_radius.all(30),
      content = ft.Column([
        ft.Column([
          ft.Row([
            ft.Image(
                 src = "assets/seo-social-web-network-internet_92_icon-icons.com_61528.png", 
                 width = 90, height = 90),
                 ], alignment=ft.MainAxisAlignment.CENTER),

          ft.Row([
            ft.Text(value = "Calculator",
                color = "black",
                size = 15,
                weight = 'bold',
                style = ft.ButtonStyle(color = "white",
                                       padding = 10)
                ),
          ], alignment=ft.MainAxisAlignment.CENTER),
        ], spacing = 1),

        ft.Text(value = "Your personal mathematician",
                color = "#424949",
                size = 11,
                style = ft.ButtonStyle(color = "white",
                                      padding = 10)
                ),
    ], spacing = 7), 
    ),

    ft.Container(
      width = 162,
      height = 200, 
      top = 430,
      left = 208,
      alignment = ft.alignment.center,
      padding = ft.padding.all(10),
      gradient = ft.LinearGradient(
        begin = ft.alignment.top_left,
        end = ft.alignment.bottom_right,
        colors = ['#86E3CE','#D6E6A5','#FFDD94','#FA897B','#CCABD8']
      ), 
      border_radius= ft.border_radius.all(30),
      content = ft.Column([
         ft.Column([
           ft.Row([
            ft.Image( 
                src = "assets/annual_calender_day_schedule_date_time_calendar_icon_256444.png", 
                width = 70, height = 90),
                 ], alignment=ft.MainAxisAlignment.CENTER),
        
        ft.Row([
          ft.Text(value = "Calendar",
                color = "black",
                size = 15,
                weight = 'bold',
                style = ft.ButtonStyle(color = "white",
                                       padding = 10)
                ),
        ], alignment=ft.MainAxisAlignment.CENTER),
        ], spacing = 1),
       

        ft.Text(value = "Your calendar is your compass; let it lead you to your dreams.",
                color = "#424949",
                size = 11,
                style = ft.ButtonStyle(color = "white",
                                       padding = 10)
                ),
    ], spacing = 7), 
    ),
  ]
  ),
  gradient = ft.LinearGradient(
    begin = ft.alignment.top_center,
    end = ft.alignment.bottom_center,
    colors = ['#86E3CE','#D6E6A5','#FFDD94','#FA897B','#CCABD8']
  ),
  width = 800,
  height = 800, 
)

