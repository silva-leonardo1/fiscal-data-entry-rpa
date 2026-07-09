import pyautogui
import pyperclip
import time
import keyboard

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05

# --- DATA ---
data_to_paste = [
    "REQ/001/24 - 123 Fake St, Springfield (general)",
    "REQ/002/24 - 456 Evergreen Terrace (general)",
    "104207/26 - 789 Elm St, Apt 2 (construction)",
    "JUS/157.25 - 101 Maple Ave (general)",
    "003216/26 - 555 Oak Blvd, Suite 10 (infraction)",
    "003214/26 - 777 Pine Rd (infraction)",
    "JUS/00870.26 - 888 Cedar Ln (general)",
    "JUS/00959.26 - 999 Birch Ct (permit)",
    "M/006706/26 - [99123] 111 Walnut Dr (permit)",
    "M/006680/26 - [88456] 222 Cherry Way (general)"
]

# --- CONFIG ---
WAIT_TIME = 5
ACTION_DELAY = 0.1

# --- COLUMNS (1-based) ---
COLUMNS = {
    'request': 3,
    'number': 4,
    'address': 6,
    'permit': 7,
    'sidewalk': 8,
    'apparatus': 9,
    'land': 10,
    'construction': 11,
    'embargo': 12,
    'interdiction': 13,
    'activity interdiction': 14,
    'removal': 15,
    'seizure': 16,
    'infraction': 17,
    'general': 18
}

# --- PARSER ---
def parse_line(item):
    try:
        item = item.strip()

        # grab the type from the parentheses at the end
        type_start = item.rfind("(")
        type_end = item.rfind(")")

        if type_start == -1 or type_end == -1:
            return None

        item_type = item[type_start + 1:type_end].strip().lower()
        remainder = item[:type_start].strip()

        if " - " not in remainder:
            return None

        req_id, remainder = remainder.split(" - ", 1)
        number = None

        # check if there's a [number] tag
        if remainder.startswith("["):
            close_bracket = remainder.find("]")
            if close_bracket != -1:
                number = remainder[1:close_bracket].strip()
                remainder = remainder[close_bracket + 1:].strip()

        address = remainder.strip()

        return req_id, number, address, item_type

    except Exception as e:
        print("Error parsing:", e)
        return None

# --- HELPER FUNCS ---
def go_to_column(current_col, target_col):
    for _ in range(target_col - current_col):
        pyautogui.press('tab')
    return target_col

def paste_text(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')

# --- MAIN SCRIPT ---
print(f"Starting in {WAIT_TIME}s...")
print("Leave your cursor on COLUMN 1 of the first row!")
time.sleep(WAIT_TIME)

for i, item in enumerate(data_to_paste):

    # kill switch
    if keyboard.is_pressed('esc'):
        print("Stopped by user.")
        break

    print(f"Processing {i+1}/{len(data_to_paste)}")

    parsed = parse_line(item)

    if not parsed:
        print(f"[ERROR] invalid format: {item}")
        continue

    req_id, number, address, item_type = parsed

    current_col = 1

    # REQUEST
    current_col = go_to_column(current_col, COLUMNS['request'])
    paste_text(req_id)

    # NUMBER
    current_col = go_to_column(current_col, COLUMNS['number'])
    if number:
        paste_text(number)

    # ADDRESS
    current_col = go_to_column(current_col, COLUMNS['address'])
    paste_text(address)

    # TYPE
    item_type = item_type.lower()

    if item_type in COLUMNS:
        current_col = go_to_column(current_col, COLUMNS[item_type])
        pyautogui.write("X")
    else:
        print(f"[WARN] unknown type: {item_type}")

    # move to the next row
    pyautogui.press('home')
    pyautogui.press('enter')
    pyautogui.press('enter')

    time.sleep(ACTION_DELAY)

print("All done.")
input("Press ENTER to exit...")
