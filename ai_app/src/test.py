import flet as ft
# from components.components import MenuIcon, AIChatBox, MEChatBox



def main(page: ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER


    page.add(
        ft.Container(
            expand=True,
            padding=ft.padding.only(bottom=30, right=10),
            gradient=ft.LinearGradient(
                colors=[
                    ft.Colors.with_opacity(0.3, "blue"),
                    ft.Colors.with_opacity(0.4, "red"),
                    # ft.Colors.with_opacity(1.0, "#e4aab2"),
                ],
                stops=[
                    0.08,
                    0.57,
                    # 0.87
                ],
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
            ),
            alignment=ft.alignment.bottom_right,
            # content=ft.Column([app_bar, app_body]),
        )
    )


if __name__ == "__main__":
    ft.app(target=main, assets_dir="src/assets")