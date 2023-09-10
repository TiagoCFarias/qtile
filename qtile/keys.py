from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

terminal = guess_terminal()


mod = "mod4"

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
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    

    # Hide or show the bar
    Key([mod], "b", lazy.hide_show_bar(), desc="Hide or show the bar"),
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
    # Key([],"XF86AudioNext", lazy.spawn("mpc next")),
    # Key([],"XF86AudioPrev", lazy.spawn("mpc prev")),
    # Key([],"XF86AudioPlay", lazy.spawn("mpc toggle")),
    Key([],"XF86AudioNext", lazy.spawn("playerctl next")),
    Key([],"XF86AudioPrev", lazy.spawn("playerctl  previous")),
    Key([],"XF86AudioPlay", lazy.spawn("playerctl play-pause")),

    # Keys Related to Brightness
    # xbacklight works only with x
    # Key([], "XF86MonBrightnessUp", lazy.spawn(
    #    "xbacklight -inc 10")),
    # Key([], "XF86MonBrightnessDown", lazy.spawn(
    #    "xbacklight -dec 10")),
    Key([], "XF86MonBrightnessUp", lazy.spawn(
        "light -A 3")),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
        "light -U 3")),

    # Open program
    Key([mod], "e", lazy.spawn("nautilus")),
    Key([mod, "shift"], "w", lazy.spawn("firefox")),

    # launch rofi to find a program
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Launch rofi"),

    # launch screenshot tool ksnip rectangular area
    Key([mod], "Print", lazy.spawn("ksnip -r"), desc="Select a rectangular area from where to take a screenshot"),

]
