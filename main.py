from bot.duckie import Duckie


def main():
    duckie = Duckie('Duckie')
    # prompt the user to enter a message and loop until the user enters 'bye'
    # for each message, print the duckie's response
    print("Hello, I'm Duckie. I'm a duck. To exit, type 'bye'.")
    while True:
        message = input('> ')
        if message == 'bye':
            break
        print(duckie.prompt(message))


if __name__ == '__main__':
    main()

