''' Todo list:
    Possibility to remap p?
    use jaraco instead of pyperclip? cause of images/efficency etc...
'''

from os import system
from base64 import b64decode
from time import sleep
from requests import get
from pyperclip import copy as pyper_copy, paste as pyper_paste
from codecs import encode as codecs_encode, decode as codecs_decode
from globalhotkeys import GlobalHotKeys
from decimal import Decimal
from key_define import PressKey, ReleaseKey
from natsort import index_natsorted


# VERSION
version = "5.1"
system('mode con: cols=99 lines=40')

listButtons = []
listCodes = []
listStrings = []
timeOut = 0.05
versionCheck = ""
clipboard_tmp = ""


def hit_enter():
    PressKey(0x1c)
    ReleaseKey(0x1c)
    # time.sleep(timeOut) Falls immer noch blinken sollte


def paste():
    PressKey(0x1D)
    PressKey(0x2F)
    sleep(timeOut)
    ReleaseKey(0x1D)
    ReleaseKey(0x2F)


def configure_time():
    global timeOut
    system('cls')
    logo()
    print("Some users may experience this issue.")
    print("To resolve this start this program as admin and/or increase the latency of the key presses")
    print("The standard latency is 0.05. Even minimal changes like 0.06 could maybe solve this problem!")
    print("Please tell me if this helps or if the problem still persists. admin@m10x.de")
    print("Your current latency is {}".format(timeOut))

    try:
        inputUser = input("Write any float or Return(0)\n")
    except:
        print("Invalid Input")
        input("Press Enter to continue")

    if inputUser == "0":
        return
    if is_float(inputUser):
        timeOut = float(inputUser)
        input("The Latency has changed to {}. Press Enter to continue".format(timeOut))
    else:
        print("Invalid Input")
        input("Press Enter to continue")


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


def is_int(value):
    try:
        int(value)
        return True
    except:
        return False


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


def button_assignmend():
    for i in range(len(listButtons)):
        print("{}: {}".format(listButtons[i][3:], listStrings[i]))
    print("Latency: {}".format(timeOut))
    print("\nP: Pause hotkeys and reactivate console")


def save_to_file():
    print("Saving config to .\gw2chatcodebuddy.config")
    try:
        with open("gw2chatcodebuddy.config", "w+") as f:
            f.write("Latency;{}\n".format(timeOut))
            for x in range(0, len(listButtons)):
                tmpString = ("{};{};{}\n").format(listButtons[x],
                                                  listCodes[x],
                                                  listStrings[x])
                f.write(tmpString)
            print("Successfully saved config to .\gw2chatcodebuddy.config")
    except:
        print("Failed to write to .\gw2chatcodebuddy.config")
    input("Press Enter to continue")


def load_from_file():
    try:
        with open("gw2chatcodebuddy.config", "r") as f:
            listButtons.clear()
            listCodes.clear()
            listStrings.clear()
            for line in f:
                config = line.split(";")
                if config[0] == "Latency":
                    global timeOut
                    timeOut = float(config[1].strip())
                else:
                    assign_button(config[0], config[2][:-1], config[1].strip(), True)
            print("Successfully loaded config from .\gw2chatcodebuddy.config")
    except:
        print("Couldn't open .\gw2chatcodebuddy.config")
    input("Press Enter to continue")


def check_in_list(_list, _data):
    try:
        _index = _list.index(_data)
        return _index
    except ValueError:
        return -1


