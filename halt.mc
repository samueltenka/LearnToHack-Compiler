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
set 0 1.0
copy 0 2
set 0 2.0
copy 0 1
set 0 3.0
mul 0 1
#add 0 2
#copy 0 2
#set 0 4.0
#copy 0 1
#set 0 5.0
#copy 0 2
#set 0 6.0
#add 0 2
#copy 2 0
#mul 0 1
#add 0 2
#HALT:
set 7 -1
jump 7 0
