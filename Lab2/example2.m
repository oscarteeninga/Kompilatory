# assignment operators
# binary operators
# transposition

A = ones(5);  # create 5x5 matrix filled with zeros
B = eye(5);   # create 7x7 matrix filled with ones
D = ones(3);

E1 = [ 1, 2, 3;
       4, 5, 6;
       7, 8, 9 ] ;

C = -A;     # assignemnt with unary expression
print(C);
C = E1' ;    # assignemnt with matrix transpose
print(C);
C = A+B ;   # assignemnt with binary addition
print(C);
C = A-B ;   # assignemnt with binary substraction
print(C);
C = A*B ;   # assignemnt with binary multiplication
print(C);
C = A/B ;   # assignemnt with binary division
print(C);
C = A.+B ;  # add element-wise A to B
print(C);
C = A.-B ;  # substract B from A
print(C);
C = A.*B ;  # multiply element-wise A with B
print(C);
C = A./B ;  # divide element-wise A by B
print(C);

E1 += D ;  # add B to C 
print(E1);
E1 -= D ;  # substract B from C 
print(E1);
E1 *= D ;  # multiply A with C
print(E1);
E1 /= E1 ;  # divide A by C
print(E1);
print(2000.021);