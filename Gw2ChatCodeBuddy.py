# add admin check / notification

import pyperclip
import time
import win32com.client
import codecs
import requests
import os
import base64

from globalhotkeys import GlobalHotKeys
from decimal import Decimal
from key_define import PressKey, ReleaseKey

# VERSION
version = "4.5"
shell = win32com.client.Dispatch("WScript.Shell")
os.system('mode con: cols=93 lines=40')


def hit_enter():
    PressKey(0x1c)
    ReleaseKey(0x1c)

def paste():
    PressKey(0x1D)
    PressKey(0x2F)
    time.sleep(0.05)
    ReleaseKey(0x1D)
    ReleaseKey(0x2F)

def logo():
    print("                  -::/://:::+sdss+:/so////+osssssssso+")
    print("               ` .//+:-++++osydsooso+/+//+soossssssyyy")
    print("              `:`:///-+o+ooyydhssysssso-   .+sooosssyy")
    print("              `//::/oo/:+ysy+odyyyyyyo-:.    -+oossyys")
    print("               :/:/+/.-osyys/s:yyyyssooyyo/. `:ssyyyyy")
    print("             `+o/:-:/+oysyyod/+hhhhhyhhhhys/. `syhdhso")
    print("      :`  - .ohso++osyyssooshoyddddohddyso`    -hdhhyh")
    print("      +o.`dsdhydhyhdy:./yy+hdyyddd-  :o/-`     `syhddd")
    print("      `:ohmhmmdhddo+-  +yosydsydd-             .+ddddd")
    print("      .sydymNNdy.``   `hhy/.hhhm+               :ddddd")
    print("       :ydmdy/`       +dy. `osdNs.             .hddddh")
    print("         `-:-       `+h:   -/omNdh+``         `:ymddhh")
    print("                `-/+:.    `:+so+`   `.        +dddddhy")
    print("         ````.-:/.                         `odmddhyhhy")
    print("   ___ _         _    ___         _     ___         _    _      ")
    print("  / __| |_  __ _| |_ / __|___  __| |___| _ )_  _ __| |__| |_  _ ")
    print(" | (__| ' \/ _` |  _| (__/ _ \/ _` / -_) _ \ || / _` / _` | || |")
    print("  \___|_||_\__,_|\__|\___\___/\__,_\___|___/\_,_\__,_\__,_|\_, |")
    print("                                                           |__/ ")
logo()
print("Checking for updates...")

# check for update
try:
    response = requests.get('https://github.com/m10x/Gw2ChatCodeBuddy/blob/master/version.txt')
    index = response.text.index("buddyversion")
    versionNewest = response.text[index+14:index+17]

    if (Decimal(version) < Decimal(versionNewest)):
        versionCheck = "\nA newer version is available at: https://github.com/m10x/Gw2ChatCodeBuddy/releases/tag/"+versionNewest+"\n"
    else:
        versionCheck = ("\nVersion "+version+". You are up-to-date. :)\n")
except:
    versionCheck = "Couldn't check for updates :/... Please check your firewall / internet connection and restart :)"

listButtons = ["F1", "F2", "F3", "F4", "F5", "F6",
               "F7", "F8", "F9", "F10", "F11"]
listCodes = ["Not assigned"] * 11
listCodesShow = ["Not assigned"] * 11

def button_assignmend():
    print("F1: " + listCodesShow[0] + "\nF2: " + listCodesShow[1] + "\nF3: "
          + listCodesShow[2] + "\nF4: " + listCodesShow[3] + "\nF5: "
          + listCodesShow[4] + "\nF6: " + listCodesShow[5] + "\nF7: "
          + listCodesShow[6] + "\nF8: " + listCodesShow[7] + "\nF9: "
          + listCodesShow[8] + "\nF10: " + listCodesShow[9] + "\nF11: "
          + listCodesShow[10] + "\nP: Pause Hotkeys and reactivate Console")

