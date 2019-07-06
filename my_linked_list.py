class Node:
    def __init__(self, current_value=None ):
        self.current_value = current_value
        self.next_node= None

class SLinkedList:
    def __init__(self):
        self.head_node = None
    
    def trasverse_list(self):
        print_value = self.head_node
        while print_value is not None:
            print(print_value.current_value)
            print_value = print_value.next_node

    def insert_at_beggining(self, value_to_insert):
        current_node = self.head_node
        if current_node is None:
            print('List has no head')
            return
        self.head_node = Node(value_to_insert)
        self.head_node.next_node = current_node
    
    def insert_at_end(self, value_to_insert):
        current_node = self.head_node
        if current_node is None:
            self.head_node = Node(value_to_insert)
            return
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = Node('4')

    def insert_after_node(self, value_before, value_to_insert):
        current_node = self.head_node
        while current_node.current_value != value_before:
            current_node = current_node.next_node
        node_after = current_node.next_node
        current_node.next_node = Node(value_to_insert)
        current_node.next_node.next_node = node_after

    def removing_unique_value(self, value_to_remove):
        current_node =  self.head_node
        while current_node.current_value != value_to_remove:
            prev_node = current_node
            current_node = current_node.next_node
        prev_node.next_node = current_node.next_node
        current_node = None
        

if __name__ == '__main__':
    print('Creating list')
    list1 = SLinkedList()
    n1 = Node('1')
    n2 = Node('2')
    n3 = Node('3')
    list1.head_node = n1
    n1.next_node = n2
    n2.next_node = n3
    list1.trasverse_list()
    print('Inserting 0 at beginning')
    list1.insert_at_beggining('0')
    list1.trasverse_list()
    print('inserting 4 at end')
    list1.insert_at_end('4')
    list1.trasverse_list()
    print('inserting 3.5 between 3 and 4')
    list1.insert_after_node('3','3.5')
    list1.trasverse_list()
    print('inserting 4.5 after 4')
    list1.insert_after_node('4','4.5')
    list1.trasverse_list()
    print('removing 3')
    list1.removing_unique_value('3')
    list1.trasverse_list()
    print('removing 4')
    list1.removing_unique_value('4')
    list1.trasverse_list()
