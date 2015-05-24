def recur_sum(mylist):
    if len(mylist) == 1:
        return mylist[0]
    else:
        g.es(mylist[0],"+ 遞迴加(", mylist[1:], ")")
        return mylist[0] + recur_sum(mylist[1:])

mylist = [1, 4, 5, 3, 7]
sum = recur_sum(mylist)
g.es("sum is:", sum)
