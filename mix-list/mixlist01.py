#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]
#List with three items

print("The first item on the list (IP): " + my_list[0] )
#IP value
print("The second item on the list (port): " + str(my_list[1]) )
#Port Value

print("The last item in the list (state): " + my_list[2] )
#State 

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
#New list 6 items

#Display sentence multi-lined
print("When I " + new_list[5] + " into IP addresses " + new_list[3])
print("or " + new_list[4] + " I am unable to ping ports")
print(str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2]))


