class col:
    END = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    NEG = '\033[7m'
    GRAY_LIGHT = '\033[0;37m'
    GRAY_DARK = '\033[1;30m'
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    PURPLE = '\033[1;35m'
    CYAN = '\033[1;36m'
    WHITE = '\033[1;37m'

class log(col):
    Config_Incorrect= f"{col.YELLOW}Incorrect input. Try again: {col.END}"
    Error_General = f"{col.RED}[ERROR] Unknown error has occured. {col.END}\nRefer to debugging for more information.\n{col.BLINK}NON-TRIVIAL EXIT.{col.END}"
    Error_KeyboardInterrupt = f"{col.RED}KeyboardInterrupt detected outside chat. Stopping now.{col.END}"
    Hist_Import_Missing = f"{col.RED}{col.NEG}[ERROR] Failed to import history: File not found. \nPossible missing file or incorrect path?"
    Hist_Import_Success = f"{col.CYAN}[INFO] Import successful.{col.END}"
    Hist_Import_Empty = f"{col.YELLOW}[WARN] History not provided, starting afresh... {col.END}"
    Hist_Export_Fail = f"{col.RED}[ERROR] Failed to export history to JSON.{col.END}"
    Chat_Prompting = f"\nAwaiting the next (short) prompt: \n{col.NEG}${col.END} "
    Chat_Processing = f"{col.UNDER}Crunching the numbers. {col.BLINK}Please wait...{col.END}"
    Exit_KeyboardInterrupt = f"\n{col.RED}[WARN] KeyboardInterrupt detected. Closing chatbot now.{col.END}"
    Exit_Uncaught = f"{col.RED}[ERROR] Critical uncaught failure. Quitting immediately. {col.END}"
    Exit_Trivial = f"{col.BLINK}TRIVIAL EXIT! :) {col.END}"
    Exit_NonTrivial = f"{col.RED}{col.BLINK}NON-TRIVIAL EXIT! :({col.END}"
    # "\nGoodbye! *wave*"