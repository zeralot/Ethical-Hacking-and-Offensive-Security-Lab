from socket import * 
import ipaddress
import sys
import datetime

def scan_port(target_ip):
    min = 0
    max = 10000
    open_ports = []
    for i in range(min, max):
        s = socket(AF_INET, SOCK_STREAM)
        result = s.connect_ex((target_ip, i))
        #Add open ports
        if(result == 0):
            open_ports.append(i)
        s.close()
    return open_ports
    
def get_list_host(range):
    ip_list = list(ipaddress.ip_network(unicode(range)).hosts())
    rs = []
    for ip in ip_list:
        rs.append(str(ip))
    return rs

def print_results(open_ports):
    if (len(open_ports)!= 0):
        open_ports.sort()
        print '- - - - - - - - - - - - - - - - - - - - - - - - -'
        for i in open_ports:
            print ('Port %d: OPEN' % (i,))
        print '- - - - - - - - - - - - - - - - - - - - - - - - -'

if __name__ == '__main__':
    target = raw_input("Enter IP/IP range: ")
    list_ip = get_list_host(target)
    if (len(list_ip)!= 0):
        for target_ip in list_ip:   
            print 'Starting scan on :', target_ip
            open_ports = scan_port (target_ip)
            print_results(open_ports)
    else:
        print 'Starting scan on :', target
        open_ports = scan_port (target)
        print_results(open_ports)


