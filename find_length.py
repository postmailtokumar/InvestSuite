"""this script is written to find the length of the given number"""


def ask_input():
    """Asking the input from the Customer"""
    inp = input("Enter the integer or float number:")
    return inp


def validate_input(inp):
    """Validating the given inputs whether it is valid integer or float value"""
    try:
        res = float(inp)
        return res
    except Exception as exc:
        print(exc)
        inp = ask_input()
        val_res = validate_input(inp)
        return val_res


def find_len(val_res):
    """Once the input got validated,
    this function helps to find the length of the given input"""
    try:
        result = len(str(round(val_res)))
        return result
    except Exception as exc:
        print(exc)
        print('Error in finding the length of value:')
        return None


def main_execution():
    """Execution in waterfall model!!"""
    inp = ask_input()
    val_res = validate_input(inp)
    if val_res is not None:
        result = find_len(val_res)
        print('Length of the given input:', result)


if __name__ == '__main__':
    """Infinite loop so that we can test easily"""
    while True:
        main_execution()



