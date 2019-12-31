def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    string = string.upper()
    vowels = ["A","E","I","O","U"]
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
    if kevin_score > stuart_score:
        print("Kevin",kevin_score)
    elif kevin_score == stuart_score:
        print("Draw")
    else:
        print("Stuart",stuart_score)
if __name__ == '__main__':
    s = input()
    minion_game(s)
