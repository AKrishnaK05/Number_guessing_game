def get_valid_response():
    valid = {"higher", "lower", "correct"}
    while True:
        response = input("Your answer (higher/lower/correct): ").strip().lower()
        if response in valid:
            return response
        print("Invalid input. Please try again.")