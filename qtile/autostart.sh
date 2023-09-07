#!/bin/sh

picom &
xset b off &
nm-applet &
xinput set-prop "$touchpad" "libinput Tapping Enabled" 1 &
xinput set-prop 9 "libinput Tapping Enabled" 1 & 
xinput set-prop 9 "libinput Natural Scrolling Enabled" 1 &
