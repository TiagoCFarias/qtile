from libqtile import bar, layout
from libqtile.config import Screen
from libqtile.lazy import lazy
# import fontawesome as fa

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from colors import *
from theme import *

left_triangle = ""
right_triangle = ""

backslash = "◥"
slash = "◣"
left_separator = slash
right_separator = backslash
bar_height = 30 
radius = int(bar_height / 4)

widget_defaults = dict(
    font="NovaMono for Powerline Bold",  # "Source Code Pro Regular", "Expansiva" "JetBrains Mono Bold",
    fontsize=12,
    padding=10,
    foreground=foreground,
    background=transparent,
)

extension_defaults = widget_defaults.copy()

custom_spacer = widget.Spacer(length=5)

# background_gradient = [colors[0], colors[4], colors[0]]
background_gradient = dark_purple_gradient

default = [
    #region First Section of the bar

    widget.CurrentLayoutIcon(
        background=transparent,
        scale=0.75,
        decorations=[
            RectDecoration(colour=background_gradient, radius=radius, filled=True, padding_y=0)
        ],
    ),
    custom_spacer,
    # CPU   
    widget.CPU(
        format="\uf2db {load_percent:2.1f}%",
        foreground=foreground,
        decorations=[
            RectDecoration(colour=background_gradient, radius=radius, filled=True, padding_y=0)
        ]
    ),
    custom_spacer,    
    widget.Memory(
        format="\uf1c0 {MemUsed: .0f}{mm}",
        padding=20,
        foreground=foreground,
        decorations=[
            RectDecoration(colour=background_gradient, radius=radius, filled=True, padding_y=0)
        ]
    ),
    custom_spacer,
    widget.ThermalSensor(
        format="\uf2c7 {temp:.1f}{unit}",
        decorations=[
            RectDecoration(colour=background_gradient, radius=radius, filled=True, padding_y=0)
        ]
    ),

    widget.Spacer(
        foreground=background,
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
        foreground=foreground,
        fontsize=15,
        decorations=[
            RectDecoration(colour=transparent, radius=radius, filled=True, padding_y=0)
        ]
    ),

    custom_spacer,
    
    widget.Systray(
        icon_size=20,
    ),

    custom_spacer,

    widget.Volume(
        fmt="\uf025 {}",
        volume_app="pactl",
        foreground=foreground,
        decorations=[
            RectDecoration(colour=background_gradient, radius=radius, filled=True, padding_y=0)
        ]
    ),
    custom_spacer,
    widget.Battery(
        notify_below=40,
        format="{char} {percent:2.1%} {hour:d}:{min:02d} {watt:.2f} W",
        charge_char='\uf1e6',
        background=transparent,
        foreground=foreground,
        discharge_char='\uf0e7',
        update_interval = 5,
        decorations=[
            RectDecoration(colour=background_gradient, radius=radius, filled=True, padding_y=0)
        ]
    ),
    custom_spacer,

    widget.Clock(
        format="\uf017 %a %I:%M %p \uf133 %d.%m",
        foreground=foreground,
        decorations=[
            RectDecoration(colour=background_gradient, radius=radius, filled=True, padding_y=0)
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
        foreground=foreground,
        background=transparent,
        decorations=[
            RectDecoration(colour=background_gradient, radius=radius, filled=True, padding_y=0)
        ],
    ),
    # endregion
]


screens = [
    Screen(
        wallpaper="~/.config/qtile/wallpapers/mountains-moon-trees-minimalism-hd.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            default,
            bar_height,
            margin=[int(bar_height / 4),int(bar_height / 6), int(bar_height / 4), int(bar_height / 6)],
            # 4, 6 
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