def assign_button(button, itemname, itemcode, loading=False):

    global listButtons, listCodes, listStrings

    if (not loading):
        anzahl = 0
        while 1 > anzahl or 250 < anzahl:
            try:
                anzahl = int(input("How much of "+itemname+" (1-250)?\n"))
            except:
                print("Invalid Input")
                input("Press Enter to continue")
        listIndex = check_in_list(listButtons, button)  # check if button is already assigned
        if (listIndex == -1):
            listButtons.append(button)
            listCodes.append(str(calculate(anzahl, itemcode)))
            listStrings.append(str(anzahl) + " " + itemname)
        else:
            listCodes[listIndex] = str(calculate(anzahl, itemcode))
            listStrings[listIndex] = str(anzahl) + " " + itemname
    else:  # loading from config
        listButtons.append(button)
        listCodes.append(itemcode)
        listStrings.append(itemname)

    # sort lists simultaneously
    sortIndex = index_natsorted(listButtons)
    listButtons = [listButtons[i] for i in sortIndex]
    listCodes = [listCodes[i] for i in sortIndex]
    listStrings = [listStrings[i] for i in sortIndex]

    listIndex = check_in_list(listButtons, button)
    keyValue = GlobalHotKeys.__dict__.get(button)

    @GlobalHotKeys.register(keyValue, button)
    def f1():
        pyper_copy(listCodes[listIndex])  # pyperclip, save to clipboard
        spam()


def calculate(amount, itemcode):
    # calculate chat code
    # itemcode from base64 to hex
    hex_itemcode = b64decode(itemcode).hex()
    # amount to hex
    hex_amount = '{0:02x}'.format(int(amount))
    # calculate item + amount
    hexa = hex_itemcode[:2] + hex_amount + hex_itemcode[4:]
    # encode to base64
    b64 = codecs_encode(codecs_decode(hexa, 'hex'), 'base64').decode()
    # Next 2 lines to remove \n from b64
    strb64 = str(b64)
    strb64 = strb64[:-1]
    return "[&"+strb64+"]"


def spam():
    hit_enter()
    paste()
    hit_enter()


def customHotkey():
    print("F1-11 can't satisfy you? Choose other Keys as Hotkeys:")
    print("0 - 9, A - Z (no P), NUMPAD0 - NUMPAD9, F1-F12")
    print("MULTIPLY, ADD, SEPERATOR, SUBSTRACT, DECIMAL, DIVIDE")
    print("Some Keys might won't work, e.g. when they are already assigned as hotkey from another program\n")
    key = input().strip().upper()
    vkkey = "VK_{}".format(key)
    if GlobalHotKeys.__dict__.get(vkkey) is None:
        input("Invalid input ({}). Press 'Enter' to continue.".format(vkkey))
        return
    liorkp(vkkey)


