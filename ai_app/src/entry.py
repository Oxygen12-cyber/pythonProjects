import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Container(
            expand=True,
            content="",
        )
    )


if __name__ == "__main__":
    ft.app(main)
