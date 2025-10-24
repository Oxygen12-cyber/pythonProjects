from flet import Container, Colors
import flet as ft


class IconBox(Container):
    def __init__(self, bgcolor, imgsrc=None, size:int=36):
        super().__init__(
            height=size,
            width=size,
            border_radius=size,
            alignment=ft.alignment.center,
            shadow=ft.BoxShadow(
                spread_radius=.2,
                blur_radius=5,
                color="black",
                blur_style=ft.ShadowBlurStyle.OUTER
            ),
            bgcolor=bgcolor,
        )
        self.imgsrc=imgsrc
        # self.content=ft.GestureDetector(
        #     ft.Image(src=self.imgsrc, fit=ft.ImageFit.COVER),
        #     on_tap=self.on_tap
        # )

class TextBox(Container):
    def __init__(self, value, margin, hint_text, padding, border_radius:int=10, bgcolor="yellow", width:int=200, height:int=30, on_submit=None):
        super().__init__()
        self.width=width
        self.height=height
        self.bgcolor=bgcolor
        self.border_radius=border_radius
        self.padding=padding
        self.margin=margin

        self.value = value
        self.on_submit = on_submit
        self.alignment=ft.alignment.center_left
        self.content=ft.TextField(
            value=self.value,
            hint_text=hint_text,
            multiline=True,
            max_lines=10,
            min_lines=1,
            keyboard_type=ft.KeyboardType.TEXT,

            shift_enter=True,
            text_align=ft.TextAlign.LEFT,
            cursor_color="black",
            border_color=ft.Colors.TRANSPARENT,
            
            
            on_submit=self.on_submit,
        )



class AIChatBox(Container):
    def __init__(self, response=None, imgsrc=None, size:int=36, radius:int=12):
        super().__init__()
        self.ai_reply = response
        self.alignment=ft.alignment.center_left
        self.chatbox=ft.Row(
            [
                ft.Container(
                    ft.Image(src=imgsrc, fit=ft.ImageFit.COVER),
                    height=size,
                    width=size,
                    border_radius=size,    
                ),
                ft.Column(
                    [
                        ft.Text(value="AI", color="white", size=18),
                        ft.Container(
                            width=200,
                            bgcolor="#5C7581",
                            content=ft.Text(value=self.ai_reply, text_align=ft.TextAlign.LEFT, overflow=ft.TextOverflow.CLIP,expand=True,no_wrap=False,max_lines=0),
                            border=ft.border.all(1, Colors.with_opacity(0.6, "white")),
                            padding=8,
                            border_radius=radius
                        )
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    # expand=True,
                    # expand_loose=True
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.END
        )
        self.content=ft.Container(
            # height=100,
            padding=ft.padding.only(left=10,right=10,top=5,bottom=5),
            bgcolor=ft.Colors.TRANSPARENT,
            content=ft.Row(
                [self.chatbox],
                alignment=ft.MainAxisAlignment.START,
                expand=True,
                expand_loose=False
            )
        )

        


class MEChatBox(Container):
    def __init__(self, response=None, imgsrc=None, size:int=36, radius:int=12):
        super().__init__()
        self.expand=True
        self.me_reply = response
        self.alignment=ft.alignment.center_right
        self.chatbox=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(value="ME", color="white", size=18),
                        ft.Container(
                            bgcolor="#5C7581",
                            content=ft.Text(value=self.me_reply),
                            border=ft.border.all(1,Colors.with_opacity(0.6, "white")),
                            padding=8,
                            border_radius=radius
                        )
                    ],
                    spacing=0,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                    # expand=True,
                    # expand_loose=True
                ),
                ft.Container(
                    ft.Image(src=imgsrc, fit=ft.ImageFit.COVER),
                    height=size,
                    width=size,
                    border_radius=size,    
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.END
        )
        self.content=ft.Container(
            height=100,
            padding=20,
            bgcolor=ft.Colors.TRANSPARENT,
            content=ft.Row(
                [self.chatbox],
                alignment=ft.MainAxisAlignment.END,
                expand=True,
                expand_loose=False
            )
        )

    