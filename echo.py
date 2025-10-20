import sys

def echo():
    shout = "--s" in sys.argv
    message = input("Please enter something: ")
    print(message.upper() if shout else message)

if __name__ == "__main__":
    echo()# Echo Application - Type a message and it will be echoed back
