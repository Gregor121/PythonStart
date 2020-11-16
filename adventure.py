import random
hp = 100

def bedroom():
    story = """You wake up in your room cold and dark.  Notice a flashing
    warning that all O2 has been vented during the night. Your cabin seems fine
    but all other life on the ship is dead."""
    
    user_input = adv_input(story, ["Move to cockpit", "Venture into hallway"])

    if user_input == 1:
        cockpit()
    elif user_input == 2:
        hallway()

def cockpit():
    print("""Slipping through a secret compartment brings you into the cockpit.
    The forward glass is all iced over and the pilot is slumped in his seat. 
    Do you try and fire up the shuttle? Only time will tell.""")
    user_input = input("""Choose an adventure!
        1: Shove pilot out of the way and fire this baby up
        2: Leave controls alone and head down the hallway towards the engines
        > """)
    if user_input == "1":
        explode = random.randint(1, 6)
        if explode == 3:
            print('You hit the big red button and the ship exploded')
            exit(0)
        else:
            print('You got the controls fired up, but nothing is responding')
            hallway()
    elif user_input == "2":
        print('You choose to leave the controls be and head for the engine room')
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

def kitchen():
    global hp
    print("""Confidently strolling into the kitchen after your battle with
    the minotaur you come upon a much needed buffet in the kitchen!""")
    user_input = input("""Choose an adventure!
        1: You see a half eaten KitKat bar on the counter. 
        2: You see a delicious looking ostrich egg.
        3: You are to panicked to eat and head for the engine room.
        > """)
    
    if user_input == "1":
        hp = hp + 10
        print('Your HP has been restored, it is now ' + str(hp))
        engine_room()
    elif user_input == "2":
        print("""If this already wasn't a bad situation the egg turned out
        to be a face hugger alien and you are now dead""")
        exit(0)
    elif user_input == "3":
        print("You charge onward to the engine room")
        engine_room()
    else:
        print('Not correct value')    
        exit(1)

def engine_room():
    story = """You've made it to the engine room! You now have to abandon ship or
    fix this wreck!"""

    user_input = adv_input(story, ["Pick a space suit and leave", "Attempt to repair engine controls", "Replace plasma conduit inhibitor"])

    if user_input == 1:
        print("You slowly start floating into space using tiny thrusters, hopefully someone will find you")
    elif user_input == 2:
        explode = random.randint(1, 2)    
        if explode == 2:
            print('Luck ran out, your engine has exploded and you died')
        else:
            print('You fixed the engine controls!  Away we go!')
    elif user_input == 3:
        print('You attempt to replace the plasma conduit inhibitor and get blasted with hot magma, sigh. Death again.')
                    

def adv_input(story, choices):
    print(story)
    while True:
        print('Choose an adventure!')
        for i, c in enumerate(choices):
            print(i + 1, ':' , c)
        try:
            user_input = int(input('> '))
        except:
            print('Please enter a number')
            continue               
        if user_input >= 1 and user_input <= len(choices):
            return user_input
        print("Your input is invalid, try again")

    
           
           

bedroom()