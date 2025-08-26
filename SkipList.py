import random
class SkipListNode:
    class Node:
        def __init__(self, value):
            self.value=value
            self.next=None
            self.down=None
    def __init__(self):
        self.head=self.Node(None)


    def _search(self, value):
        last_nodes   = []
        current_node = self.head

        while True:
            if current_node.next is not None and current_node.next.value <= value:
                current_node = current_node.next
            else:
                last_nodes.append(current_node)
                if current_node.down is not None:
                    current_node = current_node.down
                else:
                    break
        return last_nodes
    
    def search(self, value):
        last_nodes = self._search(value)

        if last_nodes[-1].value == value:
            return value

        return None
    
    def insert(self, new_value):

        last_nodes = self._search(new_value)

        if last_nodes[-1].value == new_value:
            return

        last_created_node = None
        while True:
            new_node = self.Node(new_value)

            if len(last_nodes) > 0:
                last_node       = last_nodes.pop()
                new_node.next   = last_node.next
                last_node.next  = new_node
            else:
                new_head       = self.Node(None)
                new_head.down  = self.head
                new_head.next  = new_node
                new_node.next  = None
                self.head      = new_head

            new_node.down      = last_created_node
            last_created_node  = new_node

            if random.randint(0, 1) != 0:
                break
    
    
    def remove(self, value):
        current_node = self.head

        while True:
            if current_node.next is not None and current_node.next.value <= value:
                if current_node.next.value < value:
                    current_node = current_node.next
                else:
                    current_node.next = current_node.next.next

                if current_node.value is None and current_node.next is None and current_node.down is not None:
                    self.head = current_node.down
            else:
                if current_node.down is not None:
                    current_node = current_node.down
                else:
                    break
