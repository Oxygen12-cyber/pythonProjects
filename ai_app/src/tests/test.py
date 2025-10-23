import flet as ft
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from logic.logic import send_response
from components.components import IconBox, MEChatBox, TextBox, AIChatBox

def main(page: ft.Page):
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.bgcolor="white"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER,
    page.padding=0
    page.spacing=0



    chat_list = ft.Column(
        spacing=8,
        scroll=ft.ScrollMode.AUTO,
        auto_scroll=True,
        expand=True,
    )
    

    def send_text_message(e):
        chat_list.controls.append(MEChatBox(response=chat_box.value))
        chat_list.update()
        response=send_response(chat_box.value)
        chat_list.controls.append(AIChatBox(response=response))
        print(response)
        chat_list.update()
        

    
    chat_box = ft.TextField(
        multiline=False,
        width=200,
        on_submit=send_text_message
    )

    page.add(
        ft.Container(
            bgcolor="#111921",
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Column(
                [
                    ft.Container(
                        bgcolor="#1a1a1a",
                        expand=6,
                        content=chat_list
                    ),
                    ft.Container(
                        margin=ft.margin.only(bottom=30),
                        bgcolor="#41413e",
                        expand=1,
                        alignment=ft.alignment.center,
                        content=chat_box
                    )
                ], 
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )

if __name__=="__main__":
    ft.app(main)