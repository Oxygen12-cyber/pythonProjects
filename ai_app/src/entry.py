import flet as ft
from logic.logic import send_response
from components.components import app_body, app_bar, MEChatBox, AIChatBox, box, chat_area


def main(page: ft.Page):
    page.padding=0
    page.spacing=0

            

    page.add(
        ft.Container(
            expand=True,
            padding=ft.padding.only(bottom=30, right=10),
            gradient=ft.LinearGradient(
                colors=[
                    "#523da0e2",
                    "#64fdb9fd",
                    "#76e4aab2"
                ],
                stops=[0.08,0.57,0.87],
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right   
            ),
            alignment=ft.alignment.bottom_right,
            content=ft.Column(
                [
                    app_bar,
                    app_body
                ]
            )
        )
    )


if __name__ == "__main__":
    ft.app(target=main, assets_dir="src/assets")
