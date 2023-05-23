inp=[[-1,-1],[-1,1],[1,-1],[1,1]]
target=[-1,1,1,-1]
w11=0.05
w12=0.1
w21=0.2
w22=0.2
v0=0.5
v1=0.5
lr=0.5
b1=0.3
b2=0.15
b3=0.5
w=[0.0,0.0,0.0,0.0]
b=[0.0,0.0,0.0]
print("x1\tx2\tt\tz1\tz2\ty\tdw11\tdw12\tdw21\tdw22\tdwb1\tdwb2\tdwb3")
for k in range(4):
    for i in range(4):
        y1=inp[i][0]*w11+inp[i][1]*w21+b1
        if y1<0:
            y1=-1
        else:
            y1=1
        y2=inp[i][0 ]*w12+inp[i][1]*w22+b2
        if y2<0:
            y2=-1
        else: 
            y2=1
        y3=y1*v0+y2*v1+b3
        if y3<0:
            y3=-1
        else:
            y3=1
        if y3!=target:
            error=target[i]-y3
            w[0]=lr*error*inp[i][0]
            w[1]=lr*error*inp[i][0]
            w[2]=lr*error*inp[i][1]
            w[3]=lr*error*inp[i][1]
            b[0]=lr*error
            b[1]=lr*error
            b[2]=lr*error
            w11=w11+w[0]
            w12=w12+w[1]
            w21=w21+w[2]
            w22=w22+w[2]
        print(f"{inp[i][0]}\t{inp[i][1]}\t{target[i]}\t{y1}\t{y2}\t{y3}\t{w[0]}\t{w[1]}\t{w[2]}\t{w[3]}\t{b[0]}\t{b[1]}\t{b[2]}\t")
    print("----------------")

