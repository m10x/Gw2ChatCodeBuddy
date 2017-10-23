# Gw2ChatCodeBuddy
[![Release](https://img.shields.io/badge/release-v2.0-brightgreen.svg)](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)
[![Size](https://img.shields.io/badge/size-9.725mb-brightgreen.svg)](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)
[![GW2](https://img.shields.io/badge/gw2-LowkeyFlex.8432-blue.svg)](#)
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.me/LowkeyFlex)

## Introduction
You got (good) Raid Experience but you can't get into a raid group because you don't have enough Legendary Insights? :pensive:  
You already killed a Raid Boss but you don't have the Kill Proofs<sup>1</sup> anymore? :persevere:  
You are just lazy and don't want to carry your LIs and KPs<sup>1</sup> around with you and/or are too lazy to spam it? :smirk:

Then Gw2ChatCodeBuddy is what you need.
It calculates the Chat Code for a certain amount of LIs or KPs<sup>1</sup>, copies it to the clipboard and emulates the key strokes "enter" and "left control" + "v" to post it.

I'm currently learning Python and i wanted to do a script which may be useful for some people. :)  
I use PyInstaller to pack the script into an executable. So you only have 1 file which you can easily use.

[Download newest release here](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)

<sup>1</sup>: Kill Proofs are planned to be added soon

## Guide:
1. Start Gw2ChatCodeBuddy.exe
2. Choose LI from 1-250
3. Click into Guild Wars 2
4. Press F1 to post LI to chat
5. Press Q to quit programm
6. ...
7. Profit?

Notes: 
1. make sure you choose enough seconds to click inside of gw2
2. make sure you are in the right chat but that your chatbox isn't currently open
3. you only need "Gw2ChatCodeBuddy.exe" you can delete "README.md" and "version.txt"

## Currently working @
- Use Hotkey to Post Chatcode instead of timed

## What Features are planned to be added?
- copy chatcode to clipboard without spamming
- add kill proof spam for all bosses w1-w4
- choose multiple stacks of LI

## Build with
[![PyInstaller](http://www.pyinstaller.org/_downloads/pyinstaller-draft1a-35x35-trans.png)](http://www.pyinstaller.org/)  [PyInstaller](http://www.pyinstaller.org/) - to create executable

[globalhotkeys.py](https://gist.github.com/LowkeyFlex/a9a2eb296fab2106a5ae7c16b8874a4b) i forged it from [mdavey](https://gist.github.com/mdavey/6d40a89dbc15aefcc8cd) and improved it (works now also great with python 3.6) ;)

## "api-ms-win-crt-runtime-l1-1-0.dll is missing"
install windows updates. you can also get the needed .dll with an update from here:  
https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows  
tested on fresh installed win7 & 10

## Release notes:
V2.0 release (23.10.2017)
- removed time based spam
- added hotkey "F1" to post and "Q" to quit

V1.2 released (20.10.2017) # I had to take a ~2month break because of studying
- bug fix
- small improvement

V1.1 released (10.08.2017)
- automatically check for new version

V1.0 released (09.08.2017)
