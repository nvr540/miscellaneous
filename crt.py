import argparse
import requests
from bs4 import BeautifulSoup
"""
author: Nivrita Podder
age: 17
email : nivrita540@gmail.com
date: 19 July 2021
Disclaimer: The creator will not be responsible for any misuse of this program.
"""
parser = argparse.ArgumentParser()
parser.add_argument("-u", type=str, help= "Enter the domain name")
parser.add_argument("-o", type=str, help="Add the file name you want to add the subdomain")
args = parser.parse_args()
def main():
    domain = str(args.u).replace("https://", "").replace("http://", "")
    url = f"https://crt.sh/?q={str(domain)}"
    htmlContent = requests.get(url).content
    soup = BeautifulSoup(htmlContent, "html.parser")
    if args.o != None:
                f = open(str(args.o), "w")
    for sub in soup.find_all('td'):
        if domain in str(sub.string) and "Type: " not in str(sub.string):
            subdomain = str(sub.string).replace("*.","")
            print('\033[92m'+subdomain)
            if args.o != None:
                try:
                    f.write(subdomain+"\n")
                except:
                   continue
    if args.o != None:
        f.close()
if __name__ == '__main__':
    print( '\033[94m'+"""
 ███▄    █ ██▒   █▓ ██▀███  
 ██ ▀█   █▓██░   █▒▓██ ▒ ██▒
▓██  ▀█ ██▒▓██  █▒░▓██ ░▄█ ▒
▓██▒  ▐▌██▒ ▒██ █░░▒██▀▀█▄  
▒██░   ▓██░  ▒▀█░  ░██▓ ▒██▒
░ ▒░   ▒ ▒   ░ ▐░  ░ ▒▓ ░▒▓░
░ ░░   ░ ▒░  ░ ░░    ░▒ ░ ▒░
   ░   ░ ░     ░░    ░░   ░ 
         ░      ░     ░     
               ░            
""")
    main()

