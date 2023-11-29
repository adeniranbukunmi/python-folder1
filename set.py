list_of_set=int(input('enter the number of set you want for operation: '))
set_list=[]
y=0
for each_set in range(1, list_of_set+1):
    set_list.append(set())
    number_of_value_in_each_set=int(input(f"enter total items in set {each_set}: "))
    items=[]
    x=1
    for each_item in range( number_of_value_in_each_set):
        item=int(input(f'{x}. enter item {x}: '))
        items.append(item)
        x+=1
    set_list[y]=set((items))
    y+=1
    print(set_list)