import sys

def gcf(x,y):
    while y > 0:
        x, y = y, x % y
    return x

def lcd(args):
    while len(args) > 1:
        x, y = args.pop(), args.pop()
        args.append(((x*y) // gcf(x, y)))
    return args[0]

# Main
if __name__ == "__main__":
    try:
        x = [int(i) for i in sys.argv[1:]]
        print(f"Least common multiple of {x} is {lcd(x.copy())}")        
    except:
        print("Error. Check your arguments and try again.")
