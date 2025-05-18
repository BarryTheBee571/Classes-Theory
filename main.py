from game_objects import Player, Weapon
import random

Player1= Player('Bartholomew of Scotland III', 'Russian', 'Trumpet Blower', 20, 200)
Player2= Player('Little Timmy', 'Gnome', 'Anklebiter', 50, 20)
Player3= Player('Oscar Piastri', 'Human', 'F1 Driver', 20, 500)
Player4= Player('Jerome', 'Monkey', 'Proffesional Banana Eater', 2, 10)

Weapon1= Weapon('Big Stick', 'Melee', 10)
Weapon2= Weapon('Small Sword', 'Melee', 5)
Weapon3= Weapon('R-36M Intercontinental Ballistic Missile', 'Range', 500)
Weapon4= Weapon('Garlic', 'Repellent', 0)

def choose_player():
    while True:
        player= input("Which Character would you like to choose?:\n1. " + Player1.name + "\n2. " + Player2.name + "\n3. " + Player3.name + "\n4. " + Player4.name + "\nPlease enter one of the numbers: ")
        if player=='1':
            print(f"You have chosen: {Player1.name}\nrace: {Player1.race}\nClass: {Player1.cls}\nAttack: {Player1.atk}\nHealth: {Player1.health}")
            break
        elif player=='2':
            print(f"You have chosen: {Player2.name}\nrace: {Player2.race}\nClass: {Player2.cls}\nAttack: {Player2.atk}\nHealth: {Player2.health}")
            break
        elif player=='3':
            print(f"You have chosen: {Player3.name}\nRace: {Player3.race}\nClass: {Player3.cls}\nAttack: {Player3.atk}\nHealth: {Player3.health}")
            break
        elif player=='4':
            print(f"You have chosen: {Player4.name}\nrace: {Player4.race}\nClass: {Player4.cls}\nAttack: {Player4.atk}\nHealth: {Player4.health}")
            break
        else:
            print("Please choose a valid number")

def choose_weapon():
       while True:
        player= input("\nWhich Weapon would you like to use?:\n1. " + Weapon1.name + "\n2. " + Weapon2.name + "\n3. " + Weapon3.name + "\n4. " + Weapon4.name + "\nPlease enter one of the numbers: ")
        if player=='1':
            print(f"You have chosen: {Weapon1.name}\nCategory: {Weapon1.category}\nDamage: {Weapon1.damage}")
            break
        elif player=='2':
            print(f"You have chosen: {Weapon2.name}\nCategory: {Weapon2.category}\nDamage: {Weapon2.damage}")
            break
        elif player=='3':
            print(f"You have chosen: {Weapon3.name}\nCategory: {Weapon3.category}\nDamage: {Weapon3.damage}")
            break
        elif player=='4':
            print(f"You have chosen: {Weapon4.name}\nCategory: {Weapon4.category}\nDamage: {Weapon4.damage}")
            break
        else:
            print("Please choose a valid number")

choose_player()

choose_weapon()

