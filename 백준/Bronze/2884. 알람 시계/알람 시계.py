H, M=map(int,input().split())
M2=M-45

if M2<0:
    H=H-1
    M=60+M2 
else:
    M=M2
if H<0:
    H=23
print(H, M)   