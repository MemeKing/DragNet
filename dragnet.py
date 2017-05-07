#!/usr/bin/env python
import nmap


def Scan(port):
    nm = nmap.PortScanner()
    while True:
        nm.scan('-iR 1', str(port))
        if len(nm.all_hosts()) > 0:
            if nm[nm.all_hosts()[0]]['tcp'][port]['state'] == "open":
                return nm.all_hosts()[0]


if __name__ == "__main__":
    print "Scanning..."
    openHosts = []
    while len(openHosts) < 5:       # How many live IPs to fetch.
        openHosts.append(Scan(80))  # Change '80' to search other ports.
        print openHosts[-1]
