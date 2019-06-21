from collections import Counter

def calc_lcd(*args):
    if len(args) < 2:
        return "Not enough arguments. Exiting..."
    else:
        denoms = Counter()
        c = 1
        while True:
            for i in args:
                denoms[i*c] += 1
                most_common, num_common = denoms.most_common(1)[0]
            if num_common == len(args):
                return f"Most common denominator of {args} is {most_common}"
            else:
                c += 1
                if c == 100:
                    return "Could not find a common denominator."
        else:
            return "Could not find a common denominator."


if __name__ == "__main__":
    result = calc_lcd(2, 8, 20, 15)
    print(result)

