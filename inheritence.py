class A:
    def feature1(self):
        print('feature1 is working')

    def feature2(self):
        print('feature2 is working')

class B:
    def feature3(self):
        print('feature3 is working')

    def feature4(self):
        print('feature4 is working')

class C(B,A):
    def feature5(self):
        print('feature5 is working')

a1 = A()
a1.feature1()
a1.feature2()

B1=B()
B1.feature3()

C1 = C()
C1.feature2()
C1.feature4()
C1.feature5()
