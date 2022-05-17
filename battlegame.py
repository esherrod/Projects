# Initialize Character Classes
wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"
# Initialize Character Health
wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 200
# Initialize Character Damage
wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 125
# Initialize Character choice
character = ""
character_hp = 0
character_damage = 0
# Initialize Boss Health and Damage
dragon_hp = 300
dragon_damage = 50

play_game = True

while play_game:

    while play_game:
        print(f"1) {wizard}\n2) {elf}\n3) {human}\n4) {orc}\n5) Quit Game")
        choice = str(input("Choose your character: ")).lower()

        if choice == '1' or choice == 'wizard':
            print('You have chosen the {}!\nHealth: {}\nDamage: {}'.format(
                wizard, wizard_hp, wizard_damage))
            character = wizard
            character_hp = wizard_hp
            character_damage = wizard_damage
            break
        elif choice == '2' or choice == 'elf':
            print('You have chosen the {}!\nHealth: {}\nDamage: {}'.format(
                elf, elf_hp, elf_damage))
            character = elf
            character_hp = elf_hp
            character_damage = elf_damage
            break
        elif choice == '3' or choice == 'human':
            print('You have chosen the {}!\nHealth: {}\nDamage: {}'.format(
                human, human_hp, human_damage))
            character = human
            character_hp = human_hp
            character_damage = human_damage
            break
        elif choice == '4' or choice == 'orc':
            print('You have chosen the {}!\nHealth: {}\nDamage: {}'.format(
                orc, orc_hp, orc_damage))
            character = orc
            character_hp = orc_hp
            character_damage = orc_damage
            break
        elif choice == '5' or choice == 'quit':
            play_game = False
        else:
            print("That wasn't one of the options! Please try again!\n")

    while play_game:
        print("The {} damaged the dragon!".format(character))
        dragon_hp -= character_damage
        if dragon_hp < 0:
            dragon_hp = 0
        print("The Dragons HP is now {}!".format(dragon_hp))
        if dragon_hp <= 0:
            print("The {} has slain the Dragon, and brought peace to the Kingdom!".format(
                character))
            break

        print("The Dragon has damaged the {}!".format(character))
        character_hp -= dragon_damage
        print("The {}'s HP is now {}!".format(character, character_hp))
        if character_hp <= 0:
            print("The {} has been slain by the Dragon! Now the land shall fall into darkness!".format(
                character))
            break

    if play_game == True:
        play_again = str(
            input("1) Yes\n2) No\nWould you like to play again: ")).lower()

        if play_again == '1' or play_again == 'yes' or play_again == 'y':
            dragon_hp = 300
        else:
            print(""" 
  ________                        ________                      
 /  _____/_____    _____   ____   \_____  \___  __ ___________  
/   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \ 
\    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/ 
 \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|    
        \/     \/      \/     \/          \/          \/       
    """)
            print("Thanks for playing!")
            play_game = False
    else:
        print(""" 
  ________                        ________                      
 /  _____/_____    _____   ____   \_____  \___  __ ___________  
/   \  ___\__  \  /     \_/ __ \   /   |   \  \/ // __ \_  __ \ 
\    \_\  \/ __ \|  Y Y  \  ___/  /    |    \   /\  ___/|  | \/ 
 \______  (____  /__|_|  /\___  > \_______  /\_/  \___  >__|    
        \/     \/      \/     \/          \/          \/      
    """)
        print("Thanks for playing!")
