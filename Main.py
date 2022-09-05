try:
    import time
except ImportError:
    logging.error("time.py not found")
    exit()
try:
    import logging
    date = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    logging.basicConfig(filename=f"log_{date}.log", level=logging.DEBUG)
except ImportError:
    print("Logging.py not found")
    exit()
try:
    import Stack
except ImportError:
    logging.error("Stack.py not found")
    exit()


if __name__ == "__main__":
    try:
        stack = Stack.Stack()
    except:
        logging.error("Could not create stack")
    while True:
        try:
            try:
                choice = int(input(
                    "1. Push\n2. Pop\n3. Get Element\n4. Get Largest Element\n5. Compare Items Size\n6. Get Items\n7. Exit\nEnter your choice: "))
                if choice == 1:
                    stack.push(str(input("Enter the element to push: ")))
                elif choice == 2:
                    stack.pop()
                elif choice == 3:
                    print(stack.getElement(int(input("Enter the index: "))))
                elif choice == 4:
                    print(stack.getLargest())
                elif choice == 5:
                    stack.compareItemsSize(int(input("Enter the index 1: ")), int(
                        input("Enter the index 2: ")))
                elif choice == 6:
                    stack.getItems()
                elif choice == 7:
                    exit()
            except ValueError:
                print("Invalid choice")
                continue
        except KeyboardInterrupt:
            logging.info("\n Received keyboard interrupt, exiting...")
            print("Exiting...")
            exit()
else:
    logging.error("Please run this file directly")
