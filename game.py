from utils import get_valid_response


def play_game(root):
    current = root
    questions = 0

    print("\n🎯 Think of a number and answer honestly.")

    while current:
        questions += 1
        print(f"\nIs your number higher, lower, or equal to {current.value}?")
        response = get_valid_response()

        if response == "correct":
            print(f"\n🎉 Your number is {current.value}")
            print(f"Questions asked: {questions}")
            return

        elif response == "higher":
            if not current.right:
                print("⚠️ Inconsistent answers detected.")
                return
            current = current.right

        elif response == "lower":
            if not current.left:
                print("⚠️ Inconsistent answers detected.")
                return
            current = current.left