class Node:
    def __init__(self, current_value=None):
        self.current_value = current_value
        self.prev_node = None
        self.next_node = None
    
class DLinkedList:
    def __init__(self):
        self.head_node = None

    def traverse_list(self, starting_value, direction='forward'):
        current_node = self.head_node

        if current_node.current_value is None:
            print('List has no head node')
            return

        if direction not in ['forward', 'backward']:
                print('invalid direction. Please specify forward or backward')
                return
        
        should_print = False
        while current_node is not None:
            if current_node.current_value == starting_value:
                should_print = True
            if should_print:
                print(current_node.current_value)
                if direction == 'forward':
                    current_node = current_node.next_node
                else:
                    current_node = current_node.prev_node
            else:
                current_node = current_node.next_node

    def push(self, value_to_push):
        current_head = self.head_node
        self.head_node = Node(value_to_push)
        if current_head is not None:
            self.head_node.next_node = current_head
            current_head.prev_node = self.head_node

    def append(self, value_to_append):
        current_node = self.head_node
        if current_node is None:
            self.head_node = Node(value_to_append)
            return
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = Node(value_to_append)
        current_node.next_node.prev_node = current_node

    def inserting_after_node(self, before_value, value_to_insert):
        current_node = self.head_node
        if current_node is None:
            print('List has no head')
            return
        while current_node.current_value != before_value:
            current_node = current_node.next_node
        n = Node(value_to_insert)
        n.next_node = current_node.next_node
        n.prev_node = current_node
        current_node.next_node = n

    def remove_unique_node(self, value_to_remove):
        current_node = self.head_node
        while current_node.current_value != value_to_remove:
            prev_node = current_node
            current_node = current_node.next_node
        prev_node.next_node = current_node.next_node
        current_node.next_node.prev_node = prev_node
        current_node = None


if __name__ == "__main__":
    print('creating doubly linked list')
    n1 = Node('1')
    n2 = Node('2')
    n3 = Node('3')
    list1 = DLinkedList()
    list1.head_node = n1
    n1.next_node = n2
    n2.prev_node = n1
    n2.next_node = n3
    n3.prev_node = n2
    list1.traverse_list('3', 'rubbish')
    print('*******')
    list1.traverse_list('2', 'forward')
    print('*******')
    list1.traverse_list('3', 'backward')
    print('*******')
    list1.traverse_list('1', 'backward')
    print('*******')
    list1.traverse_list('1', 'forward')
    print('pushing 0 to doubly linked list')
    list1.push('0')
    list1.traverse_list('0', 'forward')
    print('appending 4 to doubly linked list')
    list1.append('4')
    list1.traverse_list('0', 'forward')
    print('inserting 3.5 after 3')
    list1.inserting_after_node('3', '3.5')
    list1.traverse_list('0', 'forward')
    print('removing 3.5')
    list1.remove_unique_node('3.5')
    list1.traverse_list('0', 'forward')



