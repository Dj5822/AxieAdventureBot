import pyautogui
import time
import random
import admin


def get_random_time():
    return 0.1 + random.randint(-100, 100) / 1000


def select_cards():
    # Detect the position of all the attack cards.
    detected = []
    detected.extend(list(pyautogui.locateAllOnScreen("battle/carrotHammer.png", confidence=0.97)))
    detected.extend(list(pyautogui.locateAllOnScreen("battle/carrotSlap.png", confidence=0.97)))
    detected.extend(list(pyautogui.locateAllOnScreen("battle/pricklyTrap.png", confidence=0.97)))
    detected.extend(list(pyautogui.locateAllOnScreen("battle/riskyFish.png", confidence=0.97)))
    detected.extend(list(pyautogui.locateAllOnScreen("battle/shellJab.png", confidence=0.97)))
    detected.extend(list(pyautogui.locateAllOnScreen("battle/starShuriken.png", confidence=0.97)))
    detected.extend(list(pyautogui.locateAllOnScreen("battle/swiftEscape.png", confidence=0.97)))
    detected.extend(list(pyautogui.locateAllOnScreen("battle/upstreamSwim.png", confidence=0.97)))
    detected.extend(list(pyautogui.locateAllOnScreen("battle/vegetableBite.png", confidence=0.97)))

    for card_position in detected:
        x = random.randint(card_position.left, card_position.left + card_position.width)
        y = random.randint(card_position.top, card_position.top + card_position.height)
        pyautogui.moveTo(x, y, get_random_time(), pyautogui.easeOutQuad)
        pyautogui.click(clicks=1, interval=get_random_time())


def end_turn():
    x_min = 2244
    x_max = 2505
    y_min = 974
    y_max = 1053
    x = random.randint(x_min, x_max)
    y = random.randint(y_min, y_max)
    pyautogui.moveTo(x, y, get_random_time(), pyautogui.easeOutQuad)
    pyautogui.click(clicks=1, interval=get_random_time())


def turn_started():
    position = pyautogui.locateOnScreen("battle/endTurn.png", confidence=0.97)
    if position is None:
        return False
    else:
        return True


def check_victory():
    position = pyautogui.locateOnScreen("battle/victory.png", confidence=0.97)
    if position is None:
        return False
    else:
        return True


def find_start():
    position = pyautogui.locateOnScreen("battle/start.png", confidence=0.97)
    if position is None:
        return False
    else:
        return True


if not admin.isUserAdmin():
    admin.runAsAdmin()

loop_count = input("Input the number of times you would like to repeat the battle: ")

for i in range(int(loop_count)):
    # adventure menu
    print("starting new battle")
    while not find_start():
        time.sleep(get_random_time() + 0.4)
    position = pyautogui.locateOnScreen("battle/start.png", confidence=0.97)
    x = random.randint(position.left, position.left + position.width)
    y = random.randint(position.top, position.top + position.height)
    pyautogui.moveTo(x, y, get_random_time(), pyautogui.easeOutQuad)
    pyautogui.click(clicks=1, interval=get_random_time())

    # wait for loading screen
    print("waiting for loading screen")
    while not turn_started():
        pyautogui.moveTo(x, y, get_random_time(), pyautogui.easeOutQuad)
        pyautogui.click(clicks=1, interval=get_random_time())
        time.sleep(get_random_time() + 1)

    continue_battle = True

    # the battle loop
    while continue_battle:
        print("turn started")
        print("selecting cards")
        select_cards()
        print("ending turn")
        end_turn()
        print("waiting...")
        while not turn_started():
            time.sleep(get_random_time()+0.4)
            if check_victory():
                print("Victory!")
                continue_battle = False
                pyautogui.click()
                while check_victory():
                    time.sleep(get_random_time() + 0.4)
                    pyautogui.click()
                break
