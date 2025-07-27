class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1 from A"
        print("A.__init__ called")

    def method_a(self):
        print("Method from A")

class B:
    def __init__(self):

        self.prop1 = "prop1 from B"
        print("B.__init__ called")

    def method_b(self):
        print("Method from B")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C.__init__ called")

    def method_c(self):
        print("Method from C")

c = C()

