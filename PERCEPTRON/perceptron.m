%{Create a perceptron with appropriate no. of inputs and outputs.
    Train it using fixed increment learning algorithm until no change in weights is required. 
    Output the final weights.%}

lr = 0.01;
w1 = 0.04;
w2 = 0.3;

x=[0 0 1 1];
y=[0 1 0 1];

choice = (input("\n1. And \n2. OR \n3. NAND \n4. NOR \n5. XOR \n\n Enter your choice :"));

switch choice
    case 1
        disp('choice 1');
        label=[0 0 0 1];
    case 2
        label=[0 1 1 1];
    case 3
        label=[1 1 1 0];
    case 4
        label=[1 0 0 0];
    case 5
        label=[0 1 1 0];
    otherwise
        disp('Wrong choice');
end

for j=1:4
  fprintf("\nEpoch - %d\n\n", j);
  fprintf("  x1 \t\t   x2 \t\t   t \t\t yin \t\t   y \t\t w1 \t\t w2\n");

  output=[];
  error=[];
  for i=1:4

    fprintf('\n');
    fprintf("%4d \t\t",x1(i));
    fprintf("%4d \t\t",x2(i));
    fprintf("%4d \t\t",target(i));
    temp=(w1*x(i))+(w2*y(i));
    fprintf("%4d \t\t",temp);

    if temp>0.5
       temp = 1;
    else
       temp = 0;
    endif
    fprintf("%4d \t\t",temp);

    output=[output,temp];
    e=(label(i)-output(i))*(label(i)-output(i));
    error=[error, e];
    d = sum(error);
    w1=w1+lr*d;
    w2=w2+lr*d;

    fprintf("%4d \t\t",w1);
    fprintf("%4d \t\t",w2);
  end;
end;

