class A:

    def __init__(self) -> None:
        super().__init__()
        print('A')
        
class B(A):

    def __init__(self) -> None:
        super().__init__()
        print('B')
        
class X:
    
    def __init__(self) -> None:
        super().__init__()
        print('X')
        

class Forward(B, X):

    def __init__(self) -> None:
        super().__init__()
        print('Forward')

class Backward(X, B):

    def __init__(self):
        super().__init__()
        print('Backward')

forward = Forward()
backward = Backward()

print(Forward.__mro__())
