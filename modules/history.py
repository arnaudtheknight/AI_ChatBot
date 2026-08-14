# Importing modules:
from os import getcwd as get_path
from json import load, dump
from datetime import datetime
## Self-written:
from modules.classes import log

# Import previous chat history from JSON file:
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

def history_import2():
    root = get_path()
    while True:
        path = input(f"\nInput path to history file here: \n{root}/") # [./]history/blah.json
        if path.lower() in {'', 'n'}:
            print(log.Hist_Import_Empty)
            return []
        candidates = [
            f"{root}/{path}", # [root/]history/blah.json
            f"{root}/history/{path}", # [root/history/]blah.json
            path # ~/.../history/blah.json
        ]
        for spot in candidates:
            try:
                with open(spot, 'r') as file:
                    content = load(file)
                print(log.Hist_Import_Success)
                return content
            except FileNotFoundError:
                print(f"Tried opening '{spot}' and failed.")
        print("Yeah, no, you oopsied, try again.")

# Export this chat as JSON file:
def history_export(history):
    storage = f"{get_path()}/history"
    stop = datetime.now()
    stop_date, stop_hour, stop_min, stop_sec = stop.date(), f"{stop.hour:02d}", f"{stop.minute:02d}", f"{stop.second:02d}"
    path = f"{storage}/hist-{stop_date}-{stop_hour}{stop_min}{stop_sec}.json"
    try:
        with open(path, 'a') as file:
            dump(history, file, ensure_ascii=False, indent=2)
        print(f"{log.CYAN}[INFO] Exited on {stop_date} at {stop_hour}:{stop_min}:{stop_sec}.{log.END}")
        print(f"{log.CYAN}[INFO] Exported to {log.UNDER}{path}.{log.END}")
    except Exception:
        exit(log.Hist_Export_Fail)
