N = int(input())
list_N = sorted(list(map(int,input().split()))) 
cost = 0

for i in range(N//2):
    cost += list_N[N - 2*i - 1]-list_N[N - (2*i+1) - 1]

if(N % 2 == 1):
    cost += list_N[0]

print(cost)