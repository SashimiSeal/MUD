
def welcome_screen():
    print("******************************************************")
    print("*                     WELCOME                        *")
    print("******************************************************")
    print("*                   (づ◔ ͜ʖ◔)づ                       *")


def locked_door():
    print ("  /       \ ")
    print (" |        | ")
    print (" |        | ")

def main():
    welcome_screen()
    print ("You are standing in a castle. \nA minotaur is about to charge at you.")
    input_var = input("Do you (a)Run Away or (b)Fight")
    print ("You entered " + input_var)

    if (input_var == 'a'):
        print("You got away and find yourself in a room with a beholder.")
        room2_var = input("Do you (a)try and convince it you mean no harm or (b)Try and fight it")
        print ("You entered" + room2_var)
    else:
        print("Bad move buddy. The minataur is buff and angry. He stuffs you and your head gets mounted on his wall.")

    if (room2_var == 'a'):
        print("The beholder decides to befriend you an helps you fight off the minotaur")

    else:
        print("uh oh, now you have two angry monsters on your tail.")
        corridor_var = input("(a)Right? or (b)Left?")
        print ("You entered" + corridor_var )
    if (corridor_var == 'a'):
        print ("you find yourself at a locked door")
       
# main()
locked_door()