# 简介[Introduction]
基于Python3开发的远程唤醒计算机程序，支持PC客户端、命令行和网页。网页端主要为了移动端使用。  
A remote wake-up computer program developed based on Python3, supporting PC clients, command lines, and web pages. The web end is mainly designed for mobile app use.

# 配置文件[Config file]
您可以编辑`info`文件以导入要唤醒的主机信息。它需要域名/IP地址、MAC地址和端口。格式如下：  
You can edit the info file to import the host information to wake up. It needs the domain name / IP address, MAC address and port. The format is as follows:  
__`Domain/IP` `MAC` `PORT`__  

#### 示例[Example]  
123.123.123.123 :XX:XX:XX:XX:XX:XX 9  
test.test.com XX:XX:XX:XX:XX:XX 8  

# 用法[Usage]
## PC端远程唤醒[PC Remote Wake]  
运行`python3 wakeonremote.py`，然后双击列表中要唤醒的主机，如图所示：  
Run `python3 wakeonremote.py`, and then double-click the host to wake up in the list, as shown in the figure:  
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/example.png)  
运行`python3 wakeonremote.py`，填写域名/主机、MAC和端口，然后点击唤醒，如图所示：  
Run `python3 wakeonremote.py`, fill in the domain name / host, MAC and port, and then click wake-up, as shown in the figure:  
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/example2.png)
您也可以使用`WakeOnMotor_console.py`  
You can also use WakeOnRemote_console.py

## PC端命令行局域网唤醒[PC Local Wake]  
使用`WakeOnmote_sole.py`：  
Using `WakeOnRemote_console.py`:  
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/wake.png)  
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/send.png)  
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/waked.png)  

## Web端网页唤醒[Web Remote Wake]  
运行`python3 wake.py`即可启动web服务，默认监听在本地80端口，如果需要部署在公网，修改代码监听地址即可。可以使用PC、Android或iOS的浏览器访问，实现简易的跨平台使用。  
Run 'python3 wake. py' to start the web service. By default, it listens to port 80 locally. If it needs to be deployed on the public network, simply modify the code listening address. It can be accessed using PC, Android, or iOS browsers for easy cross platform use.  
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/wap.png)
![Image text](https://github.com/NHPT/Wake-On-Remote/blob/master/example/pc.png)  

# OS Config  
https://blog.csdn.net/qq_32261191/article/details/102885664
