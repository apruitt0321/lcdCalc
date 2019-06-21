from collections import Counter
import sys

def calc_lcd(args):
    if len(args) < 2:
        return "Not enough arguments. Exiting..."
    else:
        denoms = Counter()          # Counter object
        count = 1                       # loop counter
        while True:
            for denominator in args:
                denoms[denominator * count] += 1
            # Takes most common product and the number of times it appears
            product, num_common = denoms.most_common(1)[0]
            # Checks if a product appears as many times as there are arguments
            if num_common == len(args):
                return f"Most common denominator of {args} is {product}"
            else:
                count += 1
                # Prevents potential hanging. Could probably be removed.
                if count == 200:
                    return "Reached 200 iterations. Exiting..."
        else:
            return "Could not find a common denominator."

# Main
if __name__ == "__main__":
    x = [int(i) for i in sys.argv[1:]]
    result = calc_lcd(x)
    print(result)
