# Importing modules:
from sys import exit
from os import getcwd as get_path
from json import load, dump
from datetime import datetime
## Self-written:
from modules.classes import log, log2

# Import previous chat history from JSON file:
"""
def history_import():
    root = get_path()
    path = input(f"\nInput path to history file here: \n{root}/")
    if path.lower() not in ('', 'n'):
        path = f"{root}/{path}"
        try:
            with open(path, 'r') as file:
                content = load(file)
            print(log.Hist_Import_Success)
            return content
        except FileNotFoundError:
            exit(log.Hist_Import_Missing)
    else:
        print(log.Hist_Import_Empty)
        return []
"""
        
def history_import():
    root = get_path()
    while True:
        print(log2.Import_Prompt)
        path = input(f"{log2.UNDER}{root}/{log2.RESET}") # [./]history/blah.json
        if path.lower() in {'', 'n'}:
            print(log2.Import_Skipped)
            return []
        else:
            path = f"/{path}"
        candidates = [
            f"{root}{path}", # [root/]history/blah.json
            f"{root}/history{path}", # [root/history/]blah.json
            path # ~/.../history/blah.json
        ]
        for spot in candidates:
            try:
                with open(spot, 'r') as file:
                    content = load(file)
                print(log.Hist_Import_Success)
                return content
            except FileNotFoundError:
                print(f"Tried opening '{log2.UNDER}{spot}{log2.RESET}' and failed.")
        print(log2.Import_Failed)

# Export this chat as JSON file:
def history_export(history):
    root = get_path()
    now = datetime.now()
    stop_d, stop_h, stop_m, stop_s = now.date(), f"{now.hour:02d}", f"{now.minute:02d}", f"{now.second:02d}"
    stop = f"{stop_d}-{stop_h}{stop_m}{stop_s}"
    name1, name2, name_true = f"{root}/history/hist-{stop}.json", f"{root}/hist-{stop}.json", None
    for name in (name1, name2):
        try:
            with open(name, 'a') as file:
                dump(history, file, ensure_ascii=False, indent=2)
            name_true = name
            break
        except Exception:
            print(log2.Export_Failure)
            print(log2.Export_Alternative)
    print(f"\n{log2.INFO} Exited on {stop_d} at {stop_h}:{stop_m}:{stop_s}.{log2.RESET} ")
    exit(f"{log2.INFO} Exported to {log2.UNDER}{name_true}.{log2.RESET} ")

"""
Points of improvement:
- Export:
    - Do not export empty history
- Import:
    - History imports full AND last two split
"""