# Definition for singly-linked list.
class Node(object):
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        return str(self.data)


class ChainTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def append(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1

        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        if self.isEmpty():
            print "this chain table is empty."
            return

        if index < 0 or index >= self.length:
            print 'error: out of index'
            return

        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            prev._next = node._next
            self.length -= 1

    def insert(self, index, dataOrNode):
        if self.isEmpty():
            print "this chain tabale is empty"
            return

        if index < 0 or index >= self.length:
            print "error: out of index"
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def update(self, index, data):
        if self.isEmpty() or index < 0 or index >= self.length:
            print 'error: out of index'
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        if j == index:
            node.data = data

    def getItem(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            print "error: out of index"
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        return node.data

    def getIndex(self, data):
        j = 0
        if self.isEmpty():
            print "this chain table is empty"
            return
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1

        if j == self.length:
            print "%s not found" % str(data)
            return

    def clear(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            return "empty chain table"
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist

    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print "error: out of index"
            return
        return self.getItem(ind)

    def __setitem__(self, ind, val):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print "error: out of index"
            return
        self.update(ind, val)

    def __len__(self):
        return self.length


class Solution(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def addTwoNumbers(self, l1, l2, res):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        for i in range(l1.length):
            res[l1.length - i - 1] = res[l1.length - i - 1] + (l1[i] + l2[i]) % 10
            if l1.length - i - 2 >= 0:
                res[l1.length - i - 2] = res[l1.length - i - 2] + (l1[i] + l2[i]) / 10

        for i in range(len(res)-1):
            print res[i]
        #print res
        return res


L1 = ChainTable()
L1.append(5)
L1.append(4)
L1.append(3)

L2 = ChainTable()
L2.append(5)
L2.append(6)
L2.append(4)

res = ChainTable()
for i in range(L1.length + 1):
    res.append(0)

s = Solution()
s.addTwoNumbers(L1, L2, res)
