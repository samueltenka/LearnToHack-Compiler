#REINIT:
set 0 0.0
set 1 0.0
set 2 0.0
set 3 0.0
set 4 0.0
set 5 0.0
set 6 0.0
set 7 0.0
#MAIN:
set 6 1.0
set 7 50.0
set 0 1.0
copy 0 2
set 0 2.0
copy 0 1
set 0 3.0
mul 1 0
add 2 0
copy 0 2
set 0 4.0
copy 0 1
store 7 0
add 6 7
store 7 1
add 6 7
store 7 2
add 6 7
set 0 5.0
copy 0 2
set 0 6.0
add 2 0
copy 0 3
sub 6 7
load 7 2
sub 6 7
load 7 1
sub 6 7
load 7 0
copy 3 0
mul 1 0
add 2 0
#HALT:
set 7 -1
jump 7 0
