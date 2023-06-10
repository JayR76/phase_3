def knapsack(items,capacity):
    bag=[]
    for item in items:
        item['ratio']=round(item['value']/item['weight'])
    items=sorted(items,key=lambda x:x['value'],reverse=True)
    total=0
    for item in items:
        if item['weight']<=capacity:
           bag.append(item)
           total += item['value']
           capacity -= item['weight']
        else:
            total += item['ratio'] + capacity
            capacity -= capacity
            break  

    total_value=0
    for item in bag:
        total_value+=item['value']
    return bag,total_value

items=[
    {"value":34,"weight":7},
    {"value":32,"weight":2},
    {"value":20,"weight":4},
    {"value":12,"weight":5},
    {"value":10,"weight":7}
] 

cap = 15
ans = knapsack(items, cap)
print(ans)



            



