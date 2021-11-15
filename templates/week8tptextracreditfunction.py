def find_twos_and_eights(n):
    ## Print list of all integers leading up to n:
    # nl = []
    # for i in range(n):
    #     nl.append(str(i))
    # print(nl)
    l = []
    for i in range(0, n, 2):
        l.append(str(i))
    ## Print list of all even numbers:
    # print(l)
    #
    ## Print list of all even numbers that contain 2 or 8
    # print(list(filter(lambda a: '2' in a or '8' in a, l)))
    # or
    # print(list(filter(None, [l[i] if (('2' in l[i]) or '8' in l[i]) else None for i in range(len(l))])))
    return len(list(filter(lambda a: '2' in a or '8' in a, l)))
    ## Also works:
    # return len(list(filter(None, [l[i] if (('2' in l[i]) or '8' in l[i]) else None for i in range(len(l))])))


print(find_twos_and_eights(3))
print(find_twos_and_eights(9))
print(find_twos_and_eights(19))
print(find_twos_and_eights(23))
