# / 除算
a = 17 / 3
# // 切り下げ除算
b = 17 // 3

# 対話モードの場合のみ、_に最後に表示した式が代入されている
# c = _ * 5

# 特殊文字に解釈させないためにはraw文字列を使う
print("C:\aaa\nnn")
print(r"C:\aaa\nnn")

# トリプルクォートで文字列を複数行に書ける
print("""\
aaa\
bbb
ccc\
""")

# 文字列の繰り返しや連結
print("[" + 5 * ' ' + "] rept space for 5 times!")

# 文字列は、列挙すると自動で連結
print("a" "b" "c")

# 文字列をインデックス指定するとキャラクタが得られる
m = "Python"
print(m[:3] + "|" + m[3] + "|" + m[3:])

# Pythonの文字列は改変が出来ない immutable

# len関数
print(len(m))

# list型はmutable(変更可能)
l = [2, 3, 6, 7]
l[0] = 1
print(l)

# listは入れ子に出来る
ll = [l, [1, 4, 5, 8]]
print(ll)

# フィボナッチ級数
a,b=0,1
while b < 10:
  print(b,end=",")
  a,b=b,a+b 