def save_to_file():
    print("Saving config to .\gw2chatcodebuddy.config")
    try:
        f = open("gw2chatcodebuddy.config", "w+")
        for x in range(0, len(listButtons)):
            tmpString = ("{};{};{}\n").format(listButtons[x],
                                              listCodes[x],
                                              listCodesShow[x])
            f.write(tmpString)
    except:
        print("Failed to write to .\gw2chatcodebuddy.config")
    finally:
        f.close()

def load_from_file():
    try:
        f = open("gw2chatcodebuddy.config", "r")
        lines = f.readlines()
    except:
        print("Couldn't open .\gw2chatcodebuddy.config")
    finally:
        f.close()
    for line in lines:
        config = line.split(";")
        assign_button(config[0], config[2][:-1], config[1], True)
    print("Successfully loaded config from .\gw2chatcodebuddy.config")
    button_assignmend()


def assign_button(button, itemname, itemcode, loading=False):
    if (not loading):
        anzahl = 0
        while 1 > anzahl or 250 < anzahl:
            try:
                anzahl = int(input("How much of "+itemname+" (1-250)?\n"))
            except:
                print("Invalid Input")
        listCodes[(button - 1)] = str(calculate(anzahl, itemcode))
        listCodesShow[(button - 1)] = str(anzahl) + " " + itemname
    else:
        index = listButtons.index(button)
        listCodes[index] = itemcode
        listCodesShow[index] = itemname
    if button == 1 or button == "F1":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F1)
        def f1():
            pyperclip.copy(listCodes[0])
            spam()
    elif button == 2 or button == "F2":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F2)
        def f2():
            pyperclip.copy(listCodes[1])
            spam()
    elif button == 3 or button == "F3":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F3)
        def f3():
            pyperclip.copy(listCodes[2])
            spam()
    elif button == 4 or button == "F4":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F4)
        def f4():
            pyperclip.copy(listCodes[3])
            spam()
    elif button == 5 or button == "F5":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F5)
        def f5():
            pyperclip.copy(listCodes[4])
            spam()
    elif button == 6 or button == "F6":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F6)
        def f6():
            pyperclip.copy(listCodes[5])
            spam()
    elif button == 7 or button == "F7":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F7)
        def f7():
            pyperclip.copy(listCodes[6])
            spam()
    elif button == 8 or button == "F8":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F8)
        def f8():
            pyperclip.copy(listCodes[7])
            spam()
    elif button == 9 or button == "F9":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F9)
        def f9():
            pyperclip.copy(listCodes[8])
            spam()
    elif button == 10 or button == "F10":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F10)
        def f10():
            pyperclip.copy(listCodes[9])
            spam()
    elif button == 11 or button == "F11":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F11)
        def f11():
            pyperclip.copy(listCodes[10])
            spam()
    """ F12 NOT WORKING???
    elif button == 12 or button == "F12":
        @GlobalHotKeys.register(GlobalHotKeys.VK_F12)
        def f12():
            pyperclip.copy(listCodes[11])
            spam()
    """


def calculate(amount, itemcode):
    # calculate chat code
    # itemcode from base64 to hex
    hex_itemcode = base64.b64decode(itemcode).hex()
    # amount to hex
    hex_amount = '{0:02x}'.format(int(amount))
    # calculate item + amount
    hexa = hex_itemcode[:2] + hex_amount + hex_itemcode[4:]
    # encode to base64
    b64 = codecs.encode(codecs.decode(hexa, 'hex'), 'base64').decode()
    # Next 2 lines to remove \n from b64
    strb64 = str(b64)
    strb64 = strb64[:-1]
    return "[&"+strb64+"]"


def spam():
    shell.AppActivate("Guild Wars 2")  # Gw2Focus
    hit_enter()
    paste()
    hit_enter()

