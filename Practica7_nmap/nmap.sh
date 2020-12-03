#!/bin/bash
script(){
ip address
hostname -I
curl ifconfig.me
nmap -v 1 192.168.0.1
nmap -v 1 scanme.nmap.org
nmap -v 1 189.219.74.175
}
script > escaneo.txt