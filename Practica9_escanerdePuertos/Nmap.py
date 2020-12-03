# Alejandro de Jesús López Díaz
# Mat: 1990072

import nmap
import json
scan = nmap.PortScanner()
NmapScan = scan.scan("127.0.0.1")
print(json.dumps(NmapScan, indent=4))
print()
print()
for host in scan.all_hosts():
    print('Host : ', (host, scan[host].hostname()))
    print("State : ", (scan[host].state()))
    for protocol in scan[host].all_protocols():
        print("----------")
        print("Protocol : ", protocol)

        port = scan[host][protocol].keys()
        # print(port)
        for port in port:
            print('port : %s\tstate : %s' % (port, scan[host][protocol][port]['state']))
