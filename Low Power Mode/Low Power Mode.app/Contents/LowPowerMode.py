import math
import subprocess


def main():
    # TO-DO: brightness(√), KB backlight(√), dnd(√), mute(√), bt(√), wifi(x), clock(x), gpu(x)

    # ------CONFIGURATION----------
    BuiltInScreenBrightness = True
    DoNotDisturb = True
    MuteVolume = True
    KeyboardBacklight = True
    Bluetooth = True
# -----------------------------

    LowPowerModeState = getLowPowerModeState()
    btest = getBuiltInDisplayBrightness()
    kbbtest = getKeyboardBacklightBrightness()
    bttest = getBluetoothState()
    if LowPowerModeState:
        resetLowPowerModeState()
        if BuiltInScreenBrightness:
            resetBuiltInDisplayBrightness()
        if DoNotDisturb:
            resetSystemDoNotDisturbState()
        if MuteVolume:
            resetMutedVolume()
        if KeyboardBacklight:
            resetKeyboardBacklightBrightness()
        if Bluetooth:
            resetBluetoothState()

    else:
        setLowPowerModeState()
        if BuiltInScreenBrightness:
            setBuiltInDisplayBrightness()
        if DoNotDisturb:
            setSystemDoNotDisturbState()
        if MuteVolume:
            setMutedVolume()
        if KeyboardBacklight:
            setKeyboardBacklightBrightness()
        if Bluetooth:
            setBluetoothState()


# -----------------------------

