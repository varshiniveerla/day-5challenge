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

