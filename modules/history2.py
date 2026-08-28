## Importing modules:
# Quit time:
from datetime import datetime
# Folder gen:
from os.path import isdir
from os import makedirs
# Self-written modules:
from classes import log2, slash
# Global:
from os import getcwd as get_path
from json import JSONDecodeError, load, dump

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
            path # input: /.../history/blah.json
        ]

        for spot in candidates:
            try:
                return get_contents(spot)
            except FileNotFoundError as err:
                print(log2.Importing.Import_Error_404(err))
                # print(f"{log2.WARNING} Failed to open '{log2.UNDER}{err.filename}{log2.RESET}': {err.strerror}.")
                # print(f"Tried opening '{log2.UNDER}{spot}{log2.RESET}' and failed.")
            except JSONDecodeError as err:
                print(f"{log2.WARNING} Failed to open '{log2.UNDER}{spot}{log2.RESET}': {log2.Importing.Import_Filetype}")
        print(log2.Importing.Import_Failure)

# Get exit time:
def quit_handling():
    now = datetime.now()
    stop_d, stop_h, stop_m, stop_s = now.date(), f"{now.hour:02d}", f"{now.minute:02d}", f"{now.second:02d}"
    name = f"{stop_d}-{stop_h}{stop_m}{stop_s}"
    message = f"\n{log2.INFO} Exited on {stop_d} at {stop_h}:{stop_m}:{stop_s}.{log2.RESET} "
    return name, message

# Verify folder existence:
def folder_check(term, root=get_path()):
    folder = f"{root}/{term}"
    if not isdir(folder):
        print(f"{log2.WARNING}'{term}' folder not found. Creating one now.{log2.RESET} ")
        makedirs(folder)
    return folder

def history_export(history):
    filename, message = quit_handling()
    if history:
        path = folder_check(term="history")
        location = f"{path}/hist-{filename}.json"
        try:
            with open(location, 'a') as file:
                dump(history, file, ensure_ascii=False, indent=2)
                print(f"{log2.INFO} Successfully exported history to '{log2.UNDER}{location}{log2.RESET}'. ")
        except Exception as err:
            print(log2.Exporting.Export_Failure)
            print("An exception occured:", err)
        

if __name__ == '__main__':
    history_import()