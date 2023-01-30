T = int(input())
for t in range(T):
    num = int(input())
    if num > 500 :
        print('Error')
        break
    Quarter = num//25
    Dime = (num - (Quarter*25))//10
    Nickel = (num - (Quarter*25) - (Dime*10))//5
    Penny = (num - (Quarter*25) - (Dime*10) - (Nickel*5))//1
    print(Quarter, Dime, Nickel, Penny)
