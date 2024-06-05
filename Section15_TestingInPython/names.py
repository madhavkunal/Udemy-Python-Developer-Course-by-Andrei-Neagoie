from name_function import get_formatted_name

while True:
    print("\n[Enter 'q' at any time to exit the program]")

    first = input("Please provide a first name: ")
    if first == "q":
        break
    last = input("Please provide a last name: ")
    if last == "q":
        break
    middle = input("Optional: Provide a middle name [Press Enter to Skip]: ")
    if middle == "q":
        break
    
    formatted_name = get_formatted_name(first, middle, last)
    print(f"{formatted_name}")
