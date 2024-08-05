import sys

def main():
    names = []

    # Read names from user input until Ctrl-D (EOF) is entered
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    # Determine the number of names
    num_names = len(names)

    # Generate the farewell message based on the number of names
    if num_names == 1:
        farewell = f"Adieu, adieu, to {names[0]}"
    elif num_names == 2:
        farewell = f"Adieu, adieu, to {names[0]} and {names[1]}"
    elif num_names > 2:
        farewell = f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"

    # Print the farewell message
    print(farewell)

if __name__ == "__main__":
    main()
