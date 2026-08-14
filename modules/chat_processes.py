from ollama import chat
from ollama import RequestError, ResponseError
from modules.classes import log

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
    print('Thinking:\n========\n', out_think) if out_think else None
    print('Response:\n========\n', out_ans)
    return out_think, out_ans

def generate_stream(output, out_think="", out_ans=""):
    for chunk in output:
        print("Done crunching!") if not out_think and not out_ans else None
        if chunk.message.thinking:
            print(chunk.message.thinking, end='', flush=True)
            out_think += chunk.message.thinking
        elif chunk.message.content:
            print("Thinking complete!") if not out_think else None
            print(chunk.message.content, end='', flush=True)
            out_ans += chunk.message.content
    return out_think, out_ans
