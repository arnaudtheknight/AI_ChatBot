## Imports:
# Global:
from os import getcwd as get_path
# Quit message:
from datetime import datetime
# Folder gen:
from os.path import isdir
from os import makedirs
# Export:
from json import dump
from sys import exit
# Self-written modules:
from modules.classes import log2

# Get exit time:
def quit_message():
    now = datetime.now()
    stop_d, stop_h, stop_m, stop_s = now.date(), f"{now.hour:02d}", f"{now.minute:02d}", f"{now.second:02d}"
    name = f"{stop_d}-{stop_h}{stop_m}{stop_s}"
    message = f"{log2.INFO} Exited on {stop_d} at {stop_h}:{stop_m}:{stop_s}.{log2.RESET} "
    return name, message

# Verify folder existence:
def folder_check(term, root=get_path()):
    path = f"{root}/{term}"
    if not isdir(path):
        print(log2.Exporting.FolderMissing(term))
        makedirs(path)
    return path

# History file creation:
def history_dump(content, path, overwrite=False):
    operation = 'w' if overwrite else 'x'
    with open(path, operation) as file:
        dump(content, file, ensure_ascii=False, indent=2)
    print(log2.Exporting.Success(path))

# History export logic:
def history_out(history):
    filename, message = quit_message()
    if history:
        path = folder_check(term="history")
        file = f"{path}/{filename}.json"
        try:
            history_dump(history, file)
            return exit(message)
        except FileExistsError as err:
            print(log2.Exporting.Error(err.filename))
            print(log2.Exporting.Alternative)
            history_dump(history, f"{path}/dump.json", overwrite=True)
        except Exception as err:
            print(log2.Exporting.Error(file))
            print("An exception occured:", err) 
    else: 
        print(log2.Exporting.Empty)
    exit(message)