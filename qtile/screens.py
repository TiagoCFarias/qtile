from libqtile import bar, layout
from libqtile.config import Screen
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration

from colors import *
from theme import *
from color_schemes.nordtheme import * 

left_triangle = ""
right_triangle = ""

bar_height = 30 
radius = int(bar_height / 4)

background_gradient = dark_purple_gradient
widget_defaults = dict(
    font="NovaMono for Powerline Bold",  # "Source Code Pro Regular", "Expansiva" "JetBrains Mono Bold",
    fontsize=12,
    padding=10,
    foreground=foreground,
    decorations=[
       RectDecoration(colour=background_gradient, radius=radius, filled=True, padding_y=0)
    ],
   background=transparent,
)
extension_defaults = widget_defaults.copy()

custom_spacer = widget.Spacer(length=5, decorations=[])

default = [
    widget.CurrentLayoutIcon(
        background=polar_night[0],
        scale=0.75,
    ),
    custom_spacer,
    widget.CPU(
        format="\uf2db {load_percent:2.1f}%",
        background=polar_night[1],
    ),
    custom_spacer,    
    widget.Memory(
        format="\uf1c0 {MemUsed: .0f}{mm}",
        background=polar_night[2],
    ),
    custom_spacer,
    widget.ThermalSensor(
        format="\uf2c7 {temp:.1f}{unit}",
    ),
    custom_spacer,
    widget.Clipboard(
        timeout=None,
    ),
    widget.Spacer(
        decorations=[]
    ),
    widget.GroupBox(
        disable_drag=True,
        spacing=0,
        center_aligned=True,
        # highlight_color=white,
        active=blue0,
        inactive=colors[3],
        highlight_method="text",
        this_current_screen_border=white0,
        urgent_border=warning,
        hide_unused=False,
        font="Font Awesome 6 Bold",
        fontsize=15,
        decorations=[]
    ),
    custom_spacer,
    widget.Systray(
        icon_size=20,
        decorations=[]
    ),

    custom_spacer,

    widget.Volume(
        fmt="\uf025 {}",
        volume_app="pactl",
    ),
    custom_spacer,
    widget.Battery(
        notify_below=40,
        format="{char} {percent:2.1%} {hour:d}:{min:02d} {watt:.2f} W",
        charge_char='\uf1e6',
        background=transparent,
        discharge_char='\uf0e7',
        update_interval = 5,
    ),
    custom_spacer,

    widget.Clock(
        format="\uf017 %a %I:%M %p \uf133 %d.%m",
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
    ),
]

screens = [
    Screen(
        wallpaper="~/.config/qtile/wallpapers/mountains-moon-trees-minimalism-hd.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            default,
            bar_height,
            margin=[int(bar_height / 4),int(bar_height / 6), int(bar_height / 4), int(bar_height / 6)],
            opacity=1,
            background=transparent,
            border_color=transparent,
        ),
    ),
]

