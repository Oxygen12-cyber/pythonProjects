import flet as ft
from components.components import MenuIcon, AIChatBox, MEChatBox



def main(page: ft.Page):


    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER


    page.add(
        ft.Container(
            expand=True,
            bgcolor="white",
            alignment=ft.alignment.center,
            content= ft.Column(
                [
                    AIChatBox(response="hello there im an ai haha"),
                    MEChatBox(response="describe hunting in a word")
                ]
            )
        )
    )


if __name__ == "__main__":
    ft.app(target=main, assets_dir="src/assets")