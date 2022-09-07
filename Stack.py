import logging
import time

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        try:
            self.items.append(item)
            logging.info(f"{time.strftime('%H:%M:%S', time.localtime())} Added element to top of stack: {item}")
        except:
            logging.error(f"{time.strftime('%H:%M:%S', time.localtime())} Invalid input, input recieved: {item}")
            print("Invalid input")

    def pop(self):
        try:
            logging.info(
                (f"{time.strftime('%H:%M:%S', time.localtime())} Removed element in top of stack: {self.getElement(-1)}"))
            self.items.pop()
        except IndexError:
            logging.error(
                f"{time.strftime('%H:%M:%S', time.localtime())} Tried to remove element from stack, but stack is empty")
            print("Can't remove element, stack is empty")
        return

    def getElement(self, index):
        if self.isEmpty():
            logging.warning(f"{time.strftime('%H:%M:%S', time.localtime())} Trying to get element, but stack is empty")
        try:
            logging.info(
                f"{time.strftime('%H:%M:%S', time.localtime())} Returning element at index {index}: {self.items[index]}")
            return self.items[index]
        except IndexError:
            logging.error(f"{time.strftime('%H:%M:%S', time.localtime())} index out of range")
            print("Can't get element, index out of range")
            return

    def isEmpty(self):
        return self.items == []

    def getItems(self):
        if self.isEmpty():
            logging.warning(f"{time.strftime('%H:%M:%S', time.localtime())} Stack is empty")
            print("Stack is empty, can't get items")
            return
        for i in reversed(self.items):
            print(f"[{self.items.index(i)}]. {i} \n")
        return

    def getLargest(self):
        if self.isEmpty():
            logging.warning(
                f"{time.strftime('%H:%M:%S', time.localtime())} trying to get largest element, but stack is empty")
            print("Stack is empty, can't get largest element")
            return
        else:
            return max(self.items, key=len)

    def getItemSize(self, item):
        if self.isEmpty():
            logging.error(f"{time.strftime('%H:%M:%S', time.localtime())} Trying to get size of {item}, but Stack is empty")
            return
        try:
            return len(item)
        except TypeError:
            logging.error(f"{time.strftime('%H:%M:%S', time.localtime())} Invalid input, not a string, recieved {item}")
            return

    def compareItemsSize(self, index1, index2):
        try:
            if self.getItemSize(self.getElement(index1)) > self.getItemSize(self.getElement(index2)):
                print(f"Item 1 ({self.getElement(index1)}) is larger")
                logging.info(
                    f"{time.strftime('%H:%M:%S', time.localtime())} Input 1 {index1}, input 2 {index2}, result {self.getElement(index1)} is larger")
            elif self.getItemSize(self.getElement(index1)) < self.getItemSize(self.getElement(index2)):
                logging.info(
                    f"{time.strftime('%H:%M:%S', time.localtime())} Input 1 {index1}, input 2 {index2}, result {self.getElement(index2)} is larger")
                print(f"Item 2 ({self.getElement(index2)}) is larger")
            else:
                logging.info(
                    f"{time.strftime('%H:%M:%S', time.localtime())} Input 1 {index1}, input 2 {index2}, result {self.getElement(index1)} is equal")
                print("Items are equal")
        except ValueError:
            print("Could not compare items")
            logging.error(f"{time.strftime('%H:%M:%S', time.localtime())} Invalid input, input recieved: {index1} {index2}")
            return
        except IndexError:
            print("Could not compare items")
            logging.error(
                f"{time.strftime('%H:%M:%S', time.localtime())} Index out of range, input recieved: {index1} {index2}")
            return
        except TypeError:
            print("Could not compare items")
            logging.error(f"{time.strftime('%H:%M:%S', time.localtime())} Invalid input, recieved {index1} {index2}")
            return
        except:
            logging.error(f"{time.strftime('%H:%M:%S', time.localtime())} unexpected error, recieved {index1} {index2}")
            print("Could not compare items")
            return
