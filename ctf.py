import argparse
import requests
from bs4 import BeautifulSoup

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
            print(subdomain)
            if args.o != None:
                try:
                    f.write(subdomain+"\n")
                except:
                   continue
    if args.o != None:
        f.close()
if __name__ == '__main__':
    main()

