
% Write program that ask user to enter two fuzzy sets and computes the resultant fuzzy relation upto 10 greater than 6.
disp("Enter the first fuzzy set elements between 6-10:");
A = input("A = ");
if length(A)>=6 && length(A)<=10
  disp("Enter the second fuzzy set elements between 6-10::");
B = input("B = ");

if length(B)>=6 && length(B)<=10
  R = zeros(length(A),length(B));
for i = 1:length(A)
  for j = 1:length(B)
    R(i,j) = min(A(i),B(j));
  endfor
endfor

% Display the resultant fuzzy relation
disp("The resultant fuzzy relation is:")
disp(R)
  else
  disp("Please enter the setB elements within range of 6-10")
  end
else
  disp("Please enter the setA elements within range of 6-10")
  End

