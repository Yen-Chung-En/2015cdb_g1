
def while_sum(mylist):
    i = 0
    sum = 0
    while i < len(mylist):
        sum += mylist[i]
        i += 1
    return sum

mylist = [1, 4, 5, 3, 7]
sum = while_sum(mylist)
g.es("sum is:", sum)
