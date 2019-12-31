s = input()
count_list = []
List = []
for i in range(len(s)):
    count = 1
    for j in range(i+1,len(s)):
        if s[i] == s[j]:
            count += 1
            count_list.append(count)
            List.append([s[i],count])
if len(List) < 3:
    List.append([s[-1],1])
print(count_list)
