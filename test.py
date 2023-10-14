import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"



def main(page: ft.Page):
    def items():
        r = ft.Row(wrap=True, scroll="always",expand=1)

        for i in range(5):
            r.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Image("images/Nutella-Milkshake.jpg",expand=1),
                        ft.Row(
                            [
                                ft.IconButton(ft.icons.REMOVE,expand=1),
                                ft.TextField(value="0", text_align=ft.TextAlign.RIGHT,expand=1),
                                ft.IconButton(ft.icons.ADD,expand=1),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ]),
                    margin=10,
                    padding=10,
                    bgcolor=ft.colors.YELLOW_300,
                    width=180,
                    height=250,
                    border_radius=10,
                    # ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                )
            )
        return r
    
    def navBar():
        rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            # extended=True,
            min_width=100,
            min_extended_width=400,
            leading=ft.Image("images/logo.png",width=70,height=70),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.ADD_SHOPPING_CART, selected_icon=ft.icons.ADD_SHOPPING_CART_OUTLINED, label="فروش"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.MONEY),
                    selected_icon_content=ft.Icon(ft.icons.MONEY),
                    label=" خرید ",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.EVENT_NOTE,
                    selected_icon_content=ft.Icon(ft.icons.EVENT_NOTE_OUTLINED),
                    label_content=ft.Text("گزارشات"),
                ),
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
        )
        return rail

    def controlerOrder():
        return ft.Container(
            content=ft.Row([
                ft.Text("هزینه نهایی : {80,000}", size=13, weight=ft.FontWeight.W_900),
                ft.FilledButton("پرداخت", icon="add"),
            ],alignment=ft.MainAxisAlignment.END,expand=1),
            bgcolor='white',
            
        )
        
    def footerLog():
        lv = ft.ListView(spacing=10, padding=20, auto_scroll=True, height=200)
        count = 1

        for i in range(10):
            lv.controls.append(
                ft.Container(
                    ft.Column([
                        ft.Row([
                            ft.IconButton(ft.icons.REMOVE),
                            ft.IconButton(ft.icons.REMOVE)
                        ])
                    ]),
                    bgcolor=ft.colors.YELLOW,
                    padding=5
                )
            )
            count += 1

        return lv
    
    
    page.add(
        ft.Row(
            [
                navBar(),
                ft.VerticalDivider(width=1),
                ft.Column([ 
                    controlerOrder(),
                    ft.Divider(height=9, thickness=3),
                    items(),
                    ft.Container(footerLog(),border_radius=10,border=ft.border.all(2, ft.colors.GREY),)
                ], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )
        
    

ft.app(target=main)