
import random

#given some product history predict what items should be in basket
#ignore min spend and multi buys

#sim some data

prods=100

hist=[] #basket,days ago,product,price
prices=[round(random.random(),2) for i in range(prods)]
for b in range(10):
    n=int(1+random.random()*100) #items in basket
    days=-int(1+random.random()*100) #from today
    for i in range(n):
        p=int(random.random()*prods)
        hist.append([b,days,p,prices[p]])
    #total basket
    print b,days,n,sum([i[3] for i in hist if i[0]==b])


#now collect stats
prodStats={} 
for i in hist:
    p=i[2]
    days=i[1]
    if p not in prodStats:
        prodStats[p]=set()
    prodStats[p].add(days)

#predict, show prods and running total
#for all products that have been bought 2+ find average diff and last days
print 'prediction'
tot=0
i=0
for p,v in prodStats.iteritems():
    if len(v)>1:
        avg=float(max(v)-min(v))/(len(v)-1)
        if avg+max(v)>=0:
            i+=1
            tot+=prices[p]                    
            print p,i,tot
        
