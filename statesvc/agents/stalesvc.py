#!/usr/bin/python
#
# Sample program for accessing the Livestatus Module
# from a python program
socket_path = "/omd/sites/home/tmp/run/live"

import socket
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect(socket_path)

# Write command to socket
s.send("GET services\n")
s.send("Columns: host_name description state check_interval staleness last_state_change\n")
s.send("Filter: staleness > 1\n")

# Important: Close sending direction. That way
# the other side knows we are finished.
s.shutdown(socket.SHUT_WR)

# Now read the answer
answer = s.recv(100000000)

# Parse the answer into a table (a list of lists)
table = [ line.split(';') for line in answer.split('\n')[:-1] ]

# change scientific notation to float
print "<<<stalesvc>>>"
for i,list in enumerate(table):
  table[i][-1] = str(round(float(list[-1]), 2))
  table[i][-2] = str(round(float(list[-2]), 2))
  print ";".join(table[i])
