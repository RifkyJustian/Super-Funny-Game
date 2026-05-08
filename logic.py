from game.generator import generate_number
from utils.display import show_result
from config import MAX_ATTEMPTS

def start_game():

    secret_number = generate_number()
    attempts = 0

    while attempts < MAX_ATTEMPTS:

        try:
            guess = int(input("\nEnter your guess: "))
        except:
            print("❌ Please enter a valid number!")
            continue

        attempts += 1

        if guess == secret_number:
            show_result("🏆 Correct! You win!")
            return

        elif guess < secret_number:
            show_result("📉 Too low!")

        else:
            show_result("📈 Too high!")

        print(f"Remaining attempts: {MAX_ATTEMPTS - attempts}")

    print(f"\n❌ Game Over! The number was {secret_number}")
