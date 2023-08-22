##함수
def isStackFull() :
    global SIZE, stack, top
    if (top == SIZE -1):  # >= -1도 가능
        return True
    else :
        return False
    
def push(data):
    global SIZE, stack, top
    if (isStackFull() == True):
        print('스택이 꽉참')
        return
    top += 1
    stack[top] = data
        
def pop():
    global SIZE, stack, top
    if (isStackEmpty()): #== True):
        print('스택이 텅 비었다.')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data
    
    
def isStackEmpty():
    global SIZE, stack, top
    if (top == -1): # <=-1도 가능
        return True
    else:
        return False
    
def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('스택 텅~~')
        return
    return stack[top]
    
    
##전역
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1


##메인
push('커피')
push('녹차')
#push('꿀물')
#push('환타')
#push('콜라')
#push('게토레이')

print('바닥:', stack)
retData = pop()
print('팝 데이터 --> ', retData)
print('다음 예정:', peek())

retData = pop()
print('팝 데이터 --> ', retData)
retData = pop()
print('팝 데이터 --> ', retData)
print('바닥:', stack)

select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 -->')
while (select != 'X' and select !='x'):
    if select == 'I' or select == 'i':
        data = input('입력할 데이터: ==>')
        push(data)
        print('스택 상태: ',stack)
    elif select == 'E' or select == 'e':
        data = pop()
        print('추출된 데이터 ==>', data)
        print('스택 상태: ', stack)
    elif select == 'V' or select =='v':
        data == peek()
        print('확인된 데이터 ==>', data)
        print('스택 상태:', stack)
    else:
        print('입력이 잘못됨')
    
    select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 -->')

print('프로그램 종료!')
        