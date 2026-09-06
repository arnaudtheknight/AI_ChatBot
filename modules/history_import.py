# Imports:
from os import getcwd as get_path
from json import JSONDecodeError, load
## Self-written modules:
from modules.classes import log2, slash

# Obtain file contents:
def get_contents(path):
    with open(path, 'r') as file:
        content = load(file)
        print(log2.Importing.Success)
        return content

# History import logic:
def history_in(root=get_path()):
    while True:
        print(log2.Importing.Prompt)
        path = input(f"{log2.UNDER}{root}/{log2.RESET}") # [/.../]history/blah.json

        # Skip import:
        if path.lower() in slash.History_Skip:
            print(log2.Importing.Skipped)
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
                print(f"{log2.Importing.Error(spot)} {err.strerror}. ")
            except JSONDecodeError as err:
                print(log2.Importing.Error(spot), log2.Importing.Error_JSON)
            except Exception as err:
                print(f"{log2.FATAL} A fatal error has occured:", err)
        print(log2.Importing.Failure)

# Points of improvement:
"""
- History imports full history AND split of last two messages
"""