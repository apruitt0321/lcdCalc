import sys

def calc_lcd(args):
    if len(args) < 2:
        return "Not enough arguments. Exiting..."
    else:
        i = 1
        while True:
            y = map(lambda x: True if i % x == 0 else False, args)
            if False not in y:
                return f"Least common denominator of {args} is {i}"
            i += 1

# Main
if __name__ == "__main__":
    x = [int(i) for i in sys.argv[1:]]
    result = calc_lcd(x)
    print(result)
