#FUZZY OPERATORS 

A = dict()
B = dict()
Y = dict()

A = {"a": 0.5, "b": 0.7, "c": 0.3, "d": 0.4,"e":0.7,"f":0,"g":0.8,"h":0}
B = {"a": 0, "b": 0, "c": 0.9, "d": 0.1,"e":0,"f":0,"g":0.7,"h":0}

print('The First Fuzzy Set is :',"\n")
for A_key in A:
   print(A[A_key],"/",A_key," + ",end="")
print("\n")

print('The Second Fuzzy Set is :',"\n")
for B_key in B:
   print(B[B_key],"/",B_key," + ",end="")
print("\n")

# SET UNION
print('\n','FUZZY SET UNION IS : ')
for A_key, B_key in zip(A, B):
    A_value = A[A_key]
    B_value = B[B_key]

    if A_value > B_value:
        Y[A_key] = A_value
        print('%.2f' %Y[A_key],"/",A_key," + ",end="")
    else:
        Y[B_key] = B_value
        print('%.2f' %Y[B_key],"/",B_key," + ",end="")
print("\n")
# SET INTERSECTION
print('\n','FUZZY SET INTERSECTION IS : ')
for A_key, B_key in zip(A, B):
    A_value = A[A_key]
    B_value = B[B_key]
 
    if A_value < B_value:
        Y[A_key] = A_value
        print('%.2f' %Y[A_key],"/",A_key," + ",end="")
    else:
        Y[B_key] = B_value
        print('%.2f' %Y[B_key],"/",B_key," + ",end="")
print("\n")        

# COMPLEMENT OF A
print("\n\n\n",'COMPLEMENT OF A IS :')
for A_key in A:
   Y[A_key]= 1-A[A_key]
   print('%.2f' %Y[A_key],"/",A_key," + ",end="")
print("\n")
# COMPLEMENT OF B
print("\n\n\n",'COMPLEMENT OF B IS :')
for B_key in B:
   Y[B_key]= 1-B[B_key]
   print('%.2f' %Y[B_key],"/",B_key," + ",end="")
print("\n")
  # SET DIFFERENCE 
print("\nFUZZY SET DIFFERENCE IS : ")
for A_key, B_key in zip(A, B):
    A_value = A[A_key]
    B_value = B[B_key]
    B_value = 1 - B_value
 
    if A_value < B_value:
        Y[A_key] = A_value
        print('%.2f' %Y[A_key],"/",A_key," + ",end="")
        
    else:
        Y[B_key] = B_value
        print('%.2f' %Y[B_key],"/",B_key," + ",end="")
print("\n")

# SET ALGEBRAIC SUM
print("FUZZY SET ALGEBRAIC SUM IS : ")
Z = dict()
for A_key,B_key in zip(A,B):
    A_value=A[A_key]
    B_value = B[B_key]

    Z[A_key]= A_value+B_value-(A_value*B_value)
    print('%.2f' %Z[A_key],"/",A_key," + ",end="")
print("\n")

#SET ALGEBRAIC PRODUCT
print("\nFUZZY SET ALGEBRAIC PRODUCT IS :")
for A_key,B_key in zip(A,B):
    A_value=A[A_key]
    B_value = B[B_key]
    Y[A_key]= (A_value*B_value)
    print('%.2f' %Y[A_key],"/",A_key," + ",end="")
print("\n")   
# BOUNDED SUM    
print("\nBOUNDED SUM IS :")
for A_key,B_key in zip(A,B):
    A_value=A[A_key]
    B_value = B[B_key]
    
    if(A_value+B_value < 1):
        Y[A_key]= A_value+B_value
        print('%.2f' %Y[A_key],"/",A_key," + ",end="")
    else:
        Y[A_key]= 1
        print(Y[A_key],"/",A_key," + ",end="")
print("\n")
# BOUNDED DIFFERENCE  
print("\nBOUNDED DIFFERENCE IS :")
for A_key,B_key in zip(A,B):
    A_value=A[A_key]
    B_value = B[B_key]
    
    if(A_value+B_value > 0):
        Y[A_key]= A_value+B_value
        print('%.2f' %Y[A_key],"/",A_key," + ",end="")
    else:
        Y[A_key]= 0
        print(Y[A_key],"/",A_key," + ",end="")
print("\n")    
# CUBE OF A 
print("\n\n\n",'FUZZY SET CUBE IS :')
for A_key in A:
   Y[A_key]= pow(A[A_key],3)
   print('%.2f' %Y[A_key],"/",A_key," + ",end="")
print("\n")
#Height of A
a=0
for A_key in A:
   
    if(A[A_key]>a):
        a=A[A_key]
print('HEIGHT OF A is :', '%.2f' %a,"\n\n\n")
#Height of B
b=0
for B_key in B:
   
    if(B[B_key]>b):
        b=B[B_key] 
print('HEIGHT OF B is :','%.2f' % b,"\n\n\n")
#CARDINALITY OF A 
card=0
for A_key in A:
   card= card+ A[A_key]
print('CARDINALITY of A  is :','%.2f' % card,"\n\n\n")
#CARDINALITY OF B 
card1=0
for B_key in B:
   card1= card1+ B[B_key]
print('CARDINALITY of B  is :', '%.2f' %card1,"\n\n\n")
