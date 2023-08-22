## 함수
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen -1] = friend
    
def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1,position,-1):
        katok[i] = katok[i -1]
        katok[i -1] = None
    katok[position] = friend
        
def delete_data(position):
    katok[position] = None
    kLen = len(katok)
    for i in range(position +1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del katok[kLen-1]

## 전역
katok = []

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)
insert_data(3, '미나')
print(katok)
delete_data(4)
print(katok)

select = int(input('선택하세요(1:추가, 2:삽입, 3:삭제, 4:종료) -->'))

while (select != 4):
    
    if (select == 1):
        data = input('추가할 데이터 -->')
        add_data(data)
        print(katok)
        
    elif (select == 2):
        position = int(input('삽입할 위치 -->'))
        data = input('추가할 데이터 -->')
        insert_data(position, data)
        print(katok)
        
    elif (select == 3):
        postition = int(input('삭제할 위치 -->'))
        delete_data(position)
        print(katok)
        
    elif (select == 4):
        print(katok)
        exit
        
    else:
        print('1~4 중 하나를 입력하세요.')
        continue