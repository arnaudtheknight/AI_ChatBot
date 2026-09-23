# Importing Python modules:
from sys import exit
from ollama import ResponseError
## Self-written:
from modules import *

def chatbot(name, history=[], mode_think=False, mode_stream=True):
    while True:
        output_thinking, output_answer = "", ""
        try:
            prompt = prompting()
            print(f"{log2.BLINK}Crunching the numbers. {log2.NEG_WHITE}Please wait...{log2.RESET}")

            history += [{'role': 'user', 'content': prompt}]

            if mode_stream:
                output = interact_stream(name, history, mode_think)
                output_thinking, output_answer = generate_stream(output)
            else:
                output = interact(name, history, mode_think)
                output_thinking, output_answer = generate(output)

            if output_thinking:
                history += [{'role': 'assistant', 'thinking': output_thinking, 'content': output_answer}]
            else:
                history += [{'role': 'assistant', 'content': output_answer}]

        except KeyboardInterrupt as err:
            print("\nKeyboard Interupt ~here~!")
            print("This is in chatbot(), so during chat, so 2 layers deep?")
            print("Press Ctrl-D or use \"/exit\" to quit.")
        except EOFError as err:
            print("\nHard EOF Interrupt ~here~!")
            print("This is in chatbot(), so during chat, so 2 layers deep?")
            break

    return history

if __name__ == '__main__':
    history = history_in()
    while True:
        try:
            valid_names, valid_choices = list_models()
            name, think, stream = model_config(valid_names, valid_choices)
            history = chatbot(name, history, think, stream)
        except EOFError as err:
            print("\nHard EOF Interrupt ~here~!")
            print("This is in name/main, so outside chatbot, so 1 layer deep?")
        except ResponseError as err:
            print("\nResponse Error here!", err)
            print("A model was somehow not appropriately provided, even though you passed config.") 
            print("Let's try this again, shall we?")
            if history and history[-1]['role'] == 'user':
                history.pop()
        except Exception as err:
            print("\nBig yikes!")
            print("Exception arguments:", err.args)
            print(f"{log2.NEG_PURPLE}Non-trivial exit!{log2.RESET} ")
        finally:
            history_out(history)