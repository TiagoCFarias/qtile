from libqtile import bar, layout
from libqtile.config import Screen
from libqtile.lazy import lazy
# import fontawesome as fa

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration

from theme import *
from colors import *

left_triangle = ""
right_triangle = ""

backslash = "◥"
slash = "◣"
left_separator = slash
right_separator = backslash
bar_height = 40
radius = 20

widget_defaults = dict(
    font="JetBrains Mono",  # "Source Code Pro Regular", "Expansiva"
    fontsize=12,
    padding=10,
    foreground=foreground,
    background=transparent,
)

extension_defaults = widget_defaults.copy()

custom_spacer = widget.Spacer(length=5)

default = [
    #region First Section of the bar

    widget.CurrentLayoutIcon(
        background=transparent,
        scale=0.75,
        decorations=[
            RectDecoration(colour=colors[0], radius=radius, filled=True, padding_y=0)
        ]
    ),
    custom_spacer,
    # CPU   
    widget.CPU(
        format="\uf2db {load_percent:2.1f}%",
        decorations=[
            RectDecoration(colour=[colors[4], colors[0], colors[4]], radius=radius, filled=True, padding_y=0)
        ]
    ),
    custom_spacer,    
    widget.Memory(
        format="\uf1c0 {MemUsed: .0f}{mm}",
        padding=20,
        decorations=[
            RectDecoration(colour=colors[0], radius=radius, filled=True, padding_y=0)
        ]
    ),


    widget.Spacer(
        foreground=background,
    ),
    widget.GroupBox(
        disable_drag=True,
        spacing=1,
        center_aligned=True,
        active=purple,
        inactive=blue,
        highlight_method="text",
        highlight_color=transparent,
        this_current_screen_border=mark,
        urgent_border=warning,
        hide_unused=False,
        font="Font Awesome 6 Free",
        foreground=foreground,
        fontsize=22,
        decorations=[
            RectDecoration(colour=colors[0], radius=radius, filled=True, padding_y=0)
        ]
    ),

    # prompt will not use since i'm running drun
    # widget.Prompt(
    #     background=background,
    # ),

    #endregion

    widget.Spacer(
        foreground=background,
    ),

    
    # region end section
    widget.Systray(
        icon_size=20,
    ),

    # widget.Textbox(
    #     **rounded_right,
    # ),

    widget.Volume(
        fmt="\uf025 {}",
        volume_app="pactl",
        decorations=[
            RectDecoration(colour=colors[0], radius=radius, filled=True, padding_y=0)
        ]
    ),
    custom_spacer,
    widget.Battery(
        notify_below=40,
        format="{char} {percent:2.1%} {hour:d}:{min:02d}",
        charge_char='\uf1e6',
        background=transparent,
        discharge_char='\uf0e7',
        update_interval = 5,
        font="JetBrains Mono",
        decorations=[
            RectDecoration(colour=colors[0], radius=radius, filled=True, padding_y=0)
        ]
    ),
    custom_spacer,
    # calendar

    widget.Clock(
        format="\uf133 %d.%m \uf017 %a %I:%M %p",
        background=transparent,
        decorations=[
            RectDecoration(colour=colors[0], radius=radius, filled=True, padding_y=0)
        ]
    ),
    custom_spacer,
    widget.TextBox(
        text="\u23fb",
        fontsize=16,
        padding=20,
        mouse_callbacks={
            "Button1": lazy.spawn("systemctl suspend"),
            "Button2": lazy.spawn("systemctl restart"),
            "Button3": lazy.spawn("sudo shutdown -h now"),
        },
        background=transparent,
        decorations=[
            RectDecoration(colour=colors[0], radius=radius, filled=True, padding_y=0)
        ],
    ),
    # endregion
]


screens = [
    Screen(
        wallpaper="~/Pictures/wallpapers/mountains.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            default,
            bar_height,
            margin=[10,6,4,6],
            # margins=[2, 0, 0, 0],
            # border_width=[4, 0, 4, 0],
            # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"],  # Borders are magenta
            opacity=1,
            background=transparent,
            border_color=transparent,
        ),
    ),
]

# unused widgets 
                # widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                # widget.QuickExit(),

                # widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                # ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),

    # widget.TextBox(
    #     text=left_triangle,
    #     foreground=purple,
    #     padding=0,
    #     background=blue,
    #     fontsize=38,
    # ),