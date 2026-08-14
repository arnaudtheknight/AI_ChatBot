class col2:
    RESET = '\033[0m' # all attributes off
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m' # Underline
    BLINK = '\033[5m' # (Slow) blink
    NEG_WHITE = '\033[7m' # swap fg and bg colours
    HIDE = '\033[8m' # Conceal
    # STRIKE = '\033[9m' # Strikethrough
    # GREY_L = '\033[37m' # Light grey
    GREY = '\033[90m' # Dark grey
    RED = '\033[91m' # Red+
    GREEN = '\033[92m' # Green+
    YELLOW = '\033[93m' # Yellow+
    BLUE = '\033[94m' # Blue+
    PURPLE = '\033[95m' # Purple+
    CYAN = '\033[96m' # Cyan+
    
    NEG_RED = '\033[41m' # Red bg
    NEG_GREEN = '\033[42m' # Green bg
    NEG_YELLOW = '\033[43m' # Yellow bg
    NEG_BLUE = '\033[44m' # Blue bg
    NEG_PURPLE = '\033[45m' # Purple bg
    NEG_CYAN = '\033[46m' # Cyan bg
    NEG_GREY = '\033[100m' # Grey+ bg

class log_mini(col2):
    DEBUG = f"{col2.NEG_GREY}[DEBUG]{col2.RESET} {col2.GREY}"
    INFO = f"{col2.NEG_CYAN}[INFO]{col2.RESET} {col2.CYAN}"
    WARNING = f"{col2.NEG_YELLOW}[WARN]{col2.RESET} {col2.YELLOW}"
    ERROR = f"{col2.NEG_RED}[ERROR]{col2.RESET} {col2.RED}"
    FATAL = f"{col2.NEG_PURPLE}[FATAL]{col2.RESET} {col2.PURPLE}"
    EXIT = f"{col2.NEG_GREEN}[EXIT]{col2.RESET} {col2.GREEN}"

# class log2(log_mini):


class col:
    END = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    NEG = '\033[7m'
    STR = '\033[9m'
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