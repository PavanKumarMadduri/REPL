A=[0, 0, 3, 4, 5]
#Base case
if not A:
  print("[]")

zeroCount=A.count(0)

#With Division
if zeroCount==0:
  product=1
  for i in A:
    product*=i
  newA=[]
  for i in A:
    newA.append(product//i)
  print(newA)

#Without Division
  B=A
  newB=[]
  for i in range(len(B)):
    product2=1
    for j in B[:i]+B[i+1:]:
      product2*=j
    newB.append(product2)
  print(newB)

elif zeroCount>=2:
  newC=[0]*len(A)
  print(newC)

else:
  zeroIndex=A.index(0)
  newD=[0]*len(A)
  newD[zeroIndex]=1
  for j in A[:zeroIndex]+A[zeroIndex+1:]:
    newD[zeroIndex]*=j
  print(newD)