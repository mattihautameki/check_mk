#!/usr/bin/python
#
# Sample program for accessing the Livestatus Module
# from a python program
import socket
socket_path = "/omd/sites/home/tmp/run/live"

#### SERVICES #####
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

#### DOWNTIMES #####
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect(socket_path)
# Write command to socket
s.send("GET downtimes\n")
s.send("Columns: host_name\n")

# Important: Close sending direction. That way
# the other side knows we are finished.
s.shutdown(socket.SHUT_WR)

# Now read the answer
answer_downtimes = s.recv(100000000)
downtime_hosts = [ line for line in answer_downtimes.split('\n')[:-1] ]

# filter all entries for hosts in downtime
table = [ service for service in table if not service[0] in downtime_hosts ]

# change scientific notation to float
print "<<<stalesvc>>>"
for i,list in enumerate(table):
  table[i][-1] = str(round(float(list[-1]), 2))
  table[i][-2] = str(round(float(list[-2]), 2))
  print ";".join(table[i])

