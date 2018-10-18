import socket
import requests

def export_file(sub_list,fileName):
    file = open(fileName,"w")
    for sub in sub_list:
    	file.write(sub + '\n')
    file.close()
    print "Your result => " + fileName
    
def print_results(subdomains):
    if (len(subdomains)!= 0):
        subdomains.sort()
        print '- - - - - - - - - - - - - - - - - - - - - - - - -'
        for i in subdomains:
            print i
        print '- - - - - - - - - - - - - - - - - - - - - - - - -'

def main():
    domain = raw_input("Enter domain to scan: ")
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey':'fee0a15e59424e5c510e097cafbea8b68264fb05fd2f6067cd35956a198303b0','domain':domain}
    response = requests.get(url, params=params)
    subdomains = response.json()['subdomains']
    output = domain + "_subdomain.txt"
    print_results(subdomains)
    export_file(subdomains,output)

if __name__ == '__main__':  
   main()