def liorkp(button):
    inputUser = -1
    while inputUser < 0 or inputUser > 5:  # count of options
        try:
            inputUser = int(input("What do you want to add?\nLI/LD(1), Wings(2), Fractals(3), Custom(4), Remove(5), Return(0)\n"))
        except:
            print("Invalid Input")
            input("Press Enter to continue")

        # Return
        if inputUser == 0:
            return

        # LI or LD
        if inputUser == 1:
            inputUser = -1
            while inputUser < 0 or inputUser > 2:
                try:
                    inputUser = int(input("Legendary Insight (1), Legendary Divination (2), Return (0)\n"))
                except:
                    print("Invalid Input")
                    input("Press Enter to continue")
                if inputUser == 0:
                    inputUser = -1
                    break
                elif inputUser == 1:
                    assign_button(button, "Legendary Insight", "[&AgH2LQEA]")
                elif inputUser == 2:
                    assign_button(button, "Legendary Divination", "[&AgGlWQEA]")

        # Wing KPs
        elif inputUser == 2:
            inputUser = -1
            while inputUser < 0 or inputUser > 7:  # count of wings
                try:
                    inputUser = int(input("W1 KP(1), W2 KP(2), W3 KP(3), W4 KP(4), W5 KP(5), W6 KP(6), W7 KP(7), Return (0)\n"))
                except:
                    print("Invalid Input")
                    input("Press Enter to continue")
            if inputUser == 0:
                inputUser = -1

            # W1 KPs
            elif inputUser == 1:
                inputUser = -1
                while inputUser < 0 or inputUser > 3:
                    try:
                        inputUser = int(input("Vale Guardian (1), Gorseval (2), Sabetha (3), Return (0)\n"))
                    except:
                        print("Invalid Input")
                        input("Press Enter to continue")
                    if inputUser == 0:
                        inputUser = -1
                        break
                    elif inputUser == 1:
                        assign_button(button, "Vale Guardian KP", "[&AgGJLwEA]")
                    elif inputUser == 2:
                        assign_button(button, "Gorseval KP", "[&AgG3LwEA]")
                    elif inputUser == 3:
                        assign_button(button, "Sabetha KP", "[&AgGgLwEA]")

            # W2 KPs
            elif inputUser == 2:
                inputUser = -1
                while inputUser < 0 or inputUser > 2:
                    try:
                        inputUser = int(input("Slothasor (1), Matthias (2), Return (0)\n"))
                    except:
                        print("Invalid Input")
                        input("Press Enter to continue")
                    if inputUser == 0:
                        inputUser = -1
                        break
                    elif inputUser == 1:
                        assign_button(button, "Slothasor KP", "[&AgGKLwEA]")
                    elif inputUser == 2:
                        assign_button(button, "Matthias KP", "[&AgFvLwEA]")

            # W3 KPs
            elif inputUser == 3:
                inputUser = -1
                while inputUser < 0 or inputUser > 3:
                    try:
                        inputUser = int(input("Escort (1), Keep Construct (2), Xera (3), Return (0)\n"))
                    except:
                        print("Invalid Input")
                        input("Press Enter to continue")
                    if inputUser == 0:
                        inputUser = -1
                        break
                    elif inputUser == 1:
                        assign_button(button, "Escort KP", "[&AgFtNAEA]")
                    elif inputUser == 2:
                        assign_button(button, "Keep Construct KP", "[&AgE2NAEA]")
                    elif inputUser == 3:
                        assign_button(button, "Xera KP", "[&AgFeNAEA]")

            # W4 KPs
            elif inputUser == 4:
                inputUser = -1
                while inputUser < 0 or inputUser > 4:
                    try:
                        inputUser = int(input("Cairn (1), Mursaat Overseer (2), Samarog (3), Deimos (4), Return (0)\n"))
                    except:
                        print("Invalid Input")
                        input("Press Enter to continue")
                    if inputUser == 0:
                        inputUser = -1
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
                inputUser = -1
                while inputUser < 0 or inputUser > 4:
                    try:
                        inputUser = int(input("Soulless Horror (1), River of Souls (2), Statues of Grenth (3), Voice in the Void (4), Return (0)\n"))
                    except:
                        print("Invalid Input")
                        input("Press Enter to continue")
                    if inputUser == 0:
                        inputUser = -1
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
                inputUser = -1
                while inputUser < 0 or inputUser > 3:
                    try:
                        inputUser = int(input("Conjured Amalgamate (1), Twin Largos (2), Qadim (3), Return (0)\n"))
                    except:
                        print("Invalid Input")
                        input("Press Enter to continue")
                    if inputUser == 0:
                        inputUser = -1
                        break
                    elif inputUser == 1:
                        assign_button(button, "Conjured Amalgamate KP", "[&AgHfWQEA]")
                    elif inputUser == 2:
                        inputUser = -1
                        while inputUser < 0 or inputUser > 4:
                            try:
                                inputUser = int(input("Token (1), Bronze Trophy (2), Silver Trophy (3), Gold Trophy (4), Return (0)\n"))
                            except:
                                print("Invalid Input")
                                input("Press Enter to continue")
                            if inputUser == 0:
                                inputUser = -1
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

            # W7 KPs
            elif inputUser == 7:
                inputUser = -1
                while inputUser < 0 or inputUser > 3:
                    try:
                        inputUser = int(input("Cardinal Sabir (1), Cardinal Adina (2), Qadim the Peerless (3), Return (0)\n"))
                    except:
                        print("Invalid Input")
                        input("Press Enter to continue")
                    if inputUser == 0:
                        inputUser = -1
                        break
                    elif inputUser == 1:
                        assign_button(button, "Cardinal Sabir's KP", "[&AgGGZAEA]")
                    elif inputUser == 2:
                        assign_button(button, "Cardinal Adina's KP", "[&AgFuZAEA]")
                    elif inputUser == 3:
                        assign_button(button, "Ether Djinn's Token", "[&AgEnZAEA]")

        # Fractals KPs
        elif inputUser == 3:
            inputUser = -1
            while inputUser < 0 or inputUser > 1:
                try:
                    inputUser = int(input("100 CM (1), Return (0)\n"))
                except:
                    print("Invalid Input")
                    input("Press Enter to continue")
                if inputUser == 0:
                    inputUser = -1
                    break
                elif inputUser == 1:
                    assign_button(button, "100 CM KP", "[&AgFPPwEA]")

        # Custom
        elif inputUser == 4:
            try:
                inputChatcode = input("Paste a Chatcode or Return (0)\n")
            except:
                print("Invalid Input")
                input("Press Enter to continue")
            if inputChatcode != "0":
                inputChatcodeName = input("Give it a name or Return (0)\n")
                if inputChatcodeName != "0":
                    assign_button(button, inputChatcodeName, inputChatcode)
                else:
                    inputUser = -1
            else:
                inputUser = -1

        # Remove Button
        elif inputUser == 5:
            global listButtons, listCodes, listStrings
            if listButtons.count(button) == 1:
                index = listButtons.index(button)
                del listButtons[index]
                del listCodes[index]
                del listStrings[index]

                GlobalHotKeys.unregister(GlobalHotKeys.__dict__.get(button))
            else:
                print("{} hasn't been assigned yet!".format(button[3:]))
                input("Press Enter to continue")
            return