def getLowPowerModeState():
    process = subprocess.Popen(
        ['osascript', '-e', 'tell application "BetterTouchTool" to get_number_variable "LowPowerMode"'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    stri = (out.decode('utf-8').strip())
    if stri == 'missing value':
        LowPowerModeState = False
    else:
        LowPowerModeState = bool(float(out.decode('utf-8').strip()))
    print("LowPowerModeState", LowPowerModeState)
    return LowPowerModeState


def setLowPowerModeState():
    subprocess.call(['open', "btt://set_number_variable/?variableName=LowPowerMode&to=1"])
    print("LPM to true")


def resetLowPowerModeState():
    subprocess.call(['open', "btt://set_number_variable/?variableName=LowPowerMode&to=0"])
    print("LPM to false")


# -----------------------------


def getBuiltInDisplayBrightness():
    process = subprocess.Popen(
        ['osascript', '-e', 'tell application "BetterTouchTool" to get_number_variable "BuiltInDisplayBrightness"'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    BuiltInDisplayBrightness = float(out.decode('utf-8').strip())
    print("BuiltInDisplayBrightness", BuiltInDisplayBrightness)
    return BuiltInDisplayBrightness


def getOldBuiltInDisplayBrightness():
    process = subprocess.Popen(
        ['osascript', '-e', 'tell application "BetterTouchTool" to get_string_variable "OldBuiltInDisplayBrightness"'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    stri = out.decode('utf-8').strip()
    if stri == 'missing value':
        print("OldBrightness missing value")
        OldBuiltInDisplayBrightness = getBuiltInDisplayBrightness()
    else:
        OldBuiltInDisplayBrightness = float(out.decode('utf-8').strip())
    print("OldBuiltInDisplayBrightness", OldBuiltInDisplayBrightness)
    return OldBuiltInDisplayBrightness


def setBuiltInDisplayBrightness():
    brightness = getBuiltInDisplayBrightness()
    btt = 'tell application "BetterTouchTool" to set_string_variable "OldBuiltInDisplayBrightness" to"' + str(
        brightness) + '"'
    process = subprocess.Popen(
        ['osascript', '-e', btt],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    steps = 0
    if brightness >= 0.17:
        steps = math.floor(brightness / 0.0595703125) - 1
    print(steps)
    for i in range(0, steps):
        subprocess.call(['open', 'btt://trigger_named/?trigger_name=DISPLAY_BRIGHTNESS_DOWN'])
    # subprocess.call(['open', "btt://set_string_variable/?variableName=BuiltInDisplayBrightness&to=0.103515625"])

    print("setBuiltInDisplayBrightness")


def resetBuiltInDisplayBrightness():
    brightness = getBuiltInDisplayBrightness()
    if brightness <= 0.18:
        oldBrightness = getOldBuiltInDisplayBrightness()
        steps = math.floor((oldBrightness) / 0.0595703125) - 1
        for i in range(0, steps):
            subprocess.call(['open', 'btt://trigger_named/?trigger_name=DISPLAY_BRIGHTNESS_UP'])
    print("resetBuiltInDisplayBrightness")


# -----------------------------


def getMutedVolume():
    process = subprocess.Popen(
        ['osascript', '-e', 'output muted of (get volume settings)'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    stri = str((out.decode('utf-8').strip()))
    MutedVolume = False
    if (stri == 'true'):
        MutedVolume = True
    print("MutedVolume", MutedVolume)
    return MutedVolume


def getOldMutedVolume():
    process = subprocess.Popen(
        ['osascript', '-e', 'tell application "BetterTouchTool" to get_string_variable "OldMutedVolume"'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    stri = out.decode('utf-8').strip()
    OldMutedVolume = False
    if stri == 'True':
        OldMutedVolume = True
    print("OldMutedVolume", OldMutedVolume)
    return OldMutedVolume


def setMutedVolume():
    MV = getMutedVolume()
    btt = 'tell application "BetterTouchTool" to set_string_variable "OldMutedVolume" to"' + str(
        MV) + '"'
    process = subprocess.Popen(
        ['osascript', '-e', btt],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if not MV:
        process = subprocess.Popen(
            ['osascript', '-e', "set volume with output muted"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        print("setting MutedVolume", out)
    # defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturb -boolean true


def resetMutedVolume():
    MV = getMutedVolume()
    oldMV = getOldMutedVolume()
    if MV:
        if not oldMV:
            process = subprocess.Popen(
                ['osascript', '-e', "set volume without output muted"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()
    print("resetMutedVolume")

    # ---------------------------------


def getSystemDoNotDisturbState():
    process = subprocess.Popen(
        ['osascript', '-e', 'tell application "BetterTouchTool" to get_number_variable "SystemDoNotDisturbState"'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    stri = out.decode('utf-8').strip()
    SystemDoNotDisturbState = bool(int(float(stri)))
    print("SystemDoNotDisturbState", SystemDoNotDisturbState)
    return SystemDoNotDisturbState


def getOldSystemDoNotDisturbState():
    process = subprocess.Popen(
        ['osascript', '-e', 'tell application "BetterTouchTool" to get_string_variable "OldSystemDoNotDisturbState"'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    stri = out.decode('utf-8').strip()
    OldSystemDoNotDisturbState = False
    if stri == 'True':
        OldSystemDoNotDisturbState = True
    print("OldSystemDoNotDisturbState", OldSystemDoNotDisturbState)
    return OldSystemDoNotDisturbState


def setSystemDoNotDisturbState():
    DND = getSystemDoNotDisturbState()
    btt = 'tell application "BetterTouchTool" to set_string_variable "OldSystemDoNotDisturbState" to "' + str(
        DND) + '"'
    process = subprocess.Popen(
        ['osascript', '-e', btt],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    print("DND", out)
    if not DND:
        subprocess.call(['open', "btt://trigger_named/?trigger_name=DND"])
    # defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturb -boolean true


def resetSystemDoNotDisturbState():
    DND = getSystemDoNotDisturbState()
    oldDND = getOldSystemDoNotDisturbState()
    #print("DND: ", DND, " oldDND: ", oldDND)
    if DND:
        if not oldDND:
            subprocess.call(['open', 'btt://trigger_named/?trigger_name=DND'])

    print("resetSystemDoNotDisturbState")


# -----------------------------


def getKeyboardBacklightBrightness():
    proc1 = subprocess.Popen(
        ['ioreg', '-c', 'AppleHIDKeyboardEventDriverV2'], stdout=subprocess.PIPE)
    process = subprocess.Popen(['grep', 'KeyboardBacklightBrightness'], stdin=proc1.stdout,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    stri = out.decode('utf-8').strip()
    KeyboardBacklightBrightness = [int(s) for s in stri.split() if s.isdigit()][0]
    print("KeyboardBacklightBrightness", KeyboardBacklightBrightness)
    return KeyboardBacklightBrightness


def getOldKeyboardBacklightBrightness():
    process = subprocess.Popen(
        ['osascript', '-e',
         'tell application "BetterTouchTool" to get_number_variable "OldKeyboardBacklightBrightness"'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    stri = out.decode('utf-8').strip()
    if stri == 'missing value':
        print("OldKbBrightness missing value")
        OldKeyboardBacklightBrightness = getKeyboardBacklightBrightness()
    else:
        OldKeyboardBacklightBrightness = int(float(out.decode('utf-8').strip()))
    print("OldKeyboardBacklightBrightness", OldKeyboardBacklightBrightness)
    return OldKeyboardBacklightBrightness


def setKeyboardBacklightBrightness():
    kbbrightness = getKeyboardBacklightBrightness()
    btt = 'tell application "BetterTouchTool" to set_number_variable "OldKeyboardBacklightBrightness" to ' + str(
        kbbrightness)
    process = subprocess.Popen(
        ['osascript', '-e', btt],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    steps = 1
    for x in range(1, 17):
        y = round(
            27.50962 + 4.05198 * x + 0.35654 * math.pow(x, 2) + 0.02912 * math.pow(x, 3) - 0.00101 * math.pow(x,
                                                                                                              4) + 0.00010 * math.pow(
                x, 5))
        print(x, y, kbbrightness)
        if y >= kbbrightness:
            steps = x
            break
    for i in range(0, steps):
        subprocess.call(['open', "btt://trigger_named/?trigger_name=KEYBOARD_BACKLIGHT_DOWN"])


def resetKeyboardBacklightBrightness():
    kbbrightness = getKeyboardBacklightBrightness()
    if kbbrightness == 0:
        oldkbbrightness = getOldKeyboardBacklightBrightness()
        steps = 1
        for x in range(1, 17):
            y = round(
                27.50962 + 4.05198 * x + 0.35654 * math.pow(x, 2) + 0.02912 * math.pow(x, 3) - 0.00101 * math.pow(x,
                                                                                                                  4) + 0.00010 * math.pow(
                    x, 5))
            print(x, y, oldkbbrightness)
            if y >= oldkbbrightness:
                steps = x
                break
        for i in range(0, steps):
            subprocess.call(['open', "btt://trigger_named/?trigger_name=KEYBOARD_BACKLIGHT_UP"])


# -----------------------------


def getBluetoothState():
    proc1 = subprocess.Popen(
        ['ioreg', '-c', 'IOBluetoothHostControllerUARTTransport'], stdout=subprocess.PIPE)
    process = subprocess.Popen(['grep', 'DevicePowerState'], stdin=proc1.stdout,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    stri = out.decode('utf-8').strip().replace("=", " = ").replace(",", " , ")
    print("stri: ", stri)
    BluetoothState = bool([int(s) for s in stri.split() if s.isdigit()][0])

    print("BluetoothState", BluetoothState)
    return BluetoothState


def getOldBluetoothState():
    process = subprocess.Popen(
        ['osascript', '-e', 'tell application "BetterTouchTool" to get_string_variable "OldBluetoothState"'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    stri = out.decode('utf-8').strip()
    OldBluetoothState = False
    if stri == 'True':
        OldBluetoothState = True
    print("OldBluetoothState", OldBluetoothState)
    return OldBluetoothState


def setBluetoothState():
    BT = getBluetoothState()
    btt = 'tell application "BetterTouchTool" to set_string_variable "OldBluetoothState" to "' + str(
        BT) + '"'
    process = subprocess.Popen(
        ['osascript', '-e', btt],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if BT:
        subprocess.call(['open', "btt://trigger_named/?trigger_name=BLUETOOTH_OFF"])
    # defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturb -boolean true
    print("setBluetoothState")


def resetBluetoothState():
    BT = getBluetoothState()
    oldBT = getOldBluetoothState()
    if not BT:
        if oldBT:
            subprocess.call(['open', 'btt://trigger_named/?trigger_name=BLUETOOTH_ON'])

    print("resetBluetoothState")


# -----------------------------


if __name__ == '__main__':
    main()
