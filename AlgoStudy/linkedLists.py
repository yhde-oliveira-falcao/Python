# First, we make a Node (a train car)
class Node:
    def __init__(self, value):
        self.value = value      # This is what’s inside the car
        self.next = None        # This points to the next car

# Then we build the train (LinkedList)
class LinkedList:
    def __init__(self):
        self.head = None  # The first car of the train

    # Add a new car at the end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node  # First car
        else:
            current = self.head
            while current.next:  # Go to the end
                current = current.next
            current.next = new_node  # Attach the new car

    # Show all the cars
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


my_train = LinkedList()
my_train.append("Engine")
my_train.append("Car A")
my_train.append("Car B")
my_train.print_list()
