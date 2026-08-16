from classes import log2

def prompting2(previous=""):
    if previous:
        return previous
    contents = []
    while True:
        try:
            prompt = str(input("[Press Ctrl-D to end] Prompt here: "))
            contents.append(prompt)
        except EOFError:
            break
    text = '\n'.join(contents)
    return text

def prompting(previous=""):
    if previous:
        return previous
    inputs = []
    print(f"Enter your prompt here, or press Ctrl-D to finish: \n{log2.NEG_GREY}")
    while True:
        try:
            line = str(input())
        except EOFError:
            print(f"{log2.RESET}{log2.PURPLE}END OF LINE.{log2.RESET}")
            break
    prompt = '\n'.join(inputs)
    return prompt

if __name__ == "__main__":
    print(prompting())

"""
Points of improvement:
- add handling of previous prompt
    - last role was user
    - last role was assistant, but content is empty
"""