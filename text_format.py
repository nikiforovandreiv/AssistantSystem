# ANSI escape codes for text formatting
class TextFormat:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'


# Example usage
# print(f"{TextFormat.RED}This is a highlighted red text.{TextFormat.RESET}")
# print(f"{TextFormat.GREEN}This is a highlighted green text.{TextFormat.RESET}")
# print(f"{TextFormat.BOLD}{TextFormat.BLUE}This is a bold and blue text.{TextFormat.RESET}")
