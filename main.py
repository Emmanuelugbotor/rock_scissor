import random
is_playing = True
level = 0
computer_score = 0
player_score = 0


def lamda_func(a):
    res = "rock" if a == 'R' else (
        'paper' if a == 'P' else 'scissor')
    return res.title()


while is_playing:
    choices = ["R", "P", "S"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("R, P, or S?: ").upper()
        level = level + 1

    if player == computer:
        print(f"Player ({ lamda_func(player)}) : CPU ({lamda_func(computer)})")
        print("Tie!")

    elif player == "R":
        if computer == "P":
            print(
                f"Player ({ lamda_func(player)}) : CPU ({lamda_func(computer)})")
            print("You lose!")
            computer_score = computer_score + 1
        if computer == "scissors":
            print(
                f"Player ({ lamda_func(player)}) : CPU ({lamda_func(computer)})")
            print("You win!")
            player_score = player_score + 1

    elif player == "S":
        if computer == "R":
            print(
                f"Player ({ lamda_func(player)}) : CPU ({lamda_func(computer)})")
            print("You lose!")
            computer_score = computer_score + 1
        if computer == "P":
            print(
                f"Player ({ lamda_func(player)}) : CPU ({lamda_func(computer)})")
            print("You win!")
            player_score = player_score + 1

    elif player == "P":
        if computer == "S":
            print(
                f"Player ({ lamda_func(player)}) : CPU ({lamda_func(computer)})")
            print("You lose!")
            computer_score = computer_score + 1
        if computer == "R":
            print(
                f"Player ({ lamda_func(player)}) : CPU ({lamda_func(computer)})")
            print("You win!")
            player_score = player_score + 1
# determine the outcome of the round
    if level == 3:
        if player_score > computer_score:
            print(f"Player win this round")
        elif player_score < computer_score:
            print(f"CPU win this round")
        else:
            print(f"this round ended in a tie")
        play_again = input(
            "Do you want to play another round? (yes/no): ").lower()
        player_score = 0
        computer_score = 0
        level = 0
        if play_again != "yes":
            is_playing = False

    if(level != 3) and (level != 0):
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            is_playing = False


print("Bye!")
