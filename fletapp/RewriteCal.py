import flet
from flet import *
import flet as ft
from datetime import datetime
import calendar
import datetime


#calendar control
class SetCalendar(UserControl):
    def __init__(self, start_year=datetime.date.today().year):
        self.current_year = start_year #current year

        self.m1 = datetime.date.today().month #current month
        self.m2 = self.m1 + 1 #second month for calendar module

        self.click_count: list = [] #for tracking clicks
        self.long_press_count: list =[] #same as above

        self.current_color = "blue" #highlight color

        self.selected_date = any #the selected data from the calendar

        self.calendar_grid = Column(
            wrap=True,
            alignment = MainAxisAlignment.CENTER,
            horizontal_alignment = CrossAxisAlignment.CENTER,
        )
        super().__init__()

    #paginate months
    def _change_month(self, delta):
        #keeps m1 between 1 and 12, and m2 between 2 and 13
        self.m1 = min(max(1, self.m1 + delta), 12)
        self.m2 = min(max(2, self.m2 + delta), 13)

        #new calendar variable
        new_calendar = self.create_month_calendar(self.current_year)
        new_calendar_grid = new_calendar
        self.update() 

    #adding more functions to the calendar 
    #highlight clicked container
    def one_click_date(self, e):
        self.selected_date = e.control.data
        e.control.bgcolor = "red"
        e.control.update()
        self.update()

    def long_click_date(self, e):
        #save the 2 clicks to a list
        self.long_press_count.append(e.control.data)
        #check if there is 2 clicks
        if len(self.long_press_count) == 2:
            #set two dates by unpacking the list
            date1, date2 = self.long_press_count  
            #get the absolute distance between them
            delta=abs(date2 - date1)
            #check to see if it's past selection or future
            if date1 < date2:
                dates = [
                    date1 + datetime.timedelta(days=x) for x in range (delta.days + 1)
                ]
            else:
                dates = [
                    date2 + datetime.timedelta(days=x) for x in range (delta.days + 1)
                    ]
            #loop over calendar matrix and color the boxes
            for _ in self.calendar_grid.controls[:]:
                for __ in __.controls[:]:
                    if isinstance(__, Row):
                        for box in __.controls[:]:
                            #check to see if dates list above match the date created in container
                            if box.data in dates:
                                box.bgcolor = "red"
                                box.update()

            self.long_press_count = []
        else:
            pass
                
    #logic for the calendar
    def create_month_calendar(self, year):
        self.current_year = year #for current year
        self.calendar_grid.controls: list = []#clear calendar grid

        for month in range(self.m1, self.m2):
            #gets month name + year
            month_label = Text(
                f"{calendar.month_name[month]} {self.current_year}",
                size = 14,
                weight = "bold",
            )

            #month matrix
            month_matrix = calendar.monthcalendar(self.current_year, month)
            month_grid = Column(alignment=MainAxisAlignment.CENTER)
            month_grid.controls.append(
                Row(
                    alignment = MainAxisAlignment.START,
                    controls = [month_label],
                )
            )

            #weekday labels
            weekday_labels = [
                Container(
                    width=28,
                    height=28,
                    alignment = alignment.center,
                    content = Text(
                        weekday,
                        size=12,
                        color="Black",
                    )
                )
                for weekday in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            ]

            #list of weekday in rows
            weekday_row = Row(controls=weekday_labels)
            month_grid.controls.append(weekday_row)

            #days
            for week in month_matrix:
                week_container = Row()
                for day in week:
                    if day == 0: #day in grid
                        day_container = Container(
                            width=28,
                            height=28,
                        )
                    else:
                        day_container = Container(
                            width=28,
                            height=28,
                            border=border.all(0.5,"gray"),
                            alignment = alignment.center,

                            data=datetime.date(
                                year=self.current_year,
                                month = month,
                                day = day,
                            ),
                            on_click = lambda e: self.one_click_date(e),
                            #on_click = lambda e: _create_entry(e),
                            animate = 400,
                        )
                    day_label = Text(str(day), size=12)

                    #second check
                    if day == 0:
                        day_label = None
                    if (
                        day == datetime.date.today().day
                        and month == datetime.date.today().month
                        and self.current_year == datetime.date.today().year
                    ):
                        day_container.bgcolor = "teal"
                    day_container.content = day_label
                    week_container.controls.append(day_container)
                month_grid.controls.append(week_container)

        self.calendar_grid.controls.append(month_grid)

        return self.calendar_grid
    
    def build(self):
        return self.create_month_calendar(self.current_year)
    

   
    #def _create_entry(e):
        #_content_column.controls.append(
            #Row(
                #controls=(
                    #border_radius==8,
                    #padding==2,
                    #expand == True,
                    #gradient == LinearGradient(
                        #begin = alignment.center_left,
                    #    end=alignment.center_right,
                    #    colors=["Black", "White"],
                    #),
                    #content=Text(
                    #    f"You have a task on\n (e.control.data)",
                    #    size=10
                    #)
                #)
            #)
        #)
        
