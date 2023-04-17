S=list(input())
Alpha='abcdefghijklmnopqrstuvwxyz'

for i in Alpha:
    if i in S:
        print(S.index(i),end=' ')
    else: 
        print(-1,end=' ')