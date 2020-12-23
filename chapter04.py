# for : 繰り返しを行う対象のシーケンスに改変をかける場合は、スライス表記[:]を使ってシャドーコピーをする事が推奨される
words = ["I", "have", "a", "pen"]
for w in words[:]:
    if len(w) == 1:
        words.append(w * 2)

print(words)

# range関数は等差級数を生成する
# - リストではなくて、iterableなオブジェクトを返す
for l in range(5):
    print(l, end=",")
else:
    print("")
# iterableなオブジェクトを受ける関数や構造はiteratorという
# - forはiterator
# - list関数はiterator
print(list(range(3)))

# キーワード引数


def mytest(a, *args, **keywords):
    print(a)

    for arg in args:
        print(arg)
    sortedKwds = sorted(keywords.keys())
    for key in sortedKwds:
        print(key, keywords[key])


mytest("a is a", "args1", "args2", key1="key1Val", key2="key2Val")

# アンパック
print([1, 2, 3])   # list
print(*[1, 2, 3])  # listをアンパック
print((1, 2, 3))   # タプル
print(*(1, 2, 3))  # タプルをアンパック
print({"a": 1, "b": 2, "c": 3})
print(*{"a": 1, "b": 2, "c": 3})

# **演算子:辞書をキーワード引数に渡せる
myDict = {"a": "1", "b": "2", "c": "3"}


def myDictPrint(a, b, c):
    print(a)
    print(b)
    print(c)


myDictPrint(**myDict)

print(30 * "-")
# lambda


def make_inc(n):
    return lambda x: x+n


f = make_inc(4)
print(f(3))
print(f(1))

pair = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pair.sort(key=lambda p: p[1])
print(pair)


