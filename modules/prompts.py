from modules.classes import log2

def prompt_loop():
    inputs = []
    print(f"Enter your prompt here, or press Ctrl-D to finish: {log2.NEG_GREY}")
    while True:
        try:
            line = str(input())
            inputs.append(line)
        except EOFError:
            print(f"{log2.RESET}\n{log2.PURPLE}END OF LINE.{log2.RESET}")
            break
    prompt = ' \n'.join(inputs)
    return prompt

"""
def prompt_history(history = []):
    if len(history) == 2:
        history1, history2 = history[0], history[1]
        history1_role, history1_content = history1['role'], history1['prompt']
        history2_role, history2_content = history2['role'], history2['content']
        if history2_role == 'user' and history2_content: # last message was from user
            return history2_content
        if (history1_role == 'user' and history2_role == 'assistant' and history2_content == ""):
            return history1_content
    else:
        print("Error retrieving prompt from history. Starting afresh... ")

def prompt_history2(history=[]):
    try:
        history2 = history[-1]
        history2_role = history2['role']
        if history2_role == 'user':
            return history2['prompt']
        history2_content = history2['content']
        try:
            history1 = history[-2]
            history1_role, history1_content = history1['role'], history1['prompt']
            if history1_role == 'user' and not history2_content:
                return history1_content
        except IndexError:
            return history2_content if history2_role == 'user' else None
        print("Error retrieving prompt from history. Starting afresh... ")
        return None
    except IndexError:
        print("Error retrieving prompt from history due to empty history. Starting afresh... ")
        return None
"""

def prompt_history3(history=[]):
    if len(history) == 1:
        history2 = history[-1]
        if history2['role'] == 'user':
            return history2['prompt']
    elif len(history) == 2:
        history1, history2 = history[-2], history[-1]
        history2_content = history2['content'] if 'content' in history2 else history2['prompt']
        if history2['role'] == 'user':
            return history2_content
        if history1['role'] == 'user' and not history2_content:
            return history1['prompt']
    return None

def prompting(previous="", history=[]):
    if previous:
        return previous
    if (prompt_sourced := prompt_history3(history)):
        return prompt_sourced
    return prompt_loop()

"""
if __name__ == "__main__":
    testing = [{'role':'user', 'prompt':"history 1 prompt"}, {'role':'assistant', 'content':""}]
    print(prompting(history=testing))
"""

"""
Points of improvement:
- add handling of previous prompt
    - last role was user
    - last role was assistant, but content is empty
"""