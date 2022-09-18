# -*- coding: utf-8 -*-
"""
Created on Tue May  3 03:11:50 2022

@author: gabri
"""
'''
Comments for the grader:
    Instead of setting a time limit for the scan, I opted to display the amount of time it takes
    to complete the scan. For my local machine, the scan takes aprrox. 2.16 minutes.
'''
#this script scans the ports of the user's machine from port 0 to port 500
import time
import socket

def main():
    host = socket.gethostname() #gets the host name of the machine
    
    hostIP = socket.gethostbyname(host) #translates the host name to IPv4
    print(f'Initializing scan on {hostIP} for ports 0 - 500, please hold.')
    
    scanner(hostIP) #calls the scanner() function, passing hostIP as an argument

def scanner(IP):
    try:
        open_ports = [] #create an empty list to store the open ports
        closed_ports = [] #create an empty list to store the closed/unknown ports
        start = time.time() #the start time of the scan
        
        for port in range(0, 501): #scans ports from 0 - 500
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket with default settings
            sock.settimeout(0.25) #set a timeout on blocking socket operations
            outcome = sock.connect_ex((IP, port)) #connect to a remote socket at the IP address
            if outcome == 0: #if the socket is open, then the method returns 0
                open_ports.append(port) #appends open ports to the open_ports list
            else:
                closed_ports.append(port) #appends closed ports to the closed_ports list
            sock.close()
        stop = time.time() # the end time of the scan
    
        #print the list of open and closed/unknown ports
        print(f'The open ports were {open_ports}')
        print(f'The closed or unknown ports were {closed_ports}')

        run_time = (stop - start) / 60 #the time, in minutes, it takes to scan
        print(f'It took {run_time:.2f} minutes to scan.')

    except socket.error:
        print('Could not connect to server')
    
    
if __name__ == '__main__':
    main()