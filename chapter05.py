from collections import deque
a = [1, 11, 1.1, 33, 3.3, 7, 7.7]

a.append(5)
a.insert(2, 0.111)
b = a.copy()

a[len(a):] = [b.pop(2)]
a.extend(b)
a.remove(33)
a.append(a.index(7))

a.reverse()
# print(a.count(7))
a.sort(key=lambda x: -x, reverse=True)
a.clear()
b.clear()
# ------

que = deque(['internet', 'moziila', 'Alpha'])
# print(que.popleft())
que.append('Might')

# ------
# リスト内包
a = [(x, y) for x in [1, 4, 5, 8] for y in [2, 3, 6, 7] if x < y]
a = [' internet  ', '   mozila', 'alpha    ']
print([mystr.strip() for mystr in a])

# forを2回使ってListを平滑化
vector = [[1, 4, 5, 8], [2, 3, 6, 7]]
print([num for elem in vector for num in elem])

# ------
# 入れ子の内包
print(list(zip(*vector)))
print([[a, b] for a, b in zip(*vector)])
print([[x[i] for x in vector] for i in range(4)])

# ------
# del文
del vector[0]


