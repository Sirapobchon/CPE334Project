import flet as ft

class ChangeNav(ft.UserControl):
    def __init__(self, page, selected_index):
        super().__init__()
        self.page = page
        self.index = selected_index

    def changetab(self):
        destinations = ['/', '/', '/', '/calculator', '/login']
        destination_url = destinations[self.index]
        self.page.go(destination_url)

    def build(self):
        print(self.index)  # Note: This print statement should be inside the build method
        return None  # You need to return something from the build method, even if it's None

class CalculatorLogic(ft.UserControl):
    def cal_cost_per_unit(self, cost, unit):
        return ("%.3f" % round(cost / unit, 3))

    def calculate(self, product_container, cost_per_unit_value):
        product_data = {}
        cost_per_unit_value.value = ""
        for i, control in enumerate(product_container.controls, start=1):
            cost = int(control.content.controls[1].value)
            unit = int(control.content.controls[2].value)
            cost_per_unit = self.cal_cost_per_unit(cost, unit)
            product_data.setdefault(control.content.controls[0].value, [])
            product_data[control.content.controls[0].value].append({
                "cost": cost,
                "unit": unit,
                "costPerUnit": cost_per_unit,
            })
            cost_per_unit_value.value += (
                f"Product {i} = {cost_per_unit} Cost/Unit\n"
            )

    def reset(self, product_container, cost_per_unit_value, quantity):
        product_container.controls.clear()
        cost_per_unit_value.value = ""
        if not quantity.value:
            return
        else:
            # Assuming you want to store the quantity in some dictionary
            my_dict = {"quantity": quantity.value}
            quantity.value = ""  # clear the value of quantity
            return my_dict

    def add_price(self, product_container, quantity):
        product_container.controls.clear()
        for i, x in enumerate(range(1, int(quantity.value) + 1), start=1):
            product_container.controls.append(
                ft.Container(
                    alignment=ft.alignment.center,
                    padding=10,
                    bgcolor="white",
                    border_radius=40,
                    width=300,
                    content=ft.Column([
                        ft.Text(f"Product {i}", size=30, weight="bold", color="#000000"),
                        ft.TextField(label="Cost", border_radius=40, width=200, height=50, color="#000000"),
                        ft.TextField(label="Unit", border_radius=40, width=200, height=50, color="#000000"),
                    ])
                )
            )

class Tempfile():
    #self.cost_per_unit_value = ft.Text("", size=20)
    #self.product_container = ft.Column(scroll="auto")
    #    self.quantity = ft.TextField(
    #        hint_text="Total of Compare product prices",
    #        on_change=lambda e: self.calculator_logic.add_price(self.product_container, self.quantity),
    #        border_radius=40,
    #        color="BLACK",
    #        bgcolor="WHITE",
    #        border_color="#FA987B",
    #        focused_border_color="#CCABD8",
    #        width=300,
    #    )
    
    def plan(self, page):
        return None

class Calculator(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.calculator_logic = CalculatorLogic
        
    def build(self):
        return ft.SafeArea(
    ft.Container(
        ft.Column([
            # Header
            ft.Row([
                ft.Container(
                    width=40,
                    margin=ft.margin.only(top=10,left=10),
                    content=ft.TextButton(
                        "<",
                        style=ft.ButtonStyle(color="#7D7C7C"),
                        on_click=lambda e: self.page.go('/'),  
                    )
                ),
                ft.Text("Price Comparison",
                    size=30, 
                    weight="bold",
                    color="#000000"
                ),
                ft.Container(
                    width=40,
                ),
            ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            
            ft.Row([
                ft.ElevatedButton("Reset", 
                    bgcolor="white", 
                    color="#424949",
                    #on_click=lambda e: self.calculator_logic.reset(product_container, cost_per_unit_value, quantity), width=120
                ),
                ft.ElevatedButton("Calculate", 
                    bgcolor="red", 
                    color="white",
                    #on_click=lambda e: self.calculator_logic.calculate(product_container, cost_per_unit_value), width=120
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
            #cost_per_unit_value,

            ft.Stack([
                ft.Container(
                    alignment=ft.alignment.bottom_center,
                    margin=ft.margin.only(bottom=10),
                    content= ft.NavigationBar(bgcolor="#fe96a5", selected_index=3,
                        destinations=[
                            ft.NavigationDestination(icon=ft.icons.CHECK),
                            ft.NavigationDestination(icon=ft.icons.SHOPPING_BAG),
                            ft.NavigationDestination(icon=ft.icons.HOME),
                            ft.NavigationDestination(icon=ft.icons.CALCULATE),
                            ft.NavigationDestination(icon=ft.icons.PERSON),
                        ],
                        on_change=lambda e: ChangeNav(e.page, e.control.selected_index).changetab(),
                    ),
                ),
            ]),
        ]),
        
        theme=ft.Theme(color_scheme_seed=ft.colors.BLACK),
        theme_mode=ft.ThemeMode.LIGHT,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[
                "#ddf7f1",
                "#f2f8e6",
                "#fff5e1",
                "#feddda",
                "#f1e7f5",
            ],
            tile_mode=ft.GradientTileMode.MIRROR,
        ),
        width=800,
        border_radius=10,
        height=760,
        #expand=True,
    ),
)

