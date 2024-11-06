#I worked on this code with Ernesto Castañeda
import random
#Menu
print("Gregs Adventures!")
print()
#Lore
print("In the land of Nauria, three powerful clans—Medics, Warriors, and Assassins—once united to protect the realm. Now divided, they battle for control over the legendary Heartstone, an ancient relic that grants immense power to its wielder. Greg, an unlikely hero from a small village, discovers a mysterious artifact tied to the Heartstone and is thrust into this conflict. To survive, he must choose a clan to join and master their unique skills, while facing dangerous foes, like ruthless bandits, who seek the Heartstone’s power for themselves. Can Greg reunite the clans and restore peace, or will darkness claim Nauria?")
print()
a = int(input("Press the 1 key to proceed: "))
while a == 1:
    name = input("Enter player name: ")
    print(f"Welcome {name}")
    print("There are 3 clans: Medic(5 damage, 15 healing), Warrior(10 damage, 10 healing), and Assassin(15 damage, 5 healing)")
    clan = input("Which clan do you want to train under?: ")
    s=open("myfile.txt", "a")
    s.write(f"\nA new character has been created! The character is a {clan}")
    s.close
    #Warrior class
    class Warrior:  
        def __init__(self, name, health, attack, heal):  
            self.name = name
            self.health = health
            self.attack = attack
            self.heal_value = heal

        def take_damage(self, attack):  
            self.health -= attack

        def is_alive(self):  
            return self.health > 0

        def heal(self):  
            self.health += self.heal_value
    
    #Medic class
    class Medic:  
        def __init__(self, name, health, attack, heal):  
            self.name = name
            self.health = health
            self.attack = attack
            self.heal_value = heal

        def take_damage(self, attack):  
            self.health -= attack

        def is_alive(self):  
            return self.health > 0

        def heal(self):  
            self.health += self.heal_value
    
    #Assassin class
    class Assassin:  
        def __init__(self, name, health, attack, heal):  
            self.name = name
            self.health = health
            self.attack = attack
            self.heal_value = heal

        def take_damage(self, attack):  
            self.health -= attack

        def is_alive(self):  
            return self.health > 0

        def heal(self):  
            self.health += self.heal_value
    
    #Make player
    if clan.lower() == "warrior":
        player = Warrior(name, 100, 10, 10)
    elif clan.lower() == "medic":
        player = Medic(name, 100, 5, 15)
    elif clan.lower() == "assassin":
        player = Assassin(name, 100, 15, 5)
    else:
        print("Invalid clan choice.")
        continue

    print("Your journey begins!")
    print()
    print()
    print()
    print()
    print("You've encountered a Bandit!")

    class Bandit:  
        def __init__(self, health, attack):  
            self.health = health
            self.attack = attack

        def take_damage(self, damage):  
            self.health -= damage

        def is_alive(self):  
            return self.health > 0

    bandit = Bandit(50, 15)
##
##
#Main#
##
##
    #Alternate turns
    player_turn = True

    while player.is_alive() and bandit.is_alive():
        if player_turn:
            #Your turn
            print()
            print(f"Your turn!")
            print(f"You have {player.health} health. The Bandit has {bandit.health} health.")
            action = input("Do you want to heal (h) or attack (a)? ")

            if action == "h":
                player.heal()
                print(f"You healed for {player.heal_value}. You are now at {player.health} health.")
            elif action == "a":
                bandit.take_damage(player.attack)
                print(f"You attacked the Bandit for {player.attack} damage.")
            else:
                print("Invalid action.")
                continue
        else:
            #Bandit turn
            print("\nBandit's turn!")
            hit_chance = random.randint(1, 10)
            if hit_chance > 5:
                player.take_damage(bandit.attack)
                print(f"The Bandit hit you for {bandit.attack} damage! You are now at {player.health} health.")
            else:
                print("The Bandit missed!")
            #Small but possible chance you die to an obstacle
            p=random.randint(1, 50)
            q=random.randint(1, 50)
            if p == q:
                player.take_damage(100)
                print("You fell into a pit of deadly animals and took 100 damage")

        #Alternate turn
        player_turn = not player_turn

    #End
    if player.is_alive():
        print()
        print(f"Congratulations, {player.name}! You have defeated the Bandit.")
        print()
        print("Level 2")
        bandit = Bandit(50, 20)
        print()
                #Alternate turns
        player_turn = True
    
        while player.is_alive() and bandit.is_alive():
            if player_turn:
                #Your turn
                print()
                print(f"Your turn!")
                print(f"You have {player.health} health. The Bandit has {bandit.health} health.")
                action = input("Do you want to heal (h) or attack (a)? ")
    
                if action == "h":
                    player.heal()
                    print(f"You healed for {player.heal_value}. You are now at {player.health} health.")
                elif action == "a":
                    bandit.take_damage(player.attack)
                    print(f"You attacked the Bandit for {player.attack} damage.")
                else:
                    print("Invalid action.")
                    continue
            else:
                #Bandit turn
                print("\nBandit's turn!")
                hit_chance = random.randint(1, 10)
                if hit_chance > 5:
                    player.take_damage(bandit.attack)
                    print(f"The Bandit hit you for {bandit.attack} damage! You are now at {player.health} health.")
                else:
                    print("The Bandit missed!")
            #Small but possible chance you die to an obstacle
            p=random.randint(1, 50)
            q=random.randint(1, 50)
            if p == q:
                player.take_damage(100)
                print("You fell into a pit of deadly animals and took 100 damage")
            #Alternate turn
            player_turn = not player_turn

        #End
        if player.is_alive():
            print()
            print(f"Congratulations, {player.name}! You have defeated the Bandit.")
            print()
            print("Level 3")
            bandit = Bandit(61, 25)
            print()
            #Alternate turns
            player_turn = True
    
            while player.is_alive() and bandit.is_alive():
                if player_turn:
                    #Your turn
                    print()
                    print(f"Your turn!")
                    print(f"You have {player.health} health. The Bandit has {bandit.health} health.")
                    action = input("Do you want to heal (h) or attack (a)? ")
        
                    if action == "h":
                        player.heal()
                        print(f"You healed for {player.heal_value}. You are now at {player.health} health.")
                    elif action == "a":
                        bandit.take_damage(player.attack)
                        print(f"You attacked the Bandit for {player.attack} damage.")
                    else:
                        print("Invalid action.")
                        continue
                else:
                    #Bandit turn
                    print("\nBandit's turn!")
                    hit_chance = random.randint(1, 10)
                    if hit_chance > 5:
                        player.take_damage(bandit.attack)
                        print(f"The Bandit hit you for {bandit.attack} damage! You are now at {player.health} health.")
                    else:
                        print("The Bandit missed!")
                #Small but possible chance you die to an obstacle
                p=random.randint(1, 50)
                q=random.randint(1, 50)
                if p == q:
                    player.take_damage(100)
                    print("You fell into a pit of deadly animals and took 100 damage")
                #Alternate turn
                player_turn = not player_turn
                #End
            if player.is_alive():
                print()
                print(f"Congratulations, {player.name}! You have deafeated all the bandits and brought piece to the land! Every clan in Nauria thanks you.")
                a+=1
        #Program defeat    
            else:
                print()
                print(f"You have been defeated by the Bandit. Better luck next time, {player.name}.")
                a+=1
        #Program defeat
        else:
            print()
            print(f"You have been defeated by the Bandit. Better luck next time, {player.name}.")
            a+=1
    #Program defeat
    else:
        print()
        print(f"You have been defeated by the Bandit. Better luck next time, {player.name}.")
        a+=1
