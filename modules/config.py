# Imports:
## Self-written:
from modules.classes import log2
from modules.model_list import list_models

# Yes/No input logic:
def yesno(string, default=True):
    choice = log2.Config.Default_Yes if default else log2.Config.Default_No
    while True:
        answer = input(f"{string} {choice}").lower()
        if answer in {"yes", 'y'}:
            return True
        elif answer in {"no", 'n'}:
            return False
        elif answer == '':
            return True if default else False

# Pre-chat parameter settings:
def model_config(official, edited):
    print(log2.Config.Model_List)
    for model in official: print(f"--> {model}")
    name = input(log2.Config.Model_Prompt)
    while (name not in official) and (name.lower() not in edited):
        name = input(log2.Config.Model_Fail)
    stream = yesno(log2.Config.Mode_Stream, default=False)
    think = yesno(log2.Config.Mode_Think, default=True)
    return name, think, stream

# Note: this file will not run as is: module import will break
if __name__ == '__main__':
    models, models_edited = list_models()
    name, think, stream = model_config(models, models_edited)
    print(f"Name: {name}")
    print(f"Think: {think}")
    print(f"Stream: {stream}")
