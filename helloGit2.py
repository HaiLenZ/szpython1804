hel = 'helloWorld!!!'
z = 'HaiLenZ'
mylist = []
for i in z:
    mylist.append(i)
print(mylist)
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

s = sum(10)
print(s)