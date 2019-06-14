# Gw2 Chat Code Buddy
[![Release](https://img.shields.io/github/release/m10x/gw2chatcodebuddy.svg?color=brightgreen)](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)
[![Github Downloads](https://img.shields.io/github/downloads/m10x/gw2chatcodebuddy/total.svg)](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)
[![Size](https://img.shields.io/badge/size-6.47mb-brightgreen.svg)](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.me/LowkeyFlex)

1. [Introduction](#introduction)
2. [Guide](#guide)
3. [Created using](#created_using)
4. [Changelog](#changelog)

## Introduction <a name="introduction"></a>
You got (good) Raid Experience but you can't get into a raid group because you don't have enough Legendary Insights? :pensive:  
You already killed a Raid Boss but you don't have the Kill Proofs anymore? :persevere:  
You are just lazy and don't want to carry your LIs/LDs and KPs around with you and/or are too lazy to spam it? :smirk:

Then Gw2ChatCodeBuddy is what you need.
It calculates the Chat Code for a certain amount of LIs, LDs, KPs or any other item chat code, copies it to the clipboard and emulates the key strokes "enter" and "left control" + "v" to post it.
You can assign different amounts of LIs/LDs or KPs to the Hotkeys F1-F11.

I'm currently learning Python and i wanted to do a script which may be useful for some people. :)  
I use PyInstaller to pack the script into an executable. So you only have 1 file which you can easily use.

[Download newest release here](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases)

## Guide <a name="guide"></a>
[YouTube Video on how to use :)](https://www.youtube.com/watch?v=TT-YfTw1A1U)

1. Download the latest release from [here](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/releases) (as .exe)
2. Start Gw2ChatCodeBuddy.exe
3. Choose which button to assign
4. Choose LI/LD, any W1-W7 Boss Kill Proof, Fractal 100cm Kill Proof or paste codes from the wiki
5. Choose amount
6. Press "g" and enter to start (you can't use the console until you press P to pause the hotkeys)
7. Click into Guild Wars 2
8. Press F1-F11 to post the assigned chat code into the chat / P to pause hotkeys 
9. ...
10. Profit?

You can now save your assignmends to a .config file by writing s and load them by writing g.
By doing that, you can skip the steips 3. to 5. the next time you use it :)

Notes: 
- make sure you are in the right chat and that your chatbox isn't currently open

## Created using <a name="created_using"></a>
[![PyInstaller](http://www.pyinstaller.org/_downloads/c2ec9d3ec62efa36a94f459a8e1454f7/pyinstaller-draft1a-35x35-trans.png)](http://www.pyinstaller.org/)  [PyInstaller](http://www.pyinstaller.org/) - to create executable

[globalhotkeys.py](https://gist.github.com/m10x/a9a2eb296fab2106a5ae7c16b8874a4b) I forged it from [mdavey](https://gist.github.com/mdavey/6d40a89dbc15aefcc8cd) and improved it (it works now also great with python 3) ;)

[key_define.py](https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game) I've found it on stackoverflow and made it PEP8 compliant

## "api-ms-win-crt-runtime-l1-1-0.dll is missing"
install windows updates. you can also get the needed .dll with an update from here:  
https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows  
tested on fresh installed win7 & 10

## Changelog <a name="release_notes"></a>
V5.1 released (13.06.2019)
Thanks to [Keldorb](https://github.com/Keldorb) for the Pull Request!
- added Wing 7 KPs

V5.0 released (01.06.2019)
Thanks for more than 2.000 downloads! :)
- custom hotkeys! Choose now between 57 possible hotkeys!
- option to remove a hotkey assignmend (e.g. if the hotkey can't be used)
- chat "blinking" fix option (only few users had this problem)
- reduced size by more than 30% (by adjusting import statements)
- temporarly save clipboard before activating hotkeys and restoring it afterwards
- more return options
- many bug fixes, code improvements and text changes

V4.5 released (30.04.2019)
- massive code improvements
- bug fixes (largos kp)
- New Feature: save / load your button assignmends to/from a .config file
- New Feature: past chatcodes (custom (8)) from the wiki

V4.1 released (02.04.2019)
Thanks to gespriella for pointing out
- Added different Twin Largos KPs

V4.0 released (15.11.2018)
Thanks to [Keldorb](https://github.com/Keldorb) and [ArisenDrake](https://github.com/ArisenDrake) for their Pull requests!
- added W6 Kill Proofs
- added Legendary Divinations

V3.7 released (05.04.2018)
- added missing W5 KP
- added Fractal 100 CM KP

V3.5 released (03.04.2018)
- added W5 Kill Proofs :)

V3.1 released (01.11.2017)
Thanks to [Friteusenfett](https://github.com/LowkeyFlex/Gw2ChatCodeBuddy/issues/1) for the Feedback :)
- changed escort kill proof
- fixed typo

V3.0 released (26.10.2017)
- implemented KP Chat Codes for each W1-W4 boss :)
- added f10+f11 as hotkeys
- code improvements
- added 32bit Version

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
