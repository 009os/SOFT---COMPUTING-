%create two matrices of the dimension 3x3 and 3x4 respectively which contain random number as there elements.
%Compute composition of these two fuzzy relation using  both max-min and max-product composition.
%
m1 = 3;
n1 = 3;
m2 = 3;
n2 = 4;

% Create the two matrices with random numbers
A = rand(m1, n1);
B = rand(m2, n2);

% Compute the max-min composition
R_mm = zeros(m1, n2);
for i = 1:m1
  for j = 1:n2
    max_min = -Inf;
    for k = 1:n1
      max_min = max(max_min, min(A(i,k), B(k,j)));
    endfor
    R_mm(i,j) = max_min;
  endfor
endfor

% Compute the max-product composition
R_mp = zeros(m1, n2);
for i = 1:m1
  for j = 1:n2
    max_prod = -Inf;
    for k = 1:n1
      max_prod = max(max_prod, A(i,k)*B(k,j));
    endfor
    R_mp(i,j) = max_prod;
  endfor
endfor

% Display the results
disp("Matrix A:")
disp(A)
disp("Matrix B:")
disp(B)
disp("Max-min composition:")
disp(R_mm)
disp("Max-product composition:")
disp(R_mp)

