import pyautogui
pyautogui.PAUSE = 1

width, height = pyautogui.size()

# マウスを移動する
for i in range(2):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

# マウスのポジションを取得
print(pyautogui.position())

# 座標の色を取得する
im = pyautogui.screenshot()
print(im.getpixel((50, 200)))
