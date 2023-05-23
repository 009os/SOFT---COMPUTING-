"""Using back-propagation network, find the new weights.
 It is presented with the input pattern [0, 1] and the target output is 1.
   Use a learning rate α = 0.25 and binary sigmoidal activation function"""
bbb = [0.3, 0.15, 0.5]
www = [0.05, 0.1, 0.2, 0.2]

w = [0.05, 0.1, 0.2, 0.2]
v = [0.5, 0.5]
lr = 0.4
b = [1, 1, 1]
inp = [[-1, 1, -1, 1], [-1, -1, 1, 1]]
t = [1, -1, -1, -1]
dif = 0
print("x1\tx2\tt\tz1\tz2\ty\tw0\tw1\tw2\tw3\tb1\tb2\tb3")
for i in range(4):
    print(f"{inp[0][i]}\t{inp[1][i]}\t{t[i]}\tz1\tz2\ty\t{w[0]}\t{w[1]}\t{w[2]}\t{w[3]}\t{b[0]}\t{b[1]}\t{b[2]}")
for j in range(4):
    print("============================================================================================================================================= ", dif)
    for i in range(4):
        z1 = inp[0][i]*w[0] + inp[1][i]*w[1] + b[0]
        z2 = inp[0][i]*w[2] + inp[1][i]*w[3] + b[1]

        # activation funciton on hidden layer
        if z1 < 0:
            z1 = -1
        else:
            z1 = 1
        if z2 < 0:
            z2 = -1
        else:
            z2 = 1

        y = z1*v[0] + z2*v[1] + b[2]
        # print(y)

        # activation function in output layer
        if y < 0:
            y = -1
        else:
            y = 1

        # print(f"{inp[0][i]}\t{inp[1][i]}\t{t[i]}\t{z1}\t{z2}\t{y}\t{w[0]}\t{w[1]}\t{w[2]}\t{w[3]}\t{b[0]}\t{b[1]}\t{b[2]}")
        if y != t[i]:
            dif = t[i]-y
            # print(dif)
            w[0] += lr*dif*inp[0][i]
            w[1] += lr*dif*inp[1][i]
            w[2] += lr*dif*inp[0][i]
            w[3] += lr*dif*inp[1][i]

            b[0] = b[0] + lr*dif
            b[1] = b[1] + lr*dif
            b[2] = b[2] + lr*dif

        print(f"{'%.2f' %inp[0][i]}\t{'%.2f' %inp[1][i]}\t{'%.2f' %t[i]}\t{'%.2f' %z1}\t{'%.2f' %z2}\t{'%.2f' %y}\t{'%.2f' %w[0]}\t{'%.2f' %w[1]}\t{'%.2f' %w[2]}\t{'%.2f' %w[3]}\t{'%.2f' %b[0]}\t{'%.2f' %b[1]}\t{'%.2f' %b[2]}")
