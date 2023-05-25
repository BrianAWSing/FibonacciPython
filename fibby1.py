#Licence: MIT
#
#Author(s): Brian Byrne
#
#Program purpose:
#----------------
# 
# Display Fibonacci sequence
#
#Program notes:
#--------------
#
# Nothing clever just add and then swap the variables.
#
# Done in 15 minutes with a tea break.
#
# All explained at: 
# https://www.mathsisfun.com/numbers/fibonacci-sequence.html
#--------------------------------------------------------
#
first=0
second=1
third=0
#
upperLimit=16
counter=1
#
while counter < upperLimit:
    counter=counter+1
    third=first+second
    print (str(first))
    first=second
    second=third
#
print("All done")