% write a program that creates two random fuzzy sets of the dimensions say n and m (to be defined by the user)
%Complete the fuzzy relation indexed by Cartesian product of the sets.
for i=1:3

A{1}(i) = input("Enter value for set A : ");
B{1}(i) = input("Enter value for set B : ");

end

%Display fuzzy set A
fprintf("A = { ");
for i=1:3
 fprintf("%d, ", A{1}(i));

end

fprintf("}\n");

%Display fuzzy set B
%Display fuzzy set B
fprintf("B = { ");
for i=1:3
 fprintf("%d, ", B{1}(i));
end

R = {[],[]};

%Display cartersian relation
fprintf("}\n\nRelation : \n\n")
for i=1:3
for j=1:3
  R{i}(j) = min(A{1}(i), B{1}(j));
  fprintf("%d\t",R{i}(j));
endfor
fprintf("\n");
end

fprintf("\n");
end

