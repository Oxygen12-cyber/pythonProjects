import flet as ft

def main(page: ft.Page):
    page.window.height=600
    page.window.width=800
    page.window.frameless=True
    page.window.ignore_mouse_events=True
    page.window.alignment=ft.alignment.center

    page.adaptive=True
    page.padding=0
    page.spacing=0

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            bgcolor="white",
            content=ft.Stack(
                [
                    ft.Container(
                        expand=True,
                        content=ft.Image(
                            width=800,
                            height=600,
                            src="images/night_bg.jpg",
                            fit=ft.ImageFit.COVER
                        )
                    ),
                    ft.Container(bgcolor=ft.Colors.with_opacity(0.6, "black")),
                    ft.Container(
                        # content=ft.Column([ft.Text("hello, oxygen"),ft.Text("hello, oxygen"),ft.Text("hello, oxygen"),ft.Text("hello, oxygen")]),
                        # bgcolor="amber",
                        # alignment=ft.alignment.bottom_center,
                        # # bottom=60,
                    )
                ]
            )
        )
    )

if __name__=="__main__":
    ft.app(target=main, assets_dir="src/assets")