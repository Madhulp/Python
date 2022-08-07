def dayofweek(y, m, d):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if (m < 3):
        y -= 1
    return (y+y//4-y//100+y//400+t[m-1]+d) % 7


n = int(input())
for i in range(n):
    d, m, y = map(int, input().split("/"))
    a = dayofweek(y, m, d)
    arr = ["Sunday", "Monday", "Tuesday",
           "Wednesday", "Thursday", "Friday", "Saturday"]
    print(arr[a])
