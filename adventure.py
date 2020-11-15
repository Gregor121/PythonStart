import random
hp = 100

def bedroom():
    print("""You wake up in your room cold and dark.  Notice a flashing
    warning that all O2 has been vented during the night. Your cabin seems fine
    but all other life on the ship is dead.""")
    user_input = input("""Choose an adventure!
            1: Move to cockpit
            2: Venture into hallway
            > """)
    if user_input == "1":
        cockpit()
    elif user_input == "2":
        hallway()
    else:
        print("Not correct value")
        exit(1)

def hallway():
    minotaur = 50
    global hp
    print("""Entering the hallway you peer around the corner and notice a
    SPACE MINOTAUR sitting against the electical panel with the O2 controls.
    Your options seem limited...""")
    while True:
        user_input = input("""Choose an adventure!
            1: You see a severed high voltage electrical cable hanging near
            the minotaur - you could stab it into it's neck and score a 
            critical hit!
            2: There is a possibility you could trip the beast up by kicking 
            it in the shin and run for the next room.
            > """)
        if user_input == "1":
            crit = random.randint(1, 4)
            if crit == 1:
                minotaur = minotaur - 30
                print("You scored a critical hit!")
            else:
                minotaur = minotaur - 7
                print("You barely hit it! Thor would be depressed." )   
             
        elif user_input == "2":
            minotaur = minotaur - 10
            print("You tickled the minotaur in the shin, why do you think that would do anything?")
        else:
            print("Not correct value")
            exit(1)

        if minotaur <= 0:
            print("The minotaur collapses into a pile of beef")   
            break
        print('The minotaur has ' + str(minotaur) + "hp") 
       
        crit = random.randint(1, 3)
        if crit == 1:
            hp = hp - 40
            print("Not the face! Nose is broken, ouch.")
        else:
            hp = hp - 10
            print("The minotaur charges you and knocks you over" ) 

        if hp <= 0:
           print("You died.")
           exit(0)

        print("Your HP is now " + str(hp)) 
        


    print("You make your way to the kitchen")
    kitchen()
           
           

        


        



        
    



bedroom()