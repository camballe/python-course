started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
              
          ''')
    elif command == "start":
        if started:
            print("Car is already started!\n")
        else:
            started = True
            print("Car started...Ready to go!\n")
    elif command == "stop":
        if not started:
            print("Car is already stopped!\n")
        else:
            started = False
            print("Car stopped.\n")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that.\n")
