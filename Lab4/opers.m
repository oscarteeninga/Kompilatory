x = 0;
y = zeros(5);
z = x .+ y;
x = eye(3);
y = eye(8);
z = x .+ y;
x = [ 1,2,3,4,5 ];
y = [ 1,2,3,4,5;
      1,2,3,4,5 ];
z = x .+ y;
x = zeros(5);
y = zeros(9);
z = x + y;
h = x + y;
w = eye(3);
x = ones(3);