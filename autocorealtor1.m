%Train the autocorrelator by given patterns: A1=(-1,1,-1,1), A2=(1,1,1,-1),
%A3=(-1, -1, - 1, 1). Test it using patterns: Ax=(-1,1,-1,1), Ay=(1,1,1,1), Az=(-1,-1,-1,-1).


A1 = [-1 1 -1 1];
A2 = [1 1 1 -1];
A3 = [-1 -1 -1 1];
tA1 = [-1 1 -1 1];
tA2 = [1 1 1 1];
tA3 = [-1 -1 -1 -1];

w1 = A1'*A1;
w2 = A2'*A2;
w3 = A3'*A3;

w = w1 + w2 + w3;
disp(w);

yin1 = tA1*w';
yin2 = tA2*w';
yin3 = tA3*w';

y1 = [];
y2 = [];
y3 = [];

for i = yin1
    if i < 0
        y1 = [y1 -1];
    else
        y1 = [y1 1];
    end
end

for i = yin2
    if i < 0
        y2 = [y2 -1];
    else
        y2 = [y2 1];
    end
end

for i = yin3
    if i < 0
        y3 = [y3 -1];
    else
        y3 = [y3 1];
    end
end

disp("Train Set : ")
disp(A1)
disp(A2)
disp(A3)

disp("Train Output : ")
disp(y1)
disp(y2)
disp(y3)

disp("Testing Set: ")
disp(tA1)
disp(tA2)
disp(tA3)

disp("Testing Output : ")
disp(y1)
disp(y2)
disp(y3)


