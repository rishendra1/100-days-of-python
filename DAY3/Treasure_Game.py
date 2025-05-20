print("Welcome to the Treasure Island Your measure is to find the Treasure")
print('''                          _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \,.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|'||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
               '-._'-.|| |' `_.-'
                    '-.||_/.-  ''')
choice1 = input("You are at crossroads, where do you want to go (Left or Right)")
if choice1 == "Left" or choice1 == "left":
    choice2 = input("You have come to a lake, there is an Island, \nif you want to swim(Type Swim) or if you want to wait(Type wait)")
    if choice2 == "Wait" or choice2 == "wait":
        choice3 = input("Now, there are 3 doors select any one - \"Red,Blue,Yellow\" - ")
        if choice3 == "Red" or choice3 == "red" or choice3 == "Blue" or choice3 == "blue" :
            print("Game Over")
        if choice3 == "Yellow" or choice3 == "yellow" :
            print("You win")
    else:
        print("Game Over")
else:
    print("Game Over")