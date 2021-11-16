# add2 = lambda n1, n2 : n1 + n2
#
# print(add2(100,200))

class User:
    #생성자 생성
    # toString
    def __str__(self):
        return self.name
    def __init__(self,name):
        self.name = name

#객체생성
user = User("파이썬")
print(user)

#주소값과 해당타입에서 사용가능한 함수목록
x=100
print(id(x))
print(dir(x))
"""
라인주석이다 ~ 
"""