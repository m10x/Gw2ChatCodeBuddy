# Gw2ChatCodeBuddy
[![Release](https://img.shields.io/badge/release-v3.0-brightgreen.svg)](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)
[![Size](https://img.shields.io/badge/size-9.5mb-brightgreen.svg)](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)
[![GW2](https://img.shields.io/badge/gw2-LowkeyFlex.8432-blue.svg)](#)
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.me/LowkeyFlex)

### 32bit version now available, only use it if you have 32bit windows

## Introduction
You got (good) Raid Experience but you can't get into a raid group because you don't have enough Legendary Insights? :pensive:  
You already killed a Raid Boss but you don't have the Kill Proofs anymore? :persevere:  
You are just lazy and don't want to carry your LIs and KPs around with you and/or are too lazy to spam it? :smirk:

Then Gw2ChatCodeBuddy is what you need.
It calculates the Chat Code for a certain amount of LIs or KPs, copies it to the clipboard and emulates the key strokes "enter" and "left control" + "v" to post it.
You can assign different amounts of LIs or KPs to the Hotkeys F1-F9.

I'm currently learning Python and i wanted to do a script which may be useful for some people. :)  
I use PyInstaller to pack the script into an executable. So you only have 1 file which you can easily use.

[Download newest release here](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)

## Guide:
[YouTube Video on how to use :)](https://www.youtube.com/watch?v=TT-YfTw1A1U)

1. Download the latest release from [here](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases) (as .exe)
2. Start Gw2ChatCodeBuddy.exe
3. Choose which button to assign
4. Choose LI or any W1-W4 Boss Kill Proof
5. Choose amount
6. Press "s" and enter to start (you can't use the console until you press P to pause the hotkeys)
7. Click into Guild Wars 2
8. Press F1-F9 to post LI to chat / P to pause hotkeys 
9. ...
10. Profit?

Notes: 
- make sure you are in the right chat and that your chatbox isn't currently open

## Currently working @
- 32bit version
- different Kill Proofs for each boss especially trio

## What Features are planned to be added
- 32bit version
- different Kill Proofs for each boss
- ~legendary armour codes
- ~more possible hotkeys

## Build with
[![PyInstaller](http://www.pyinstaller.org/_downloads/pyinstaller-draft1a-35x35-trans.png)](http://www.pyinstaller.org/)  [PyInstaller](http://www.pyinstaller.org/) - to create executable

[globalhotkeys.py](https://gist.github.com/LowkeyFlex/a9a2eb296fab2106a5ae7c16b8874a4b) i forged it from [mdavey](https://gist.github.com/mdavey/6d40a89dbc15aefcc8cd) and improved it (works now also great with python 3.6) ;)

## "api-ms-win-crt-runtime-l1-1-0.dll is missing"
install windows updates. you can also get the needed .dll with an update from here:  
https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows  
tested on fresh installed win7 & 10

## Release notes:
V3.0 released (26.10.2017)
- implemented KP Chat Codes for each W1-W4 boss :)
- added f10+f11 as hotkeys
- code improvements

V2.1 released (24.10.2017)
- choose to add li to f1-f9
- exception if offline or blocked by firewall while looking for update

V2.0 released (23.10.2017)
- removed time based spam
- added hotkey "F1" to post and "Q" to quit

V1.2 released (20.10.2017) # I had to take a ~2month break because of studying
- bug fix
- small improvement

V1.1 released (10.08.2017)
- automatically check for new version

V1.0 released (09.08.2017)
