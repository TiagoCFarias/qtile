from libqtile import bar, layout, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
import fontawesome as fa
from theme import *

left_triangle = ""
right_triangle = ""

backslash = "◥"
slash = "◣"
left_separator = slash
right_separator = backslash
bar_height = 20



default = [
    #region First Section of the bar

    widget.TextBox(
        text=" ",
        background=aqua,
    ),
    # CPU
    widget.TextBox(
        text=fa.icons['microchip'],
        background=aqua,
        font="Font Awesome 6 Free",
    ),
    widget.CPU(
        format="{load_percent:2.1f}%",
        background=aqua,
    ),

    widget.TextBox(
        text=right_triangle,
        foreground=aqua,
        padding=0,
        background=blue0,
        fontsize=38,
    ),

    # Memory
    widget.TextBox(
        text=fa.icons['memory'],
        background=blue0,
        font="Font Awesome 6 Free",
    ),
    widget.Memory(
        background=blue0,
        format="{MemUsed: .0f}{mm}",
    ),

    widget.TextBox(
        text=right_triangle,
        foreground=blue0,
        padding=0,
        background=transparent,
        fontsize=38,
    ),
    # widget.CurrentLayout(
    # ),

    widget.Spacer(
        foreground=background,
        background=transparent,
    ),
    widget.GroupBox(
        disable_drag=True,
        spacing=10,
        center_aligned=True,
        active=purple,
        inactive=blue,
        highlight_method="text",
        highlight_color=transparent,
        this_current_screen_border=mark,
        urgent_border=warning,
        hide_unused=False,
        font="Font Awesome 6 Free",
        background=transparent,
        foreground=foreground,
        fontsize=22,

    ),

    # prompt will not use since i'm running drun
    # widget.Prompt(
    #     background=background,
    # ),

    #endregion

    # widget.WindowName(
    #     foreground=background,
    #     background="#00000000"
    # ),
    widget.Spacer(
        foreground=background,
        background=transparent,
    ),

    
    # region end section
    widget.Systray(
        background=transparent,
        icon_size=20,
    ),
    widget.TextBox(
        text=left_triangle,
        foreground=red,
        padding=0,
        background=transparent,
        fontsize=38,
    ),
    widget.TextBox(
        text=fa.icons['headphones'],
        background=red,
        font="Font Awesome 6 Free",
    ),
    widget.Volume(
        fmt="{}",
        background=red,
        volume_app="pactl",
    ),
    widget.TextBox(
        text=left_triangle,
        foreground=green,
        padding=0,
        background=red,
        fontsize=38,
    ),

    widget.Battery(
        notify_below=20,
        format="{char}",
        charge_char=fa.icons['plug'],
        background=green,
        discharge_char=fa.icons['bolt'],
        update_interval = 5,
        font="Expansiva",
    ),
    widget.Battery(
        notify_below=40,
        format="{percent:2.1%} {hour:d}:{min:02d}",
        background=green,
        # font="Expansiva",
    ),
    # calendar
    widget.TextBox(
        text=left_triangle,
        foreground=yellow,
        padding=0,
        background=green,
        fontsize=38,
    ),
    widget.TextBox(
        text=fa.icons['calendar'],
        background=yellow,
        font="Font Awesome 6 Free",
    ),
    widget.Clock(
        format="%d.%m",
        background=yellow,
    ),
    widget.TextBox(
        text=left_triangle,
        foreground=blue,
        padding=0,
        background=yellow,
        fontsize=38,
    ),
    widget.TextBox(
        text=fa.icons['clock'],
        background=blue,
        font="Font Awesome 6 Free",
    ),
    widget.Clock(
        format="%a %I:%M %p",
        background=blue,
    ),
    widget.TextBox(
        text=left_triangle,
        foreground=purple,
        padding=0,
        background=blue,
        fontsize=38,
    ),
    widget.TextBox(
        text="\u23fb",
        fontsize=16,
        mouse_callbacks={
            "Button1": lazy.spawn("systemctl suspend"),
            "Button2": lazy.spawn("systemctl restart"),
            "Button3": lazy.spawn("sudo shutdown -h now"),
        },
        background=purple,
    ),
    widget.Sep(
        linewidth=5,
        background=purple,
        foreground=purple,
    ),

    # endregion
]


screens = [
    Screen(
        wallpaper="~/Pictures/wallpapers/mountains.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            default,
            25,
            # margins=[2, 0, 0, 0],
            # border_width=[4, 0, 4, 0],
            # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"],  # Borders are magenta
            opacity=1,
            background="#00000000",
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

