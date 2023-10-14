import flet as ft

def main(page: ft.Page):
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("AppBar Example"),
        center_title=False,
        bgcolor=ft.colors.WHITE,
        actions=[
            ft.Row([
                ft.Text("هزینه نهایی : {80,000}", size=13, weight=ft.FontWeight.W_900, selectable=True),
                ft.FilledButton("پرداخت", icon="add"),
            ],alignment=ft.MainAxisAlignment.END,expand=1),
        ],
    )
    page.add(ft.Text("Body!"))

ft.app(target=main)