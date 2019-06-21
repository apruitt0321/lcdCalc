import sys

def calc_lcd(args):
    i = max(args)
    while True:
        y = map(lambda x: True if i % x == 0 else False, args)
        if False not in y: return i
        i += 1

# Main
if __name__ == "__main__":
    try:
        x = [int(i) for i in sys.argv[1:]]
        print(f"Least common multiple of {x} is {calc_lcd(x)}")
    except:
        print("Error. Check your arguments and try again.")
