
def iter_ator(items, step = 3):
    for item in items:
        if step%3 == 0:
            yield item

item_list = iter_ator([1,2,3,4,5,6])
for i in item_list:
    print(i)

for j in item_list:
    print(j+100)


