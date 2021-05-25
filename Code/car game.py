# Solution
command = ""
started = False

while True:
    command = input('>').lower()        # want this always inside the while loop; otherwise, will print infinitely
    if command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == 'start':
        if started:
            print("Car is already started!")
        else:
            started = True
            print('Starting the car...')
    elif command == 'stop':
        if not started:
            print("Car stopped already")
        else:
            started = False
            print('Stopping the car...')
    elif command == 'quit':
        break
    else:
        print("I don't understand that")