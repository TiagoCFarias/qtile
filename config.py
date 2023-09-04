# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import os
import subprocess
from gruvbox.gruvbox import *
from theme import *

mod = "mod4"
terminal = guess_terminal()
left_triangle = ""
right_triangle = ""

backslash = "◥"
slash = "◣"
left_separator = slash
right_separator = backslash
bar_height = 20


# COLORS FOR THE BAR
catppuccin = {
    "flamingo": "#F2CDCD",
    "mauve": "#DDB6F2",
    "pink": "#F5C2E7",
    "maroon": "#E8A2AF",
    "red": "#F28FAD",
    "peach": "#F8BD96",
    "yellow": "#FAE3B0",
    "green": "#ABE9B3",
    "teal": "#B5E8E0",
    "blue": "92CDFB",
    "sky": "#89DCEB",
    "white": "#D9E0EE",
    "gray0": "#6E6C7E",
    "black1": "#1A1826",
}


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Keys related to Audio

    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "amixer set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn(
        "amixer set Master toggle")),
    Key([], "XF86AudioMicMute", lazy.spawn(
        "pactl set-source-mute @DEFAULT_SOURCE@ toggle")),

    # Keys related to media
    Key([],"XF86AudioNext", lazy.spawn("mpc next")),
    Key([],"XF86AudioPrev", lazy.spawn("mpc prev")),
    Key([],"XF86AudioPlay", lazy.spawn("mpc toggle")),

    # Keys Related to Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn(
        "xbackligght -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
        "xbacklight -dec 10")),

    # Open program
    Key([mod], "e", lazy.spawn("thunar")),
    Key([mod, "shift"], "w", lazy.spawn("firefox")),
]

# groups = [Group(i) for i in "1234567890"]


def init_group_names():
    return [("I", {"layout": "columns"}),
            ("II", {"layout": "columns"}),
            ("III", {"layout": "columns"}),
            ("IV", {"layout": "columns"}),
            ("V", {"layout": "columns"}),
            ("VI", {"layout": "columns"}),
            ("VII", {"layout": "columns"}),
            ("VIII", {"layout": "columns"}),
            ("IX", {"layout": "columns"}),
            ]


def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]


if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name, switch_group=True)))

# for i in groups:
#     keys.extend(
#         [
#             # mod1 + letter of group = switch to group
#             Key(
#                 [mod],
#                 i.name,
#                 lazy.group[i.name].toscreen(),
#                 desc="Switch to group {}".format(i.name),
#             ),
#             # mod1 + shift + letter of group = switch to & move focused window to group
#             Key(
#                 [mod, "shift"],
#                 i.name,
#                 lazy.window.togroup(i.name, switch_group=True),
#                 desc="Switch to & move focused window to group {}".format(
#                     i.name),
#             ),
#             # Or, use below if you prefer not to switch to that group.
#             # # mod1 + shift + letter of group = move focused window to group
#             # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#             #     desc="move focused window to group {}".format(i.name)),
#         ]
#     )

layouts = [
    layout.Columns(border_focus_stack=[
                   "#d75f5f", "#8f3d3d"], border_width=4, margin=5,),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrains Mono",  # "Source Code Pro Regular",
    fontsize=12,
    padding=3,
    foreground=foreground,
    background=background,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/Pictures/wallpapers/pxfuel.jpg",
        wallpaper_mode="fill",

        top=bar.Bar(
            [
                # CPU

                widget.CPU(
                    format="CPU {load_percent:2.1f}%",
                    background=aqua,
                    font="Expansiva",
                ),
                widget.TextBox(
                    text=right_triangle,
                    foreground=aqua,
                    padding=0,
                    background=blue0,
                    fontsize=38,
                ),

                # Memory
                widget.Memory(
                    background=blue0,
                    format="{MemUsed: .0f}{mm}",
                    font="Expansiva",
                ),
                widget.TextBox(
                    text=right_triangle,
                    foreground=blue0,
                    padding=0,
                    background=background,
                    fontsize=38,
                ),
                widget.CurrentLayout(
                    font="Expansiva",
                ),
                widget.GroupBox(
                    disable_drag=True,
                    spacing=0,
                    center_aligned=True,
                    active=active,
                    inactive=inactive,
                    highlight_method="block",
                    this_current_screen_border=mark,
                    urgent_border=warning,
                    hide_unused=True,
                    font="Expansiva",
                ),


                widget.Prompt(
                    background=background,
                    font="Expansiva",
                ),
                widget.WindowName(
                    foreground=background,
                    font="Expansiva",
                    # background="#000000",
                ),
                # widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                # ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),


                widget.TextBox(
                    text=left_triangle,
                    foreground=red,
                    padding=0,
                    background=background,
                    fontsize=38,
                ),
                widget.Volume(
                    fmt="Vol: {}",
                    background=red,
                    volume_app="pactl",
                    font="Expansiva",
                ),
                ######################################################
                widget.TextBox(
                    text=left_triangle,
                    foreground=green,
                    padding=0,
                    background=red,
                    fontsize=38,
                ),
                widget.BatteryIcon(
                    background=green,
                ),
                widget.Battery(
                    notify_below=20,
                    format="{char}",
                    charge_char="⬆",
                    background=green,
                    discharge_char="⬇",
                    update_interval = 5,
                    font="Expansiva",
                ),
                widget.Battery(
                    notify_below=20,
                    format="{percent:2.1%} {hour:d}:{min:02d}",
                    background=green,
                    font="Expansiva",
                ),
                #####################################################
                widget.TextBox(
                    text=left_triangle,
                    foreground=yellow,
                    padding=0,
                    background=green,
                    fontsize=38,
                ),
                widget.Clock(
                    format="%d.%m",
                    background=yellow,
                    font="Expansiva",
                ),
                #######################################################
                widget.TextBox(
                    text=left_triangle,
                    foreground=blue,
                    padding=0,
                    background=yellow,
                    fontsize=38,
                ),
                widget.Clock(
                    format="%a %I:%M %p",
                    background=blue,
                    font="Expansiva",
                ),
                widget.TextBox(
                    text=left_triangle,
                    foreground=purple,
                    padding=0,
                    background=blue,
                    fontsize=38,
                ),
                widget.Systray(
                    background=purple,
                    icon_size=10,
                ),
                widget.TextBox(
                    text=" ",
                    background=purple,
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

                #####################################################

                # widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                # widget.QuickExit(),
            ],
            20,
            # margins=[2, 0, 0, 0],
            # border_width=[4, 0, 4, 0],
            # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            opacity=0.8,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Script


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])