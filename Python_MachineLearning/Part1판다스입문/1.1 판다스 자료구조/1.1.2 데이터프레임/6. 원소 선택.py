# 인덱스 이름 또는 정수 위치 인덱스로 데이터프레임내 원소 선택 가능

# 인덱스 이름으로 원소 선택
# 사용법 : DataFrame 객체.loc[행 인덱스, 열 이름]
# 리턴값 : 해당되는 원소 반환, 대신 1개의 행과 2개 이상의 열 또는 2개 이상의행과 1개의 열일 경우 
#          시리즈 반환, 2행 이상 2열 이상 선택시 데이터프레임 객체 반환

# 정수 위치 인덱스로 원소 선택
# 사용법 : DataFrame 객체.iloc[행 번호, 열 번호]
# 리턴값 : 해당되는 원소 반환, 대신 1개의 행과 2개 이상의 열 또는 2개 이상의행과 1개의 열일 경우 
#          시리즈 반환, 2행 이상 2열 이상 선택시 데이터프레임 객체 반환

import pandas as pd

exam_data = { '이름' : ['서준', '우연', '민아'],
              '수학' : [ 90, 80, 70],
              '영어' : [ 95, 94, 56],
              '음악' : [ 54, 34, 23],
              '체육' : [ 100, 90, 100]}
df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스로 지정 - 이는 다음장에서 배울 내용, '이름'열을 새로운 행 인덱스로 지정한다.
df.set_index('이름', inplace=True)
print(df)

# 데이터프레임에 원소 1개 선택
a = df.loc['서준', '음악']
print(a)
b = df.iloc[0, 2]
print(b)

# 결과값
#     수학  영어  음악   체육
# 이름
# 서준  90  95  54  100
# 우연  80  94  34   90
# 민아  70  56  23  100
# 54
# 54

# 데이터프레임의 원소 2개 이상 선택(2개 이상의 인덱스 배열을 리스트로 또는 슬라이싱 기법 사용)

c = df.loc['서준', ['음악', '체육']]
print(c)
d = df.iloc[0, [2, 3]]
print(d)
e = df.loc['서준', '음악':'체육']
print(e)
f = df.iloc[0, 2:]

# 결과값
# 음악     54
# 체육    100
# Name: 서준, dtype: int64
# 음악     54
# 체육    100
# Name: 서준, dtype: int64
# 음악     54
# 체육    100
# Name: 서준, dtype: int64

# 행 인덱스와 열 이름을 각각 2개 이상 선택하여 데이터프레임 반환

g = df.loc[['서준', '우연'], ['음악', '체육']]
print(g)
h = df.iloc[[0, 1], [2, 3]]
print(h)
i = df.loc['서준':'우연', '음악':'체육']
print(i)
j = df.iloc[0:2, 2:]
print(j)

# 결과값
#     음악   체육
# 이름
# 서준  54  100
# 우연  34   90
#     음악   체육
# 이름
# 서준  54  100
# 우연  34   90
#     음악   체육
# 이름
# 서준  54  100
# 우연  34   90
#     음악   체육
# 이름
# 서준  54  100
# 우연  34   90