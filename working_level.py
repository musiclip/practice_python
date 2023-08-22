## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end = ' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()
    
def insertNode(findData, insertData):
    global memory, head, pre, current
    # Case 1 : 머리 앞에 삽입
    if (findData == head.data):
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # Case 2 : 중간 노드 앞에 삽입
    current = head
    while(current.link != None) :
        pre = current
        current = current.link
        if (current.data == findData):
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # Case 3 : 없는 노드 앞에 삽입 (재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData):
    global memory, head, pre, current
    # Case1 : 머리를 삭제
    if (deleteData == head.data):
        current = head
        head = head.link
        del(current)
        return
    # Case 2 : 중간을 삭제
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (current.data == deleteData):
            pre.link = current.link
            del(current)
            return
    # Case 3 : 없는걸 지울때
    return

def findNode(findData):
    global memory, head, pre, current
    current = head
    if (findData == current.data):
        return current
    while (current.link != None):
        current = current.link
        if (findData == current.data):
            return current
    return Node()


## 전역
memory = []
head, pre, current = None, None, None
dataArray = ['다현','정연','쯔위','사나','지효'] # 작은 데이터건 큰 데이터건 다 돌아가게


## 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # C++에서 중요

for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)
    
#printNodes(head)
#insertNode('다현','화사')
#printNodes(head)
#insertNode('사나','솔라')
#printNodes(head)
#insertNode('재남','문별')
#printNodes(head)
#deleteNode('다현')
#printNodes(head)
#deleteNode('쯔위')
#printNodes(head)
#deleteNode('재남')
#printNodes(head)
retNode = findNode('사나')
print(retNode.data, '뮤비가 나옵니다. 쿵짝쿵짝~~')
