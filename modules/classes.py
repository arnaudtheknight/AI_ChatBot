class col:
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

class tag(col):
    RESET = col.RESET
    ORDER = col.NEG_WHITE
    DEBUG = f"{col.NEG_GREY}[DEBUG]{col.RESET}{col.GREY}"
    INFO = f"{col.NEG_CYAN}[INFO]{col.RESET}{col.CYAN}"
    WARNING = f"{col.NEG_YELLOW}[WARN]{col.RESET}{col.YELLOW}"
    ERROR = f"{col.NEG_RED}[ERROR]{col.RESET}{col.RED}"
    FATAL = f"{col.NEG_PURPLE}[FATAL]{col.RESET}{col.PURPLE}"
    EXIT = f"{col.NEG_GREEN}[EXIT]{col.RESET}{col.GREEN}"

class log2(tag):
    class Importing(tag):
        Import_Prompt = f"\n{tag.ORDER}Provide path to history file:{tag.RESET} "
        Import_Filetype = f"Error parsing file. {tag.PURPLE}(Is the .json file formatted correctly?){tag.RESET}"
        Import_Error_404 = lambda err: f"{log2.WARNING} Failed to open '{log2.UNDER}{err.filename}{log2.RESET}': {err.strerror}."
        Import_Failure = f"{tag.ERROR} Error retrieving history using provided filename. Please try again.{tag.RESET} "
        Import_Skipped = f"{tag.WARNING} History file not provided. Continuing regardless...{tag.RESET} "
        Import_Success = f"{tag.INFO} History imported successfully.{tag.RESET} "

    class Exporting(tag):
        Export_Failure = f"{tag.ERROR} Unable to export message history to the appropriate JSON file.{tag.RESET} "
        Export_Empty = f"{tag.WARNING} Conversation history is empty. Program will NOT export messages.{tag.RESET} "
        Export_Alternative = f"{tag.WARNING} Saving to alternative history export location...{tag.RESET} "

    class Config(tag):
        Config_Prompt_Fail = f"{tag.WARNING} Incorrect input.{tag.RESET} {tag.UNDER}Try again.{tag.RESET} "
        Config_Model_Show = f"\n{tag.UNDER}The following models can be used for this chat:{tag.RESET} "
        Config_Model_Prompt = f"{tag.ORDER}Provide the name of the model you would like to use:{tag.RESET} "
        Config_Mode_Stream = f"{tag.UNDER}Would you like the output streamed to the terminal?{tag.RESET} {tag.ORDER}[y/N]{tag.RESET} "
        Config_Mode_Think = f"{tag.UNDER}Would you like to enable thinking mode?{tag.RESET} {tag.ORDER}[Y/n]{tag.RESET} "

class slash():
    History_Skip = {'', "/no", "/skip"}
    Chat_END = {"/end", "/eof"}
    Chat_STOP = {"/bye", "/close", "/stop"}
    Chat_Mistake = {"/del-prev", "/oops"}
    Chat_Wipe = {"/del-all", "/wipe"}
    Config = {"/conf","/config"}
    Raise_ResponseError = {"/err-response", "uuddlrlrab"}

    
class log(col):
    Config_Incorrect= f"{col.YELLOW}Incorrect input. Try again: {col.RESET}"
    Error_General = f"{col.RED}[ERROR] Unknown error has occured. {col.RESET}\nRefer to debugging for more information.\n{col.BLINK}NON-TRIVIAL EXIT.{col.RESET}"
    Error_KeyboardInterrupt = f"{col.RED}KeyboardInterrupt detected outside chat. Stopping now.{col.RESET}"
    Hist_Import_Missing = f"{col.NEG_RED}[ERROR] Failed to import history: File not found. \nPossible missing file or incorrect path?"
    Hist_Import_Success = f"{col.CYAN}[INFO] Import successful.{col.RESET}"
    Hist_Import_Empty = f"{col.YELLOW}[WARN] History not provided, starting afresh... {col.RESET}"
    Hist_Export_Fail = f"{col.RED}[ERROR] Failed to export history to JSON.{col.RESET}"
    Chat_Prompting = f"\nAwaiting the next (short) prompt: \n{col.NEG_WHITE}${col.RESET} "
    Chat_Processing = f"{col.UNDER}Crunching the numbers. {col.BLINK}Please wait...{col.RESET}"
    Exit_KeyboardInterrupt = f"\n{col.RED}[WARN] KeyboardInterrupt detected. Closing chatbot now.{col.RESET}"
    Exit_Uncaught = f"{col.RED}[ERROR] Critical uncaught failure. Quitting immediately. {col.RESET}"
    Exit_Trivial = f"{col.BLINK}TRIVIAL EXIT! :) {col.RESET}"
    Exit_NonTrivial = f"{col.RED}{col.BLINK}NON-TRIVIAL EXIT! :({col.RESET}"
    # "\nGoodbye! *wave*"

"""
Points of improvement:
- finishing the damn log2 stack
- finishing the damn migration from log to log2
- an actually decent error handling system, where i raise my own errors
- class for slash commands?
"""

""" RETIRED:
class col:
    RESET = '\033[0m'
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
"""