#/bin/bash
#gobuster dir -u http://10.10.199.11/secret -w /usr/share/wordlist/dirb/common.txt -x php,txt -o dir2.txt
#nmap -sV -A -oN nmap/initial -vv 10.10.199.11
#nikto -h http://10.10.13.194:9999/
#xterm -e 'echo -ne "\033]0;nmap\007;read' #For changing the profile name
# xterm -e 'echo "hello world"; ping google.com' 
read -p "Please enter a The IP address: " IP
echo "Enter a path Where you want t0 S4v3"
read path
cd $path
# wordlist = "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"
#Nmap 
xterm -fa 'Monospace' -fs 10 -hold -geometry 80x27+1930+0 -bg white -fg black -e 'echo -ne "\033]0;nmap\007";mkdir nmap;nmap -sV -A -oN nmap/initial -vv $IP; echo "The Scan is saved in nmap/initial";read' &

# echo "nmap scan started"
# echo "Do you want to scan all the ports [y/n]"
# read op
# if [[ "$op" -eq "y" ]]
# then

# 	echo "Hello world"
# 	# xterm -fa 'Monospace' -fs 10 -hold -geometry 80x27+1930+0 -bg white -fg black -e 'echo -ne "\033]0;nmap\007";mkdir nmap;nmap -p- -sV -A -oN nmap/initial -vv $IP; echo "The Scan is save in nmap/initial";read' &
# else
# 	# xterm -fa 'Monospace' -fs 10 -hold -geometry 80x27+1930+0 -bg white -fg black -e 'echo -ne "\033]0;nmap\007";mkdir nmap;nmap -sV -A -oN nmap/initial -vv $IP; echo "The Scan is save in nmap/initial";read' &
# 	echo "hacked"
# fi
echo "Enter any port for gobuster Or nikto scan[default is port 80]"
read port
#Nikto
echo "Nikto and gobuster attack started on port $port"
xterm  -fa 'Monospace' -fs 10 -hold -geometry 80x27+200+500 -bg darkviolet -fg black -e 'echo -ne "\033]0;nikto\007";mkdir nikto;nikto -h http://$IP:$port | tee nikto/nikto.log; echo"The scan is saved in /nikto/nikto.log";read'&
#Gobuster
xterm -fa 'Monospace' -fs 10 -hold -geometry 80x27+1930+626 -bg purple4 -fg white -e 'echo -ne "\033]0;gobuster\007";mkdir gobuster;gobuster dir -u http://$IP:$port -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt -o gobuster/gobuster.txt;echo "The scan is save in gobuster/gobuster.txt"; read' &

