n = list(map(int,input().strip().split()))
a  = list(map(int,input().strip().split()))
b = list(map(int,input().strip().split()))
Min = max(a)
Max = min(b)
count = 0
count1 = 0
final_count = 0
i = Min
while i <= Max and i >= Min:
    for j in a:
        if i % j == 0:
            count = count + 1
    for k in b:
        if k % i == 0: 
            count1 += 1
    if count1 == len(b) and count == len(a):
                final_count += 1
    count1 = 0
    count = 0
        
    i = i + 1
print(final_count)
