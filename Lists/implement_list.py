# methods in list
# append - Done
# length - Done
# print - Done
# pop
# [1, 2, 3, 4, 5]


class Node:
    
    def __init__(self, value):
        self.data = value
        self.next = None

class List:

    def __init__(self) -> None:
        
        self.tail = None
        self.head = None
        self.len = None

    def append(self,data):
        
        new_data = Node(data)

        if self.tail is None:
            self.head = new_data
            self.tail = new_data
            self.len = 1
        else:
            self.tail.next = new_data
            self.tail = new_data
            self.len += 1

    def print(self):

        if self.head is None:
            print('[]')
        else:
            read_data = self.head
            value = None
            while(read_data):
                if value is None:
                    value = str(read_data.data)
                else:
                    value = value + ',' + str(read_data.data)
                read_data = read_data.next
            
            print('[' + value + ']')

    def length(self):
        print(self.len)

    def pop(self):

        if self.head is None:
            print("List is Empty")
        else:
            new_tail = self.head

            if self.head == self.tail:
                print(self.head.data)
                self.head = None
                self.tail = None
                self.len -= 1

            while(new_tail.next):
                if new_tail.next == self.tail:
                    print(self.tail.data)
                    self.tail = new_tail
                    self.tail.next = None
                    self.len -= 1
                else:
                    new_tail = new_tail.next

                
     


list = List()
list.append(10)
list.append(10)
list.append(10)
list.print()
list.length()
list.pop()
list.pop()
list.pop()
list.pop()
list.pop()
list.print()
list.length()

''' expected output
[10,10,10]
3
10
10
10
List is Empty
List is Empty
[]
0
'''
