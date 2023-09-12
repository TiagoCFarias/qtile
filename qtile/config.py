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

from libqtile import layout
from libqtile.config import Click, Drag, Group, Key, Match
from libqtile.lazy import lazy
from libqtile import hook
import os
import subprocess
from gruvbox.gruvbox import *
from theme import *
# import fontawesome as fa

from screens import *
from keys import *


mod = "mod4"



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



# groups = [Group(i) for i in "1234567890"]


def init_group_names():
    return [('1', {"label":"\uf111", "layout": "columns"}),                      # fa.icons['firefox']
            ('2', {"label":"\uf111", "layout": "columns"}),                      # fa.icons['folder']
            ('3', {"label":"\uf111", "layout": "columns"}),                      # fa.icons['java']
            ('4', {"label":"\uf111", "layout": "columns"}),                      # fa.icons['python']
            ('5', {"label":"\uf111", "layout": "columns"}),                      # fa.icons['book']
            ('6', {"label":"\uf111", "layout": "columns"}),                      # fa.icons['image']
            ('7', {"label":"\uf111", "layout": "columns"}),                      # fa.icons['terminal']
            ('8', {"label":"\uf111", "layout": "columns"}),
            ('9', {"label":"\uf111", "layout": "columns"}),
            ]

    # return [('\ue007', {"layout": "columns"}),                      # fa.icons['firefox']
    #         ('\uf07b', {"layout": "columns"}),                      # fa.icons['folder']
    #         ('\uf4e4', {"layout": "columns"}),                      # fa.icons['java']
    #         ('\uf3e2', {"layout": "columns"}),                      # fa.icons['python']
    #         ('\uf02d', {"layout": "columns"}),                      # fa.icons['book']
    #         ('\uf03e', {"layout": "columns"}),                      # fa.icons['image']
    #         ('\uf120', {"layout": "columns"}),                      # fa.icons['terminal']
    #         ('\uf27a', {"layout": "columns"}),
    #         ('\uf1fc', {"layout": "columns"}),
    #         ]


def init_groups():
    return [Group(name, **kwargs) for name, kwargs in init_group_names()]



# if __name__ in ["config", "__main__"]:
group_names = init_group_names()
groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name, switch_group=True)))

# region old
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
# endregion

layouts = [
    # layout.Columns(border_focus_stack=[
    #                "#d75f5f", "#8f3d3d"], border_width=4, margin=5,),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(
        border_width=1,
        margin=[0, 5, 5, 5],
        margin_on_single=0,
    ),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Max(),
]


# screens used to be here

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
