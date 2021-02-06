#Question 1

list=["1","5","12","4","9","0","15","90"]
print(list)

midIndex=int(len(list)/2)

firstHalf=list[slice(0,midIndex,1)]
secondHalf=list[slice(midIndex,len(list),1)]


secondHalf.extend(firstHalf)
finalList=secondHalf
print(finalList)

#Question 2
n=int(input("please enter an intiger"))

for i in range(0,n+1):
    print(i)

    