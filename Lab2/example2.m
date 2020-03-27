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
C = E1' ;    # assignemnt with matrix transpose
C = A+B ;   # assignemnt with binary addition
C = A-B ;   # assignemnt with binary substraction
C = A*B ;   # assignemnt with binary multiplication
C = A/B ;   # assignemnt with binary division
C = A.+B ;  # add element-wise A to B
C = A.-B ;  # substract B from A 
C = A.*B ;  # multiply element-wise A with B
C = A./B ;  # divide element-wise A by B

E1 += D ;  # add B to C 
E1 -= D ;  # substract B from C 
E1 *= D ;  # multiply A with C
E1 /= E1 ;  # divide A by C
