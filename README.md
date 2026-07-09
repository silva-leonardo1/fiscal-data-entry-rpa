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
