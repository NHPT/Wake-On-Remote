# Wake-On-Remote
Remote wake-up computer program developed by Python and pyqt5.

# info File
You can edit the info file to import the host information to wake up. It needs the domain name / IP address, MAC address and port. The format is as follows:  
__Domain/IP MAC PORT__  
#### For example:  
123.123.123.123 :XX:XX:XX:XX:XX:XX 9  
test.test.com XX:XX:XX:XX:XX:XX 8  

# Usage
## Remote Wake  
Run python3 wakeonremote.py, and then double-click the host to wake up in the list, as shown in the figure:  
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/example.png)  
Run python3 wakeonremote.py, fill in the domain name / host, MAC and port, and then click wake-up, as shown in the figure:  
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/example2.png)
You can also use WakeOnRemote_console.py
## Local Wake  
Testing use WakeOnRemote_console.py:
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/wake.png)
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/send.png)
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/waked.png)

# OS Config  
https://blog.csdn.net/qq_32261191/article/details/102885664
