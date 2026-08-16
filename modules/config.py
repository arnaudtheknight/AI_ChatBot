# Absolute imports, which work for chat programs
from modules.classes import log, log2
from modules.model_list import model_lister

def yesno(string, default_yes=True):
    answer = input(string).lower()
    while True:
        if answer in {'yes', 'y'}:
            return True
        elif answer in {'no', 'n'}:
            return False
        elif answer == '':
            return True if default_yes else False
        answer = input(log2.Config_Prompt_Fail)

# Pre-chat parameter settings:
def configuration(valid, valid_edited):
    print(log2.Config_Model_Show)
    print(f"--> {valid}")
    name = str(input(log2.Config_Model_Prompt))
    while name.lower() not in (valid_edited or valid):
        name = str(input(log2.Config_Prompt_Fail))
    stream = yesno(log2.Config_Mode_Stream, default_yes=True)
    think = yesno(log2.Config_Mode_Think, default_yes=False)
    return name, think, stream

# Name/Main doesn't work, because the absolute imports above raise errors for this file
"""
if __name__ == '__main__':
    models, models_edited = model_list()
    name, think, stream = config(models, models_edited)
    print(f"Name: {name}")
    print(f"Think: {think}")
    print(f"Stream: {stream}")
"""

