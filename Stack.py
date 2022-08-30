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