def liorkp(button):
    inputUser = 10
    while 0 > inputUser or 8 < inputUser:
        try:
            inputUser = int(input("What do you want to add? LI/LD(0), W1 KP(1), W2 KP(2), W3 KP(3), W4 KP(4), W5 KP(5), W6 KP(6)\nFractals(7), Custom(8)\n"))
        except:
            print("Invalid Input")

        # LI or LD
        if inputUser == 0:
            inputUser = 10
            while 0 > inputUser or 2 < inputUser:
                try:
                    inputUser = int(input("Legendary Insight (1), Legendary Divination (2), Return (0)\n"))
                except:
                    print("Invalid Input")
                if inputUser == 0:
                    inputUser = 10
                    break
                elif inputUser == 1:
                    assign_button(button, "Legendary Insight", "[&AgH2LQEA]")
                elif inputUser == 2:
                    assign_button(button, "Legendary Divination", "[&AgGlWQEA]")


        # W1 KPs
        elif inputUser == 1:
            inputUser = 10
            while 0 > inputUser or 3 < inputUser:
                try:
                    inputUser = int(input("Vale Guardian (1), Gorseval (2), Sabetha (3), Return (0)\n"))
                except:
                    print("Invalid Input")
                if inputUser == 0:
                    inputUser = 10
                    break
                elif inputUser == 1:
                    assign_button(button, "Vale Guardian KP", "[&AgGJLwEA]")
                elif inputUser == 2:
                    assign_button(button, "Gorseval KP", "[&AgG3LwEA]")
                elif inputUser == 3:
                    assign_button(button, "Sabetha KP", "[&AgGgLwEA]")

        # W2 KPs
        elif inputUser == 2:
            inputUser = 10
            while 0 > inputUser or 2 < inputUser:
                try:
                    inputUser = int(input("Slothasor (1), Matthias (2), Return (0)\n"))
                except:
                    print("Invalid Input")
                if inputUser == 0:
                    inputUser = 10
                    break
                elif inputUser == 1:
                    assign_button(button, "Slothasor KP", "[&AgGKLwEA]")
                elif inputUser == 2:
                    assign_button(button, "Matthias KP", "[&AgFvLwEA]")

        # W3 KPs
        elif inputUser == 3:
            inputUser = 10
            while 0 > inputUser or 3 < inputUser:
                try:
                    inputUser = int(input("Escort (1), Keep Construct (2), Xera (3), Return (0)\n"))
                except:
                    print("Invalid Input")
                if inputUser == 0:
                    inputUser = 10
                    break
                elif inputUser == 1:
                    assign_button(button, "Escort KP", "[&AgFtNAEA]")
                elif inputUser == 2:
                    assign_button(button, "Keep Construct KP", "[&AgE2NAEA]")
                elif inputUser == 3:
                    assign_button(button, "Xera KP", "[&AgFeNAEA]")

        # W4 KPs
        elif inputUser == 4:
            inputUser = 10
            while 0 > inputUser or 4 < inputUser:
                try:
                    inputUser = int(input("Cairn (1), Mursaat Overseer (2), Samarog (3), Deimos (4), Return (0)\n"))
                except:
                    print("Invalid Input")
                if inputUser == 0:
                    inputUser = 10
                    break
                elif inputUser == 1:
                    assign_button(button, "Cairn KP", "[&AgHvOgEA]")
                elif inputUser == 2:
                    assign_button(button, "Mursaat Overseer KP", "[&AgGNOQEA]")
                elif inputUser == 3:
                    assign_button(button, "Samarog KP", "[&AgHXOAEA]")
                elif inputUser == 4:
                    assign_button(button, "Deimos KP", "[&AgGeOgEA]")

        # W5 KPs
        elif inputUser == 5:
            inputUser = 10
            while 0 > inputUser or 4 < inputUser:
                try:
                    inputUser = int(input("Soulless Horror (1), River of Souls (2), Statues of Grenth (3), Voice in the Void (4), Return (0)\n"))
                except:
                    print("Invalid Input")
                if inputUser == 0:
                    inputUser = 10
                    break
                elif inputUser == 1:
                    assign_button(button, "Soulless Horror KP", "[&AgHpTwEA]")
                elif inputUser == 2:
                    assign_button(button, "River of Souls KP", "[&AgEZTwEA]")
                elif inputUser == 3:
                    assign_button(button, "Statues of Grenth KP", "[&AgEoTwEA]")
                elif inputUser == 4:
                    assign_button(button, "Voice in the Void KP", "[&AgGBTgEA]")

        # W6 KPs
        elif inputUser == 6:
            inputUser = 10
            while 0 > inputUser or 3 < inputUser:
                try:
                    inputUser = int(input("Conjured Amalgamate (1), Twin Largos (2), Qadim (3), Return (0)\n"))
                except:
                    print("Invalid Input")
                if inputUser == 0:
                    inputUser = 10
                    break
                elif inputUser == 1:
                    assign_button(button, "Conjured Amalgamate KP", "[&AgHfWQEA]")
                elif inputUser == 2:
                    inputUser = 10
                    while 0 > inputUser or 4 < inputUser:
                        try:
                            inputUser = int(input("Token (1), Bronze Trophy (2), Silver Trophy (3), Gold Trophy (4), Return (0)\n"))
                        except:
                            print("Invalid Input")
                        if inputUser == 0:
                            inputUser = 10
                            break
                        elif inputUser == 1:
                            assign_button(button, "Twin Largos Token", "[&AgEcWwEA]")
                        elif inputUser == 2:
                            assign_button(button, "Bronze Twin Largos Trophy", "[&AgE8WgEA]")
                        elif inputUser == 3:
                            assign_button(button, "Silver Twin Largos Trophy", "[&AgEQWgEA]")
                        elif inputUser == 4:
                            assign_button(button, "Gold Twin Largos Trophy", "[&AgHuWQEA]")
                elif inputUser == 3:
                    assign_button(button, "Qadim KP", "[&AgFFWgEA]")

        # Fractals KPs
        elif inputUser == 7:
            inputUser = 10
            while 0 > inputUser or 1 < inputUser:
                try:
                    inputUser = int(input("100 CM (1), Return (0)\n"))
                except:
                    print("Invalid Input")
                if inputUser == 0:
                    inputUser = 10
                    break
                elif inputUser == 1:
                    assign_button(button, "100 CM KP", "[&AgFPPwEA]")

        # Custom
        elif inputUser == 8:
            try:
                inputChatcode = input("Paste a Chatcode or Return (0)\n")
            except:
                print("Invalid Input")
            if inputChatcode != "0":
                inputChatcodeName = input("Give it a name or Return (0)\n")
                if inputChatcodeName != "0":
                    assign_button(button, inputChatcodeName, inputChatcode)
                else:
                    inputUser = 10
            else:
                inputUser = 10

