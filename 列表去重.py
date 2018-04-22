# 已知某列表中包含重复数据，保持列表中元素第一次出现的顺序并去重，要求复杂度为O(n)
def fun(l):
    ll = []
    t = set()
    for i in l:
        if i not in t:
            t.add(i)
            ll.append(i)
    return ll


ll = [1,5,4,8,5,4,6,4,7,2,3,5,2,1]
print(fun(ll))