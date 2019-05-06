import ctypes
import ctypes.wintypes
import win32con


class GlobalHotKeys(object):

    key_mapping = []
    user32 = ctypes.windll.user32
    MOD_ALT = win32con.MOD_ALT
    MOD_CTRL = win32con.MOD_CONTROL
    MOD_CONTROL = win32con.MOD_CONTROL
    MOD_SHIFT = win32con.MOD_SHIFT
    MOD_WIN = win32con.MOD_WIN


    @classmethod
    def register(cls, vk, keyname, modifier=0, func=None):

        indexof = [i for i, s in enumerate(cls.key_mapping) if vk in s]
        if indexof != []:
            del cls.key_mapping[indexof[0]]

        # Called as a decorator?
        if func is None:
            def register_decorator(f):
                cls.register(vk, keyname, modifier, f)
                return f
            return register_decorator
        else:
            cls.key_mapping.append((vk, keyname, modifier, func))


    @classmethod
    def unregister(cls, vk):  # use vk number to delete from key_mapping
        indexof = [i for i, s in enumerate(cls.key_mapping) if vk in s]
        if indexof != []:
            del cls.key_mapping[indexof[0]]


    @classmethod
    def listen(cls):
        """
        Start the message pump
        """

        for index, (vk, keyname, modifiers, func) in enumerate(cls.key_mapping):
            if not cls.user32.RegisterHotKey(None, index, modifiers, vk):
                # raise Exception('Unable to register hot key: ' + str(vk))
                _ = input("Can't assign {} as hotkey. Press Enter to continue...".format(keyname[3:]))
                for index, (vk, keyname, modifiers, func) in enumerate(cls.key_mapping):
                    cls.user32.UnregisterHotKey(None, index)
                return

        try:
            msg = ctypes.wintypes.MSG()
            while cls.user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    (vk, keyname, modifiers, func) = cls.key_mapping[msg.wParam]
                    if not func:
                        break
                    func()

                cls.user32.TranslateMessage(ctypes.byref(msg))
                cls.user32.DispatchMessageA(ctypes.byref(msg))

        finally:
            for index, (vk, keyname, modifiers, func) in enumerate(cls.key_mapping):
                cls.user32.UnregisterHotKey(None, index)


    @classmethod
    def _include_defined_vks(cls):
        for item in win32con.__dict__:
            item = str(item)
            if item[:3] == 'VK_':
                setattr(cls, item, win32con.__dict__[item])


    @classmethod
    def _include_alpha_vks(cls):
        for key_code in (range(ord('A'), ord('Z') + 1)):
            setattr(cls, 'VK_' + chr(key_code), key_code)


    @classmethod
    def _include_numeric_vks(cls):
        for key_code in (range(ord('0'), ord('9') + 1)):
            setattr(cls, 'VK_' + chr(key_code), key_code)


GlobalHotKeys._include_defined_vks()
GlobalHotKeys._include_alpha_vks()
GlobalHotKeys._include_numeric_vks()
