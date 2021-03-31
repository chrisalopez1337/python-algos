class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
	start = head.next
	second = head.next.next
	while start != second:
		start = start.next
		second = second.next.next
	start = head
	while start != second:
		start = start.next
		second = second.next
	return start