#        _content_column.update()
    
#        _content_column = Column(
#            scroll="auto",
#            expand=True,
#            alignment="start",
#            controls=[
#                Container(
#                    padding=15,
#                    content=Text(
#                        "To-Do List",
#                        color="White",
#                        weight="bold",
#                        size=13,
#                    )
#                )
#            ]
#        ) 


#upper level UI
class DateSetUp(UserControl):
    def __init__(self, cal_grid):
        self.cal_grid = cal_grid #calendar instance

        

        #create buttons here, None
        self.prev_btn = BTNPagination("Prev.", lambda e: cal_grid._change_month(-1))
        self.next_btn = BTNPagination("Next.", lambda e: cal_grid._change_month(1))

        self.today = Text (
            datetime.date.today().strftime("%B %d, %Y"),
            width = 260,
            size = 13,
            color = "white",
            weight = "w400"
        )

        #hold pagination button
        self.btn_container = Row(
            alignment = MainAxisAlignment.CENTER,
            controls=[
                #buttons go in here
                self.prev_btn,
                self.next_btn
            ]
        )

       #store the calendar
        self.calendar = Container(
            width=320,
            height=450,
            bgcolor="blue",
            border_radius=8,
            animate=300,
            alignment=alignment.bottom_center,
            content=Column(
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    #actual calendar instance plus buttons
                    Divider(height=60, color='transparent'),
                    self.cal_grid,
                    Divider(height=10, color='transparent'),
                    self.btn_container,
                ],
            ),
        )

        super().__init__()

    #expands the stack to see calendar
    def _get_calendar(self, e:None):
        if self.calendar.height ==45:
            self.calendar.height = 450
            self.calendar.update()
        else:
            self.calendar.height = 45
            self.calendar.update()

    def build(self):
        return Stack(
            #stack to stack the controls on top of each other
            width=320,
            controls=[
                self.calendar,
                Container(
                    on_click=lambda e: self._get_calendar(e),
                    width=320,
                    height=45,
                    border_radius=8,
                    bgcolor="Green",
                    padding=padding.only(left=15, right=5),
                    content=Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            self.today,
                            Container(
                                width=32,
                                height=32,
                                border=border.only(
                                    left=BorderSide(0.9,"white"),
                                ),
                                alignment=alignment.center,
                                content=Icon(
                                    name=icons.CALENDAR_MONTH_SHARP,
                                    size=15,
                                    opacity=0.65,
                                ),
                            ) ,                                
                        ],
                    ),
                ),
            ],
        )

#buttons for pagination
class BTNPagination(UserControl):
    def __init__(self, txt_name, function):
        self.txt_name = txt_name
        self.function = function
        super().__init__()

    def build(self):
        return IconButton(
            content=Text(self.txt_name, size=8, weight="bold"),
            width=56,
            height=28,
            on_click=self.function,
            style=ButtonStyle(
                shape={"": RoundedRectangleBorder(radius=6)}, bgcolor={"": "teal600"}
            ),
        )

class Reminder(UserControl):
    pass    
#main function
def main(page: Page):


    page.fonts = {
        "SF Pro": "https://raw.githubusercontent.com/google/fonts/master/ofl/sfprodisplay/SFProDisplay-Bold.ttf",
    }
    page.title = "CalReminder"
    page.theme = Theme(font_family="SF Pro")
    page.window_max_width = 410
    page.window_width = 800
    page.window_max_height = 800
    page.window_height = 800
    page.bgcolor = "#86E3CE"
    page.horizontal_alignments = "center"
    page.verticle_alignments = "center"
    page.navigation_bar = ft.NavigationBar(bgcolor = "#fe96a5",selected_index=2,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.CHECK, ),
            ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG, ),
            ft.NavigationDestination(icon=ft.icons.HOME, ),
            ft.NavigationDestination(icon=ft.icons.CALCULATE,),
            ft.NavigationDestination(icon=ft.icons.PERSON, ),
            ]
  )

    #instances
    cal = SetCalendar()
    date = DateSetUp(cal)

    #main UI
    page.add(
        Row(
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.END,
            controls=[
                date
            ]
        )
    )
    page.update()

if __name__ == "__main__":
    flet.app(target=main)