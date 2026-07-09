# Data Entry Automator

A simple Python automation script to parse formatted text strings and automatically paste the extracted data into specific spreadsheet columns using simulated keystrokes. 

## How it works

The script reads a list of strings formatted like this:
`REQ_ID - [optional_number] Address (type)`

It parses each line to extract the Request ID, Number, Address, and Type. Then, it uses `pyautogui` to tab through columns, paste the relevant data using `pyperclip`, and mark an "X" in the column corresponding to the specific type.

## Requirements

You'll need Python 3 installed, along with a few external libraries. You can install the dependencies using pip:

```bash
pip install pyautogui pyperclip keyboard
```

## How to use

1. Update the `data_to_paste` list in the script with your actual data.
2. Open your spreadsheet or target application.
3. Run the script:
   ```bash
   python automator.py
   ```
4. You have 5 seconds (configurable via `WAIT_TIME`) to click on **COLUMN 1** of the first row where the data should be inserted.
5. Let go of the mouse and keyboard, and watch it work.

## Kill Switch

If something goes wrong or the script gets out of sync, press and hold the **`ESC`** key to stop the execution immediately. There is also a failsafe built into `pyautogui`: if you slam your mouse to any of the 4 corners of your screen, it will throw an exception and stop.

## Notes

* Make sure your system language or spreadsheet settings don't interfere with `Ctrl+V` pasting.
* If the script is moving too fast for your application to register the inputs, increase the `ACTION_DELAY` variable.
