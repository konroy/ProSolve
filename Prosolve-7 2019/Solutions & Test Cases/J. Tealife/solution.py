input()
A=sorted(map(int,input().split()))
input()
s=sum(A)
for q in map(int,input().split()):print(s-A[-q])