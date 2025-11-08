import flet as ft

from logic.logic import send_response


chat=send_response()

def onsubmit(e):
    chat_area.controls.append(MEChatBox(response=box.value))
    chat_area.update()

    user_message = box.value
    box.value=""
    box.update()

    tag_ai = chat(message=user_message)
    chat_area.controls.append(AIChatBox(response=tag_ai))
    chat_area.update()
    return


class MenuIcon(ft.Container):
    def __init__(self, iconsrc, iconsize, label: str = None, labelsize: str = 14):
        super().__init__()
        self.iconsrc=iconsrc
        self.content=ft.Column(
            [
                ft.Container(ft.Image(src=self.iconsrc, fit=ft.ImageFit.COVER),width=iconsize, height=iconsize),
                ft.Container(ft.Text(value=label, text_align=ft.TextAlign.CENTER ,style=ft.TextStyle(color="white", size=labelsize,weight=ft.FontWeight.BOLD)))
            ],
            spacing=3 if label is not None else 0,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True
        )


class TextBox(ft.Container):
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


class AIChatBox(ft.Container):
    def __init__(self, response=None, imgsrc=None, size:int=36, radius:int=12):
        super().__init__()
        self.ai_reply = response
        self.alignment=ft.alignment.center_left
        self.chatbox=ft.Container(
            width=400,
            bgcolor="#FCFCFC",
            content=ft.Text(value=self.ai_reply, text_align=ft.TextAlign.LEFT, overflow=ft.TextOverflow.CLIP,),
            border=ft.border.all(2, ft.Colors.with_opacity(1, "white")),
            padding=8,
            border_radius=radius     
        )
        self.content=ft.Container(
            # height=100,
            padding=ft.padding.only(left=10,right=10,top=5,bottom=5),
            # bgcolor="black",
            content=ft.Row(
                [self.chatbox],
                alignment=ft.MainAxisAlignment.START,
                expand=True,
                expand_loose=False
            )
        )


class MEChatBox(ft.Container):
    def __init__(self, response=None, imgsrc=None, size:int=36, radius:int=12):
        super().__init__()
        self.me_reply = response
        self.alignment=ft.alignment.center_right
        self.chatbox=ft.Container(
            bgcolor="#78ACFE",
            content=ft.Text(value=self.me_reply, color="white"),
            border=ft.border.all(3,ft.Colors.with_opacity(1, "#5995F7")),
            padding=8,
            border_radius=radius
        )
        self.content=ft.Container(
            padding=20,
            content=ft.Row(
                [self.chatbox],
                alignment=ft.MainAxisAlignment.END,
                expand=True,
                expand_loose=False
            )
        )

box = ft.TextField(
    hint_text="Ask Anything....",
    hint_style=ft.TextStyle(color=ft.Colors.BLACK38, size=18,weight=ft.FontWeight.W_500),
    width=500, height=80,
    multiline=True,
    shift_enter=True,
    autofocus=True,
    border=ft.InputBorder.NONE,
    text_vertical_align=ft.VerticalAlignment.CENTER,
    on_submit=onsubmit,
)

send = ft.GestureDetector(ft.Container(ft.Image(src="src/assets/icons/send_ico.png",fit=ft.ImageFit.COVER),width=40, height=40),on_tap=onsubmit)

field = ft.Container(
    margin=ft.margin.only(bottom=20),
    content=ft.Stack(
        [
            ft.Container(
                width=600, height=80, border_radius=55, expand=True, expand_loose=True,
                border=ft.border.all(4, color=ft.Colors.with_opacity(0.4, "#ED759F")),
                rotate=ft.Rotate(angle=-0.03),
                blur=28,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.center_left,
                    end=ft.alignment.center_right,
                    colors=[
                        ft.Colors.with_opacity(0.56, "#F46ABD"),
                        ft.Colors.with_opacity(0.36, "#FFFEFE"),
                        ft.Colors.with_opacity(0.42, "#ED759F"),
                        ft.Colors.with_opacity(0.43, "#81B9EA"),
                    ],
                    stops=[
                        0,
                        0.27,
                        0.59,
                        0.86
                    ]
                )
            ),
            ft.Container(
                width=600, height=80, border_radius=55, expand=True, expand_loose=True, bgcolor="white",padding=ft.padding.only(top=10),
                border=ft.border.all(2, color=ft.Colors.with_opacity(0.6, "#000000")),
                alignment=ft.alignment.bottom_center,
                content=ft.Row(
                    [box,send],tight=True
                )
            )
        ]
    )
)

menu_bar=ft.Container(
    expand=1,
    # border=ft.border.all(1, "black"),
    alignment=ft.alignment.center_left,
    padding=ft.padding.only(left=20),
    content=ft.Column(
        [
            MenuIcon(iconsrc="src/assets/icons/home_ico.png", iconsize=48, label="Chat", labelsize=16),
            MenuIcon(iconsrc="src/assets/icons/plus_ico.png", iconsize=48, label="New", labelsize=16),
            MenuIcon(iconsrc="src/assets/icons/folder_ico.png", iconsize=48, label="Recent", labelsize=16),
            MenuIcon(iconsrc="src/assets/icons/gear_ico.png", iconsize=48, label="Settings", labelsize=16)
        ],
        spacing=18,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
)

chat_area = ft.Column(
    expand=True,
    scroll=ft.ScrollMode.HIDDEN,
    auto_scroll=True,
    alignment=ft.MainAxisAlignment.START,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
)

chat_block=ft.Container(
    expand=5,
    border_radius=30,
    border=ft.border.all(3, ft.Colors.with_opacity(0.58, "white")),
    bgcolor=ft.Colors.with_opacity(0.35, "white"),
    blur=6.4,
    content=ft.Stack(
        [
            ft.Container(
                expand=True,bgcolor="transparent",
                padding=12,
                content=chat_area,
                height=900
            ),
            field
        ],
        alignment=ft.alignment.bottom_center
    ),
)



app_bar=ft.Container(
    expand=1,
    padding=ft.padding.only(left=10, right=10),
    content=ft.Row(
        [
            MenuIcon(iconsrc="src/assets/icons/menu_ico.png", iconsize=48),
            ft.Container(ft.Text(value="X-Gen AI", size=48, weight=ft.FontWeight.BOLD, color="#6074F6")),
            ft.Row(
                [
                    ft.Container(ft.Image(src='src/assets/icons/dots_ico.png', fit=ft.ImageFit.COVER),width=30, height=10,margin=ft.margin.only(bottom=10)),
                    ft.Container(ft.Image(src='src/assets/icons/profile_ico.png', fit=ft.ImageFit.COVER),width=60,height=60)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.END,
                tight=True
            )  
        ],
        spacing=100,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )
)

app_body = ft.Container(
        expand=8,
        content=ft.Row(
            [menu_bar, chat_block]
        )
    )
