class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        try: 
            self.items.append(item)
        except Exception as e:
            print(e)

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            print("Stack is empty")
        return
    
    def getElement(self, index):
        try:
            return self.items[index]
        except IndexError:
            print("Stack is empty")
            return
    
    def isEmpty(self):
        return self.items == []
    
    def getItems(self):
        for i in reversed(self.items):
            print(f"[{self.items.index(i)}]. {i} \n")
    
    def getLargest(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        else:
            return max(self.items, key=len)
    
    def getItemSize(self, item):
        if self.isEmpty():
            print("Stack is empty")
            return
        try:
            return len(item)
        except TypeError:
            print("Invalid input, not a string")
            return
    
    def compareItemsSize(self, index1, index2):
        try:
            if self.getItemSize(self.getElement(index1)) > self.getItemSize(self.getElement(index2)):
                print(f"Item 1 ({self.getElement(index1)}) is larger")
            elif self.getItemSize(self.getElement(index1)) < self.getItemSize(self.getElement(index2)):
                print(f"Item 2 ({self.getElement(index2)}) is larger")
            else:
                print("Items are equal")
        except ValueError:
            print("Invalid input")
            return
        except IndexError:
            print("Index Out of Range")
            return
        except TypeError:
            print("Invalid input, not a string")
            return