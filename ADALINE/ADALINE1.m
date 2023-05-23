x1 = [1 1 -1 -1];
x2 = [1 -1 1 -1];

target = [-1 1 1 1];

lr = 0.1;
w1 = 0.1;
w2 = 0.1;
b = 0;

for j=1:5
  fprintf("\nEpoch - %d\n\n", j);
  fprintf("  x1 \t\t   x2 \t\t   t \t\t yin \t\t\t w1 \t\t\t w2 \t\t\t b \t\t\t Error\n");

  output=[];
  error=[];
  d = 0;

  for i=1:4
    fprintf('\n');
    fprintf("%4d \t\t",x1(i));
    fprintf("%4d \t\t",x2(i));
    fprintf("%4d \t\t",target(i));

    temp = (w1*x1(i))+(w2*x2(i)) + b;

    fprintf("%4d \t\t",temp);

    if temp ~= target(i)
      w1 = w1 + lr*(target(i)-temp)*x1(i);
      w2 = w2 + lr*(target(i)-temp)*x2(i);
      b = b + lr*(target(i)-temp);
    endif

    fprintf("%4d \t\t",w1);
    fprintf("%4d \t\t",w2);
    fprintf("%4d \t\t",b);
    e = (target(i) - temp) ^ 2;

    fprintf("%4d \t\t",b);

    d = d + e;

  endfor
  %fprintf("Error = %d\n", d);
end;

