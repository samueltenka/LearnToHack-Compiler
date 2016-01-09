4  assign   0  0.0
5  assign   1  1.0
6  assign   4  10.0
7  assign   7  21.0
8  assign   6  12.0  #assign a one-use address, later overwritten
9  jump  6           #skip motor-writing into middle of loop
10 store 2  5        #loop begin:
11 store 3  6        #write motors
12 load  0  2
13 load  1  3
14 sub   2  3
15 assign   5  0.0
16 assign   6  0.0
17 bi0   4  3
18 bin   7  3
19 assign   5  1.0
20 jump  4
21 assign   6  1.0
22 jump  4
