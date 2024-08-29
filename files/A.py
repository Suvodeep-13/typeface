
class LRUCache:

    class Node:

        def __init__(self, fileId, presingedUrl) -> None:
            self.fileId = fileId
            self.presingedUrl = presingedUrl
            self.next = None
            self.prev = None
    
    head = Node(-1, -1)
    tail = Node(-1, -1)

    def __init__(self, cap) -> None:
        self.cap = cap
        self.mp = dict()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addNode(self, newNode):
        nextNode = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = nextNode
        nextNode.prev = newNode

    def deleteNode(self, delNode):
        delNext = delNode.next
        delPrev = delNode.prev
        delPrev.next = delNext
        delNext.prev = delPrev

    def get(self, fileId):
        if fileId in self.mp.keys():
            node = self.mp[fileId]
            presingedUrl = node.presingedUrl
            self.deleteNode(node)
            self.addNode(node)
            self.mp[fileId] = self.head.next
            return presingedUrl
        else:
            # add the logic to get presinged url from s3
            return -1
    
    def put(self, fileId, presingedUrl):

        # if the fileId is already present
        if fileId in self.mp.keys():
            node = self.mp[fileId]
            self.deleteNode(node)
            self.mp.pop(fileId)
        
        # check if size is full
        if self.cap == len(self.mp):
            self.mp.pop(self.tail.prev.fileId)
            self.deleteNode(self.tail.prev)

        self.addNode(self.Node(fileId, presingedUrl))
        self.mp[fileId] = self.head.next