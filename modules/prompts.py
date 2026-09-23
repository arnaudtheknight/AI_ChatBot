# Imports
## Self-written:
from modules.classes import log2, slash

def prompt_loop():
    inputs = []
    print(f"\nStart typing, or enter \"/done\" to finish: ")
    while True:
        line = str(input(f"{log2. NEG_GREY}>>> "))
        if line.lower() in slash.Chat_STOP:
            print(log2.RESET)
            raise KeyboardInterrupt
        elif line.lower() in slash.Chat_NEXT:
            print(log2.RESET)
            print(f"{log2.PURPLE}END OF LINE.{log2.RESET} ")
            break
        elif line.lower() in slash.Chat_Mistake:
            del inputs[-1]
        elif line.lower() in slash.Chat_Wipe:
            inputs = []
        else:
            inputs.append(line)
    prompt = ' \n'.join(inputs)
    return prompt

"""
def prompt_last(history=[]):
    if len(history) == 1:
        action = history[-1]
        if action['role'] == "user":
            return action['prompt']
    elif len(history) == 2:
        action1, action2 = history[-2], history[-1]
        if action2['role'] == 'user':
            asdasda
        elif action1['role'] == 'user':
            



        if 'content' in action2:
            action2_content = history['content']
        else:
            action2_content = history['prompt']
        if action2['role'] == 
"""

def prompting(previous="", history=[]):
    # if previous:
    #     return previous
    # if (prompt_sourced := prompt_last(history)):
    #     return prompt_sourced
    return prompt_loop()

"""
Points of improvement:
- add handling of previous prompt
"""