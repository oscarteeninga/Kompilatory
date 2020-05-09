# Adding CONST to MATRIX
x = eye(3);
y = x .+ 3;
y = x + 3;

# Adding VAR to MATRIX
x = eye(2);
y = 5;
z = x .+ y;
z = x + y;

# Adding VAR to VAR using MATRIXEXPRESSION
x = 3;
y = 4;
z = x .+ y;

# Adding MATRIX with other DIM
x = eye(3);
y = eye(2);
z = x .+ y;
z = x + y;

# Def MATRIX with bad DIM
x = eye(2.3);

# Def MATRIX with bad VECTORS
x = [1,2,3;
    4, 5];

# Adding MATRIX one more time
x = eye(3);
y = eye(3);
z = x .+ y;
w = eye(4);
v = z .+ w;

# Using undefined symbols
x = p + k;
x = p .+ k;