# P will stop message loop
GlobalHotKeys.register(GlobalHotKeys.VK_P, 0, False)

quitpls = 0
start = 0
while quitpls == 0:
    while start == 0:
        _ = os.system('cls')
        logo()
        print(versionCheck)
        button_assignmend()
        print("Write 1-11 to assign a chatcode to F1-F11, 'g' to start, 's' to save, 'l' to load\n")
        print("'q' to quit\n")

        inputUser = input()
        if inputUser == "s":
            save_to_file()
        if inputUser == "l":
            load_from_file()
        if inputUser == "g":
            start = 1
        elif inputUser == "q":
            start = 1
            quitpls = 1
        elif inputUser == "1":
            liorkp(1)
        elif inputUser == "2":
            liorkp(2)
        elif inputUser == "3":
            liorkp(3)
        elif inputUser == "4":
            liorkp(4)
        elif inputUser == "5":
            liorkp(5)
        elif inputUser == "6":
            liorkp(6)
        elif inputUser == "7":
            liorkp(7)
        elif inputUser == "8":
            liorkp(8)
        elif inputUser == "9":
            liorkp(9)
        elif inputUser == "10":
            liorkp(10)
        elif inputUser == "11":
            liorkp(11)
        """ F12 NOT working???
        elif inputUser == "12":
            liorkp(12)
        """
        # start main loop
        if quitpls == 0 and start == 1:
            start = 0
            GlobalHotKeys.listen()
    start = 1
