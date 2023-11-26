from linked_lists_func import Node, LinkedList

llist = LinkedList()

llist.head = Node("Monday")
tuesday = Node("Tuesday")
wednesday = Node("Wednesday")

llist.head.next = tuesday
tuesday.next = wednesday

# Add new element to the head of the list
llist.push("Sunday")

llist.insert_after(llist.head.next.next, "Tuesday evening")

# Add new element to the end of the list
llist.append("Thursday")

# Delete element
llist.delete_node("Tuesday evening")
llist.print_list()