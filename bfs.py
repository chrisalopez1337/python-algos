# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
		que = [self]
		while len(que) > 0:
			item = que.pop(0)
			array.append(item.name)
			i = 0 
			while i < len(item.children):
				que.append(item.children[i])
				i += 1
		return array
