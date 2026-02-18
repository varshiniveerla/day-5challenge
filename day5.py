request = []
n = int(input("enter no of requests : "))
for i in range(n) :
    val = int(input("enter value : "))
    request = request + [val]
low_demand = []
moderate_demand = []
high_demand = []
invalid_request = []
total_valid = 0
removed = 0
for i in request :
    if i <0 :
        invalid_request = invalid_request + [i]
    elif i==0 :
        total_valid = total_valid + 1
    elif 1<=i<=20 :
        low_demand = low_demand + [i]
        total_valid = total_valid + 1
    elif 21<=i<=50 :
        moderate_demand = moderate_demand + [i]
        total_valid = total_valid + 1
    else :
        high_demand = high_demand + [i]
        total_valid = total_valid + 1
name = input("enter your name: ")
name = name.replace(" ", "")
L = len(name)
PLI = L%3
if PLI == 0:
    removed = len(low_demand)
    low_demand = []
    rule = "A"

elif PLI == 1:
    removed = len(high_demand)
    high_demand = []
    rule = "B"

else:
    removed = len(low_demand) + len(high_demand)
    low_demand = []
    high_demand = []
    rule = "C"
print("length of name", L)
print("PLI = ",PLI," -> applying rule ",rule)
print(low_demand)
print(moderate_demand)
print(high_demand)
print(invalid_request)
print("total valid requests : ",total_valid)
print("removed requests : ",removed)
    



