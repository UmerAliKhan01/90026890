import random

def get_player_beast(player_num):
    return input(f"Player {player_num}, choose your beast: ")

def attack(dice_type, dice_number, is_defending):
    if is_defending:
        return 0
    total = sum(random.randint(1, dice_type) for _ in range(dice_number))
    return total

def play_game(p1_beast, p2_beast):
    p1_health, p2_health = 50, 50
    while p1_health > 0 and p2_health > 0:
        print(f"{p1_beast}'s health: {p1_health}")
        print(f"{p2_beast}'s health: {p2_health}")
        p1_defend = input("Player 1, do you want to defend? (y/n): ").lower() == "y"
        p2_defend = input("Player 2, do you want to defend? (y/n): ").lower() == "y"
        p1_attack = attack(6, 2, p1_defend)
        p2_attack = attack(6, 2, p2_defend)
        p1_health -= p2_attack
        p2_health -= p1_attack
        print(f"{p1_beast} attacks {p2_beast} for {p1_attack} damage")
        print(f"{p2_beast} attacks {p1_beast} for {p2_attack} damage")
    return p1_beast if p2_health <= 0 else p2_beast

if __name__ == "__main__":
    p1_beast = get_player_beast(1)
    p2_beast = get_player_beast(2)
    winner = play_game(p1_beast, p2_beast)
    print(f"{winner} wins!")

