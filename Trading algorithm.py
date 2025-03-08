stocks=[215,265,250,200,240,230]
minsofar=float('inf')
maxprofit= 0
for i in stocks:
    minsofar=min(minsofar,i)
    maxprofit=max(maxprofit,i-minsofar)
print(maxprofit)
