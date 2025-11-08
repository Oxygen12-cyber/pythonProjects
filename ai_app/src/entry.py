import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import flet as ft
from components.components import app_bar, app_body


def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.window.min_width = 1280
    page.window.min_height = 720
    page.window.alignment=ft.alignment.center
    page.theme_mode=ft.ThemeMode.LIGHT

    page.add(
        ft.Container(
            expand=True,
            padding=ft.padding.only(bottom=30, right=10),
            gradient=ft.LinearGradient(
                colors=[
                    ft.Colors.with_opacity(0.32, "#3da0e2"),
                    ft.Colors.with_opacity(0.39, "#fdb9fd"),
                    ft.Colors.with_opacity(0.46, "#e4aab2"),
                ],
                stops=[0.08, 0.57, 0.87],
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
            ),
            alignment=ft.alignment.bottom_right,
            content=ft.Column([app_bar, app_body]),
        )
    )

    print(page.width, page.height)
if __name__ == "__main__":
    ft.app(target=main, assets_dir="src/assets")
