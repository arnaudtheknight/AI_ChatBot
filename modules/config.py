# Absolute imports, which work for chat programs
from modules.classes import log
from modules.model_list import model_list

def yesno(string, default_yes=True):
    answer = input(string).lower()
    while True:
        if answer in {'yes', 'y'}:
            return True
        elif answer in {'no', 'n'}:
            return False
        elif answer == '':
            return True if default_yes else False
        answer = input(log.Config_Incorrect)

# Pre-chat parameter settings:
def config(valid, valid_edited):
    print(f"\nThe following models can be used for this chat: \n{valid}\n")
    name = str(input("Provide the name of the model you would like to use: "))
    while name.lower() not in (valid_edited or valid):
        name = str(input(log.Config_Incorrect))
    stream = yesno("Would you like the output streamed to the terminal? [Y/n] ", default_yes=True)
    think = yesno("Would you like to enable thinking mode? [y/N] ", default_yes=False)
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

