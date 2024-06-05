def get_location():
    print("\nEnter 'q' at any time to quit. ")
    print()

    while True:
        city = input("City: ")
        if city == 'q':
            return None

        state = input("State: ")
        if state == "q":
            return None

        country = input("Country: ")
        if country == 'q':
            return None

        population = input("Population (Optional):  ")
        if population == 'q':
            return None

        location = f"\n-{city}, {state.upper()}, {country.upper()}: population {population}-"
        print(location.title())
        print()

    return location    

result = get_location()
