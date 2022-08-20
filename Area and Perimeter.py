l1, b1, l2, b2 = map(int, input().split())
area1 = l1*b1
area2 = l2*b2
perimeter1 = 2*(l1+b1)
perimeter2 = 2*(l2+b2)
if area1 > area2:
    print("true")
else:
    print("false")
if perimeter1 > perimeter2:
    print("true")
else:
    print("false")
