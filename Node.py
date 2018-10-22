class Node(object):
    item = -1
    next = None

    def __init__(self, item, next):
        self.item=item
        self.next = next
    
    def __add__(self, item):
        if self.item == -1:
            self.item = item
        else:
            temp = self
            while(temp.next!=None):
                temp = temp.next
            temp.next = Node(item, None)