from ollama import chat
import re
from rich.console import Console
from rich.markdown import Markdown
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

def math_esc(text):
    # Block maths:
    text = re.sub(
        r"\$\$(.*?)\$\$",
        str(f"\n{log2.NEG_GREEN}$$" + r"\1" + f"$${log2.RESET}\n"),
        text,
        flags=re.DOTALL
    )
    # In-line maths:
    text = re.sub(
        r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)",
        str(f"{log2.GREEN}$" + r"\1" + f"${log2.RESET}"),
        text
    )
    return text


def generate(output, out_think="", out_ans=""):
    console = Console()
    if output.message:
        print("Done crunching!") if not (out_think and out_ans) else None
        out_think = output.message.thinking if output.message.thinking else None
        out_ans = output.message.content
    # if out_think:
    #     print(f"{log2.NEG_BLUE}Thinking: {log2.RESET}")
    #     console.print(Markdown(f"{log2.BLUE}{out_think}{log2.RESET}"))
    #     # console.print(f"{log2.BLUE}{Markdown(out_think)}{log2.RESET}")
    # print(f"{log2.NEG_GREEN}Response: {log2.RESET}")
    # console.print(Markdown(out_ans))
    if out_think:
        print(f"{log2.NEG_BLUE}THINKING: {log2.RESET}")
        print(log2.BLUE)
        console.print(Markdown(math_esc(out_think)))
        print(log2.RESET)
    print(f"{log2.GREEN}RESPONSE: {log2.RESET}")
    console.print(Markdown(math_esc(out_ans)))
    
    return out_think, out_ans

def generate_stream(output, out_think="", out_ans=""):
    try:
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
    except KeyboardInterrupt:
        return out_think, out_ans

# Points of Improvement:
"""
- from rich.live import Live ; with Live(console=console, refresh_per_second=5) as live: ... live.update(Markdown(out))
"""