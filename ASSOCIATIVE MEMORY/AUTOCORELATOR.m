%Train an autocorrelator network for the pattern [1,-1,1,1] and also test the new weight for one missing and one mistake entry in the test vector respectively.%
x=[ 1 -1 1 1];
disp('inputs are -');
disp(x);
%target value%
y=[ 1 -1 1 1];
disp('target value-');
disp(y);
 %transpose of the x %
 xt=x';
disp('transpose of the x');
disp(xt);
w=zeros(length(xt),length(y));
for i=1:length(xt)
  for j=1:length(y)
    w(i,j)=xt(i)*y(j);
  endfor
endfor
disp('weight are');
disp(w);
disp('yin -');
yin=x*w;
disp(yin);
for i=1:length(yin)
  if (yin(i)>=0)
    yin(i)=1;
elseif(yin(i)<0)
  yin(i)=-1;
endif
endfor
if yin=y
  fprintf("sucessful tested");
else
  fprint("Error");
endif

