a = [1,2,3,4,5,6,7,8,9]
b = 10
for i in range(int(b/2) + 1):
    if (b - i) < (len(a)):
        print(a[i] , a[b - i])