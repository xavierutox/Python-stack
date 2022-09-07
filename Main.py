try:
    import logging
    logging.basicConfig(filename=f"log.log", level=logging.DEBUG)
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
                    "1. Push\n2. Pop\n3. Get Elements\n4. Get Element\n5. Get Largest Element\n6. Get Shortests Element\n7. Compare Items Size\n8. Exit\nEnter your choice: "))
                if choice == 1:
                    stack.push(str(input("Enter the element to push: ")))
                elif choice == 2:
                    stack.pop()
                elif choice == 3:
                    stack.getItems()
                elif choice == 4:
                    print(stack.getElement(int(input("Enter the index: "))))
                elif choice == 5:
                    print(stack.getLargest())
                elif choice == 6:
                    print(stack.getShortest())
                elif choice == 7:
                    stack.compareItemsSize(int(input("Enter the index 1: ")), int(
                        input("Enter the index 2: ")))
                elif choice == 8:
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
