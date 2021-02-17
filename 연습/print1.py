# print 함수

# print 1
print("하나", "둘", "셋", "1", "2", "3")
print("하나", "둘", "셋", "1", "2", "3", sep='-') # sep : 출력시 출력대상들 사이에 구분자를 넣을 때

print("첫번째 값")
print("두번째 값") # 다른 줄에 출력됨

print("첫번째 값", end="--->")          # end : string appended after the last value, default a newline.
print("두번째 값") # 같은 줄에 출력

print("첫번째 값", end="--->")
print("두번째 값")                  # end와 같은 줄에 출력
print("세번째 값")                  # 다음줄에 출력

file = open("test.txt","w")
print("Hello Python!", file=file) # 파일로 출력 (text.txt 파일이 생성됨)
file. close()

