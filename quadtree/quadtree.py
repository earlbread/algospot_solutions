#/usr/bin/python3

def solution(s):
    if s[0] == 'w' or s[0] == 'b':
        return s[0], 1

    index = 1

    upper_left, x = solution(s[index:])
    index += x
    upper_right, x = solution(s[index:])
    index += x
    lower_left, x = solution(s[index:])
    index += x
    lower_right, x = solution(s[index:])
    index += x

    return 'x' + lower_left + lower_right + upper_left + upper_right, index

if __name__ == '__main__':
    testcases = int(input())

    for t in range(testcases):
        s = input()
        print(solution(s)[0])
