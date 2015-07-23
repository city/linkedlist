import sys
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insertAtHead(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not found in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not found in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def findMin(self):
        current = self.head
        min = current.data
        while current:
            if current.data < min:
                min = current.data
            current = current.next_node
        return min

    #def insertAtTail(self):

    def insertArrReverse(self,a):
        for x in reversed(a):
            self.insertAtHead(x)


    def printList(self):
        current = self.head
        while current:
            if(current.get_next() is None):
                sys.stdout.write(str(current.get_data())+"\n")
            else:
                sys.stdout.write(str(current.get_data())+" --> ")
            current = current.get_next()

linkedList = LinkedList()
linkedList.insertAtHead("dude")
linkedList.insertAtHead("omg")
linkedList.insertAtHead("like")
#linkedList.printList()
linkedList.delete("omg")
#a = [11,8,9,12,15,23,25,31,6,7]
#linkedList.insertArrReverse(a)
linkedList.printList()
#m = linkedList.findMin()
#print(m)
