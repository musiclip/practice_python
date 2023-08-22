## 함수
#class TreeNode():
 #   def __init__(self):
  ##      self.left = None
   #     self.data = None
    #    self.right = None

## 변수
#memory = []
#root = None
#nameAry = ['블랙핑크','레드벨벳','에이핑크','걸스데이','트와이스','마마무']

## 메인
#node = TreeNode()
#node.data = nameAry[0]
#root = node
#memory.append(node)

#for name in nameAry[1:]:
   # node = TreeNode()
    #node.data = name
    
    #current = root
    #while True:
        #if name < current.data :
            #if current.left == None:
           #     current.left = node
          #      break
         #   current = current.left
        #else:
            #if current.right == None:
             #   current.right = node
            #    break
           # current = current.right
   # memory.append(node)
    
#print('이진탐색 트리 구현 완료')

## 함수
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 변수
memory= []
root = None
nameAry = ['블랙핑크', '레드벨드', '에이핑크', '걸스데이', '트와이스', '마마무' ] # 여러분 데이터
## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] : # ['레드벨드', '마마무', ...
    node = TreeNode()
    node.data = name

    currrent = root
    while True :
        if (name < currrent.data) :
            if (currrent.left == None) :
                currrent.left = node
                break
            currrent = currrent.left
        else :
            if (currrent.right == None) :
                currrent.right = node
                break
            currrent = currrent.right

    memory.append(node) # 안 중요!

print('이진 탐색 트리 구성 완료!')

findData = '마마무'
currrent = root
while True :
    if findData == currrent.data :
        print(findData, '찾았다.')
        break
    elif findData < currrent.data :
        if currrent.left == None:
            print(findData,'없다.')
            break
        currrent = currrent.left
    else:
        if currrent.left == None:
            print(findData,'없다.')
            break
        currrent = currrent.right