##함수
import random

def binSearch(ary, fData):
    global count
    pos = -1
    start = 0
    end = len(ary)-1
    while start <= end:
        count += 1
        mid = (start + end) // 2
        if ary[mid] == fData:
            pos = mid
            break
        elif ary[mid] < fData :
            start = mid + 1
        else:
            end = mid - 1
            
    return pos

##변수
count = 0
dataAry = [random.randint(30, 2000000) for _ in range(100000)]
findData = random.choice(dataAry)
#findData = 999
dataAry.sort()
#속도가 빠르다

##메인
print('배열:', dataAry[:20])
position = binSearch(dataAry, findData)
if position == -1:
    print(findData,'는 없어요')
else:
    print(findData, '는', position, '위치에 있어요.(', count,'회)')