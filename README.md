# Pomodoro Graphical User Interface


## Project Overview
This is a GUI tool utilizing the Pomodoro Technique to aid time management.

## Objectives
- Set up the User Interface
- Create Start Button with utilizing a Countdown Mechanism
- Create Timer Mechanism for breaks
- Create Reset Button with a Reset Timer Mechanism 

## Results
![image](https://github.com/frantzalexander/pomodoro_gui/assets/128331579/a187127d-a41e-48d0-98c0-95262797deec)


## Process

```mermaid
flowchart TD
start(((START)))
ui_setup[User Interface Setup]
window[Create Program Window]
label_stamp[Creat Timer Label & Initial Time Stamp]
checkmark[Create Checkmark Label]
start_reset{Create Start & Reset Buttons}
countdown[Create Countdown Mechanism]
start_timer[Create Start Timer Mechanism]
short[Short Break]
long[Long Break]
work[Work Session]
apply[Apply Checkmark]
timer_reset[Create Timer Reset Mechanism]
reset_timer[Reset Timer Label]
reset_text[Reset Timer Text]
finish(((END)))
start --> ui_setup
ui_setup --> window
window --> label_stamp
label_stamp --> checkmark
checkmark --> start_reset
start_reset -->|Start Button|countdown
countdown --> start_timer
start_timer --> short
short --> long
long --> work
work --> apply
apply --> finish
start_reset --> |Reset Button|timer_reset
timer_reset --> reset_timer
reset_timer --> reset_text
reset_text --> finish
