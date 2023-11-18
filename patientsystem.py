#/usr/bin/python3
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        class details:
            def __init__(self):
                self.head = None
                def listprint(self):
                    val = self.head
                    print("Linked List")
                    while val is not None:
                        print(val.data)
                        val = val.next
                        L1 = details()
                        L1.head = node()
                        L2 = node()
                        L3 = node()
                        L4 = node()
                        L1.head.next = L2
                        L2.next = L3
                        L3.next = L4
                        L1.listprint()
