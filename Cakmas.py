import os
import pyfiglet
from colorama import Fore, init
from SQL import SQL
from Scanner import Scanner
from Admin_Finder import Admin_Finder
from PHP_Hacking import PHP_Hacking

os.system("cls" or "clear")

init()

Banner_Home = pyfiglet.figlet_format("Fatehgar MX")
print(Banner_Home)

cakmas_input = input(Fore.GREEN+("[1]")+Fore.RED+(" SQL")+("\n\n")+Fore.GREEN+("[2]")+Fore.RED+(" Scanner")+("\n\n")+Fore.GREEN+("[3]")+Fore.RED+(" Admin Finder")+("\n\n")+Fore.GREEN+("[4]")+Fore.RED+(" PHP Hacking")+("\n\n")+Fore.GREEN+("[5]")+Fore.RED+(" Exit")+("\n\n")+Fore.GREEN+("MX Fatehgar :> "))

if cakmas_input == "1":
    SQL.SQL()
    
os.system("cls" or "clear")
if cakmas_input == "2":
    Banner2 = pyfiglet.figlet_format("Port Scaner")
    print(Banner2)

if cakmas_input == "2":
    Scanner.port_Scanner()

if cakmas_input == "3":
    Admin_Finder.Admin_Finder()
    Banner3 = pyfiglet.figlet_format( 'Admin_Finder')
    print(Banner3)

if cakmas_input == "3":
    Admin_Finder.Admin_Finder()

if cakmas_input == "4":
    PHP_Hacking.PHP_Hacking()

if cakmas_input == "5":
    exit
    
