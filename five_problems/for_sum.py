
def for_sum(mylist):
    sum = 0
    for i in range(len(mylist)):
        sum += mylist[i]
    return sum

mylist = [1, 4, 5, 3, 7]

sum = for_sum(mylist)
g.es("sum is:", sum)
