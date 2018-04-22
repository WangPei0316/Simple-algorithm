# 扩展一个列表，列表中的元素可能也包含列表
def myextend(alist):
    tmp = []
    for i in alist:
        if isinstance(i,list):
            tmp.extend(myextend(i))
        else:
            tmp.append(i)
    return tmp


t = [1, 2, 5, [3, [], 5, 2, [57]], 90]

print(t)
print(myextend(t))