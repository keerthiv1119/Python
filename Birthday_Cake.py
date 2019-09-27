n = int(input())
s = list(map(int,input().strip().split()))
List = list(map(int,input().strip().split()))
count = 0
for i in range(len(s)- List[1] +1):
    Sum = 0
    for j in range(List[1]):
        Sum += s[i + j]
    if Sum == List[0]:
        count += 1
print(count)
