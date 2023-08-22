### 함수 선언부


### 전역 변수부
katok = ['다현','정연','쯔위','사나','지효']

### 메인 코드부
print(katok)

## 데이터 추가
katok.append(None)
katok[5] = '모모'
print(katok)

## 데이터 삽입
# 1단계 - 빈칸 추가
katok.append(None)
# 2단계 - 한칸씩 이동
katok[6] = katok[5]
katok[5] = None
katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
# 3단계 - 데이터 삽입
katok[3] = '미나'
print(katok)

## 데이터 삭제
# 1단계 - 원하는 데이터 제거
katok[4] = None
# 2단계 - 한칸씩 앞으로 이동
katok[4] = katok[5]
katok[5] = None
katok[5] = katok[6]
katok[6] = None
# 3단계 - 마지막 칸 제거
del(katok[6])
print(katok)