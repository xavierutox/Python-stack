try:
    import Stack
except ImportError:
    print("Stack.py not found")
    exit()

try:
    import Logging
except ImportError:
    print("Logging.py not found")
    exit()

if __name__ == "__main__":
    try:
        stack = Stack.Stack()
    except:
        print("Could not create stack")
    while True:
        try:
            try:
                choice = int(input("1. Push\n2. Pop\n3. Exit\nEnter your choice: "))
            except ValueError:
                print("Invalid input")
                continue
        except KeyboardInterrupt:
            print("\nExiting...")
            break
else:
    print("Please run this file directly")