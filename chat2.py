# Importing python modules:
from sys import exit
from ollama import ResponseError
# Self-written:
from modules import *

# Chatbot logic:
"""
def chatbot(name, history, mode_think=False, mode_stream=True, prompt=""):
    if prompt:
        print(f"Trying again with previous prompt...")
        print(f"{log2.NEG_GREY}{prompt}{log2.RESET}")
    while True:
        output_thinking, output_answer = "", ""
        try:
            if not prompt:
                prompt = prompting()

            print(f"{log2.BLINK}Crunching the numbers. {log2.NEG_WHITE}Please wait...{log2.RESET}")
            
            history += [{'role': 'user', 'content':prompt}]

            # if prompt == "uuddlrlrab":
            #     raise ResponseError("gay")
"""
def chatbot(name, history=[], mode_think=False, mode_stream=True, previous=""):
    while True:
        output_thinking, output_answer = "", ""
        try:
            if previous:
                prompt = previous
                print(f"Trying again with previous prompt...\n{prompt}")
            else:
                prompt = prompting()
                
            if prompt == "uuddlrlrab":
                raise ResponseError("gay")
            else:
                history += [{'role': 'user', 'content':prompt}]
                print(f"{log2.BLINK}Crunching the numbers. {log2.NEG_WHITE}Please wait...{log2.RESET}")

            if mode_stream:
                output = interact_stream(name, history, mode_think)
                output_thinking, output_answer = generate_stream(output)
            else:
                output = interact(name, history, mode_think)
                output_thinking, output_answer = generate(output)

            if output_thinking:
                history += [{'role': 'assistant', 'thinking':output_thinking,'content':output_answer}]
            else:
                history += [{'role': 'assistant', 'content':output_answer}]
        except KeyboardInterrupt:
            print("Keyboard Interrupt ~DURING CHAT~ here!")
            if output_thinking:
                history += [{'role': 'assistant', 'thinking':output_thinking,'content':output_answer}]
            elif output_answer:
                history += [{'role': 'assistant','content':output_answer}]
            break
    return history

if __name__ == '__main__':
    try:
        prompt_last = ""
        history = history_import()
        if history:
            previous = history[-1]
            if previous['role'] == 'user':
                prompt_last = previous['content'] 
                history.pop()
        while True:
            try:
                valid_names, valid_choices = model_lister()
                name, think, stream = configuration(valid_names, valid_choices)
                if prompt_last:
                    history = chatbot(name, history, think, stream, prompt_last)
                else:
                    history = chatbot(name, history, think, stream)
                break
            except ResponseError as err:
                print("Response Error here!", err)
                print("A model was somehow not appropriately provided, even though you passed config.") 
                print("Let's try this again, shall we?")
                if history:
                    previous = history[-1]
                    if previous['role'] == 'user':
                        prompt_last = previous['content'] 
                        history.pop()
            except Exception:
                print("\nBig yikes!")
                print("Non-trivial exit!")
            finally:
                history_export(history)
    except KeyboardInterrupt:
        exit("\nKeyboard Interrupt ~OUTSIDE CHAT~ here!")

"""
Points of improvement:
- full migration to log2 colours and errors
- bug-busting/perfecting the history import for last prompt
- multiline prompt inputs
"""