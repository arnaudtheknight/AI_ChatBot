from ollama import chat
# from ollama import RequestError, ResponseError
from modules.classes import log2

def interact(name, history=[], mode_think=False):
    output = chat(
        model = name,
        messages = history,
        stream = False,
        think = mode_think
    )
    return output

def interact_stream(name, history=[], mode_think=False):
    output = chat(
        model = name,
        messages = history,
        stream = True,
        think = mode_think
    )
    return output

"""
Raises RequestError if a model is not provided.
Raises ResponseError if the request could not be fulfilled.
"""

def generate(output, out_think="", out_ans=""):
    if output.message:
        print("Done crunching!") if not (out_think and out_ans) else None
        out_think = output.message.thinking if output.message.thinking else None
        out_ans = output.message.content
    print(f"{log2.NEG_BLUE}Thinking: {log2.RESET}\n{log2.BLUE}{out_think}{log2.RESET}") if out_think else None
    print(f"{log2.NEG_GREEN}Response: {log2.RESET}\n{out_ans}")
    return out_think, out_ans

def generate_stream(output, out_think="", out_ans=""):
    for chunk in output:
        print(f"{log2.NEG_BLUE}Done crunching!{log2.RESET}") if (not out_think and not out_ans) else None
        if chunk.message.thinking:
            print(f"{log2.BLUE}{chunk.message.thinking}{log2.RESET}", end='', flush=True)
            out_think += chunk.message.thinking
        elif chunk.message.content:
            print(f"{log2.NEG_GREEN}Thinking complete!{log2.RESET}") if (out_think and not out_ans) else None
            print(chunk.message.content, end='', flush=True)
            out_ans += chunk.message.content
    return out_think, out_ans
