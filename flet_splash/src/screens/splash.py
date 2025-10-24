import flet as ft


def main(page: ft.Page):
    page.window.height=600
    page.window.width=800
    page.window.frameless=True
    page.window.ignore_mouse_events=True
    page.window.alignment=ft.alignment.center
    # page.window.opacity=0.8

    # page.adaptive=True
    page.padding=0
    page.spacing=0

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            bgcolor="white",
            content=ft.Container(
                width=200,
                height=400,
                content=ft.Image(
                    src="images/night-bg.jpg",
                    fit=ft.ImageFit.FILL
                )
            )
        )
    )

if __name__=="__main__":
    ft.app(target=main, assets_dir="src/assets")

