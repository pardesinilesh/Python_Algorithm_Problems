def solution(N):
    num = binary = format(N, "06b")
    char = str(num)
    find=False
    result, conteur=0, 0

    for c in char:
        if c=='1' and not find:
            find = True

        if find and c=='0':
            conteur+=1

        if c=='1':
            if result<conteur:
                result=conteur
            conteur=0

    return result
