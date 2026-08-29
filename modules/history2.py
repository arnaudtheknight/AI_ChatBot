## Importing modules:
# Quit time:
from datetime import datetime
# Folder gen:
from os.path import isdir
from os import makedirs
# Self-written modules:
from modules.classes import log2, slash
# Global:
from os import getcwd as get_path
from json import JSONDecodeError, load, dump
from sys import exit

# Obtain file contents:
def get_contents(path):
    with open(path, 'r') as file:
        content = load(file)
        print(log2.Importing.Import_Success)
        return content

# History import logic:
def history_import(root=get_path()):
    while True:
        print(log2.Importing.Import_Prompt)
        path = input(f"{log2.UNDER}{root}/{log2.RESET}") # [/.../]history/blah.json

        # Skip import:
        if path.lower() in slash.History_Skip:
            print(log2.Importing.Import_Skipped)
            return []

        candidates = [
            f"{root}/{path}", # input: history/blah.json
            f"{root}/history/{path}", # input: blah.json
            f"/{path}" # input: /.../history/blah.json
        ]

        for spot in candidates:
            try:
                return get_contents(spot)
            except FileNotFoundError as err:
                print(f"{log2.Importing.Import_Error(spot)} {err.strerror}. ")
            except JSONDecodeError as err:
                print(log2.Importing.Import_Error(spot), log2.Importing.Import_Error_JSON)
        print(log2.Importing.Import_Failure)

# Get exit time:
def quit_handling():
    now = datetime.now()
    stop_d, stop_h, stop_m, stop_s = now.date(), f"{now.hour:02d}", f"{now.minute:02d}", f"{now.second:02d}"
    name = f"{stop_d}-{stop_h}{stop_m}{stop_s}"
    message = f"{log2.INFO} Exited on {stop_d} at {stop_h}:{stop_m}:{stop_s}.{log2.RESET} "
    return name, message

# Verify folder existence:
def folder_check(term, root=get_path()):
    path = f"{root}/{term}"
    if not isdir(path):
        print(log2.Exporting.Export_FolderMissing(term))
        makedirs(path)
    return path

def history_dump(content, path):
    with open(path, 'x') as file:
        dump(content, file, ensure_ascii=False, indent=2)
    print(log2.Exporting.Export_Success(path))

def history_export(history):
    filename, message = quit_handling()
    if history:
        path = folder_check(term="history")
        location1, location2 = f"{path}/hist-{filename}.json", f"{path}/hist-{filename}_02.json"
        for location in {location1, location2}:
            try:
                history_dump(history, f"{path}/hist-2026-08-29-001820.json")
                return exit(message)
            except FileExistsError as err:
                print(log2.Exporting.Export_Error(err.filename))
            except Exception as err:
                print(log2.Exporting.Export_Error(location))
                print("An exception occured:", err)
            print(log2.Exporting.Export_Alternative)
        print(log2.Exporting.Export_Failure)
    else:
        print(log2.Exporting.Export_Empty)
    exit(message)