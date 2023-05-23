%{Create two matrix of the dimension two matrix of dimension defined by user containing random number(0-1)
%as there elements perform the union intersection and complement operation on these two matrices treating them to be fuzzy relation.

rows = input('Enter the number of rows for the matrices: ');
cols = input('Enter the number of columns for the matrices: ');

%  two matrices with random numbers between 0 and 1
matrix1 = rand(rows, cols);
matrix2 = rand(rows, cols);

% union operation
union_matrix = max(matrix1, matrix2);

% intersection operation
intersection_matrix = min(matrix1, matrix2);

%  complement operation
complement_matrix1 = 1 - matrix1;
complement_matrix2 = 1 - matrix2;

%  original matrices and the resulting matrices
disp('Matrix 1:')
disp(matrix1)
disp('Matrix 2:')
disp(matrix2)
disp('Union:')
disp(union_matrix)
disp('Intersection:')
disp(intersection_matrix)
disp('Complement of Matrix 1:')
disp(complement_matrix1)
disp('Complement of Matrix 2:')
disp(complement_matrix2)

