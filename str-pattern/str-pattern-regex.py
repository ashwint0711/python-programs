import re

def main():
    inp = input("Enter value : ")
    res = stringPattern(inp)

    print(res)

def stringPattern(inp):

    pattern = r"^i.*a.*n$"

    regex = re.compile(pattern)

    inp = inp.lower()
    if regex.match(inp) : 
        return "Found!"
    else :
        return "Not Found!"

if __name__ == "__main__":
    main()