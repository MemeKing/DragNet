#!/usr/bin/env python
import nmap


def Scan(port):
    hosts = []
    nm = nmap.PortScanner()
    while len(hosts) == 0:
        nm.scan('-iR 1', str(port))
        for i in nm.all_hosts():
            if nm[i]['tcp'][port]['state'] == "open":
                hosts.append(i)
    return hosts


def main(n):
    openHosts = []
    while len(openHosts) < n:
        openHosts.append(Scan(80))
        print openHosts[-1]


if __name__ == "__main__":
    print "Scanning..."
    main(5)
