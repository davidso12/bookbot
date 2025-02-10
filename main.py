def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    
    print_chars(file_contents)


def print_chars(words):
    chars = {}
    for x in words:
        lower_case = x.lower()
        if lower_case in chars:
            chars[lower_case] += 1
        else:
            chars[lower_case] = 1
    print_report(chars)

def print_report(dictionary):

    for key in dictionary:
        if key == " ":
            pass
        elif key == ".":
            pass
        elif key == "#":
            pass
        else:
            print(f"The '{key}' character was found '{dictionary[key]} times'")
main()
