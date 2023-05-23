"""write a program to implement GMP and GMT and verify the implementation in presence of following cases for inputs. (PYTHON)

A={(x1,0.5),(x2,1),(x3,0.5)}
B={(y1,1),(y2,0.4)}
A`={(x1,0.6),(x2,0.9),(x3,0.7)}

CODE:"""
import numpy as np

a1 = np.matrix([1,-1,-1,-1,-1,1])
a2 = np.matrix([-1,1,-1,-1,-1,-1])
a3 = np.matrix([-1,-1,1,-1,1,1])

b1 = np.matrix([1,1,-1,-1,-1])
b2 = np.matrix([1,-1,1,-1,-1])
b3 = np.matrix([-1,1,1,1,-1])

w1 = np.dot(np.transpose(a1),b1)
w2 = np.dot(np.transpose(a2),b2)
w3 = np.dot(np.transpose(a3),b3)

w = w1 + w2 + w3

print(w)

yin3 = np.dot(a3,w)
yin3 = np.array(yin3)

print(yin3)
y3 =list()

for i in yin3[0]:
    # print(i)
    if i <0:
        y3.append(-1)
    else:
        y3.append(1)
print(y3) 
wt = np.transpose(w)
y3 = np.matrix(y3)
xin3 = np.dot(y3,wt)


xin3 = np.array(xin3)

x3 =list()

for i in xin3[0]:
    # print(i)
    if i <0:
        x3.append(-1)
    else:
        x3.append(1)
    
# x3 = np.matrix(x3[-1])
# if x3 == a1 or x3 == a2 or x3 == a3 :
#     print("conversion is done")

print( x3)
# print( )
