import flet as ft



def main(page: ft.Page):

    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER


    page.add(ft.Container(ft.Text(size=60, value="Hello, Oxygen")))

if __name__=="__main__":
    ft.app(main)