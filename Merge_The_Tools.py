def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        s = ""
        for j in string[i:i+k]:
            if j not in s:
                s += j
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
