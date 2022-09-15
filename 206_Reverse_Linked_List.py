class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode =nextNode

node1 = LinkedListNode('1')
node2 = LinkedListNode('2')
node3 = LinkedListNode('3')
node4 = LinkedListNode('4')
node5 = LinkedListNode('5')

node1.nextNode = node2 
node2.nextNode = node3 
node3.nextNode = node4 
node4.nextNode = node5 


currentNode = node1
# while True:
#     print(currentNode.value)
#     if currentNode.nextNode is None:
#         print(None)
#         break
#     currentNode =currentNode.nextNode
 

head = node1
def reverseLinkedList(head):
    
    prev_temp = None
    currentNode = head
    

    while currentNode:
        next_temp            = currentNode.nextNode
        currentNode.nextNode = prev_temp
        prev_temp            = currentNode
        currentNode          = next_temp

    print(prev_temp.value) 


reverseLinkedList(head)
