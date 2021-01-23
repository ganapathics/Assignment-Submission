def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

a="PHYTHON IS GREATE AND ABAP IS ALSO GREAT "
a=' '.join(unique_list(a.split()))
print(a)