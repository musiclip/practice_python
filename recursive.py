##함수
#def openBox():
#    print('상자를 엽니다')
#    openBox()
def openBox():
    global count
    print('상자 열기')
    count -= 1
    if count == 0:
        print('##선물 넣기##')
        return
    openBox()
    print('상자 닫기')
    
    
##메인
#openBox()
count = 10
openBox()

##함수
def addNumber(num):
    if num <= 1 :
        return 1
    return num + addNumber(num-1)

##메인
print(addNumber(100))

factValue = 1
for n in range(10, 0, -1):
    factValue *= n
print('10*9*...*1 = ',factValue)
##함수
def factorial(num):
    if num <= 1:
        print('1 반환')
        return 1
    print('%d * %d! 호출' % (num, num-1))
    retVal = factorial(num-1)
    
    print('%d * %d!(=%d) 반환' % (num, num -1, retVal))
    return num * retVal

##메인
print('\n5! = ', factorial(5))

##함수
def countDown(n):
    if n==0:
        print('발사!')
    else:
        print(n)
        countDown(n-1)
        
##메인
countDown(5)

##함수
def printStar(n):
    if n > 0:
        printStar(n-1)
        print('★'*n)
##메인
printStar(5)

##함수
def gugu(dan, num):
    print('%d x %d = %d' % (dan, num, dan*num))
    if num < 9:
        gugu(dan, num+1)
        
##메인
for dan in range(2, 10):
    print('## %d단 ##' %dan)
    gugu(dan, 1)
    
    
##함수
tab = ''
def pow(x,n):
    global tab
    tab += ' '
    if n == 0:
        return 1
    print(tab + '%d * %d^(%d - %d)'%(x,x,n,1))
    return x * pow(x,n-1)
##메인
print('2^4')
print('답 -->',pow(2,4))

##함수
import random

def arySum(arr, n):
    if n <= 0:
        return arr[0]
    return arySum(arr, n-1) + arr[n]

##메인
ary = [random.randint(0, 255) for _ in range(random.randint(10, 20))]
print(ary)
print('배열 합계 -->', arySum(ary, len(ary)-1))