def check_for_update():
    global versionCheck
    try:
        response = get('https://raw.githubusercontent.com/m10x/Gw2ChatCodeBuddy/master/version.txt')
        versionNewest = response.text[14:17]

        if (Decimal(version) < Decimal(versionNewest)):
            versionCheck = "\nA newer version is available at: https://github.com/m10x/Gw2ChatCodeBuddy/releases/tag/"+versionNewest+"\n"
        else:
            versionCheck = ("\nVersion "+version+". You are up-to-date. :)\n")
    except:
        versionCheck = "Couldn't check for updates :/... Please check your firewall / internet connection and restart :)"


def main():
    logo()
    print("Checking for updates...")

    # check for update
    check_for_update()

    # P will stop message loop
    GlobalHotKeys.register(GlobalHotKeys.VK_P, "VK_P", 0, False)

    global versionCheck
    quitpls = 0
    start = 0
    while quitpls == 0:
        while start == 0:
            system('cls')
            logo()
            print(versionCheck)
            button_assignmend()
            print("\nWrite 1-11 to assign a chatcode to F1-F11, 'c' for other keys, 's' to save, 'l' to load")
            print("'g' to start, 'q' to quit, when the chatbox only sort of 'blinks' press 'b'\n")

            inputUser = input()
            if inputUser == "s":
                save_to_file()
            elif inputUser == "l":
                load_from_file()
            elif inputUser == "g":
                start = 1
            elif inputUser == "q":
                start = 1
                quitpls = 1
            elif inputUser == "b":
                configure_time()
            elif inputUser == "c":
                customHotkey()
            elif is_int(inputUser) and int(inputUser) > 0 and int(inputUser) < 12:  # F12 not working
                liorkp("VK_F{}".format(inputUser))

            # start main loop
            if quitpls == 0 and start == 1:
                start = 0
                clipboard_tmp = pyper_paste()  # save temporarly current clipboard
                GlobalHotKeys.listen()
                pyper_copy(clipboard_tmp)  # restore clipboard after spamming
        start = 1


if __name__ == '__main__':
    main()
