time = 13
sick = False
if 12 <= time < 1 and not sick:
    print("점심 먹으러감")
elif 3 <= time <= 4 or sick:
    print("휴식")
else:
    print("일하는 중")

a = 10
if a > 10:
    ret = 100
elif a == 10:
    ret = 200
else:
    ret = 500
ret = {a > 10:100, a<10:500}.get(True,200)

name = "abcdef"
if "a" in name:
    print("있음")
else:
    print("없음")

name = ["홍길동", "가제트", "나루토"]
if "나루토" in name:
    print("있음")
else:
    print("없음")


guest = 1 
while guest < 10:
    guest += 1
    print("손님은 {}명입니다.".format(guest))
    if guest == 10:
        print("손님이 꽉찼습니다. ")

num = 1
jjak = 0
hol = 0
while num <= 10:
    if num % 2 == 0:
        print("짝수 {}".format(num))
        jjak += num
    else:
        print("홀수 {}".format(num))
        hol += num
    num += 1
print("홀수의 합 {}입니다".format(hol))
print("짝수의 합 {}입니다".format(jjak))

a = "abcdef"
for i in a:
    print(i)

a = ["python","java","c"]
for i in a:
    print(i)

for i in range(0,101,10):
    print(i)

a = [(1,2), (3,4),(5,6)]
for i in a:
    for j in i:
         print(j)

student = [{"홍길동":100}, {"가가멜:":200},{"나루토":400}]
for i in student:
    print(i)

student = [{"홍길동":100}, {"가가멜:":200},{"나루토":400}]
for s, i in enumerate(student, start=1):
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("{} 이름 : {} / 점수 : {}".format(s,name,value))

result = [num + 5 for num in range(1,6)]
print(result)

result = [num + 5 for num in range(1,10) if num % 2 == 0]
print(result)





