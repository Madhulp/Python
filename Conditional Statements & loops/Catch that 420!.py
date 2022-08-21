N = input()
n = N[:-4:-1]
n = n[::-1]
if n == '420':
    print('Caught')
else:
    print('Escaped')
