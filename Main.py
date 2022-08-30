try:
    import Stack
except ImportError:
    print("Stack.py not found")
    exit()

try:
    import logging
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
                choice = int(input("1. Push\n2. Pop\n3. Get Element\n4. Get Largest Element\n5. Compare Items Size\n6. Get Items\n7. Exit\nEnter your choice: "))
                if choice == 1:
                    try:
                        stack.push(str(input("Enter the element to push: ")))
                    except ValueError:
                        print("Invalid input")
                elif choice == 2:
                    stack.pop()
                elif choice == 3:
                    try:
                        print(stack.getElement(int(input("Enter the index: "))))
                    except ValueError:
                        print("Invalid input")
                elif choice == 4:
                    print(stack.getLargest())
                elif choice == 5:
                    try:
                        stack.compareItemsSize(int(input("Enter the index 1: ")), int(input("Enter the index 2: ")))
                    except ValueError:
                        print("Invalid input")
                elif choice == 6:
                    stack.getItems()
                elif choice == 7:
                    exit()
            except ValueError:
                print("Invalid input")
                continue
        except KeyboardInterrupt:
            print("\nExiting...")
            break
else:
    print("Please run this file directly")