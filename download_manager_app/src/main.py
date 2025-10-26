import flet as ft
from src.components.component import *


def main(page: ft.Page):
    page.window.height=600
    page.window.width=800
    page.window.resizable=False
    page.window.alignment=ft.alignment.center
    
    page.bgcolor="#4d5057"
    page.padding=0
    
    
    contents=ft.Container()


    # left_side_container = ft.Container(
    #     bgcolor="#3a3c41",
    #     width=240,
    #     shadow=ft.BoxShadow(
    #         spread_radius=0.1,
    #         blur_radius=10,
    #         color="#3a3c41",
    #         blur_style=ft.ShadowBlurStyle.SOLID
    #     ),
    #     content=contents
    # )
    left_side_container = ft.Container(
        width=80,
        height=250,
        bgcolor="#3a3c41",
        border_radius=20,
        margin=ft.margin.only(left=20),
        border=ft.border.all(1.7, ft.Colors.with_opacity(0.5, "grey"))
    )

    


    page.add(
        ft.Container(
            expand=True,
            bgcolor="#4d5057",
            content=ft.Row(
                [left_side_container],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,

            )
        )
    )


ft.app(main)
