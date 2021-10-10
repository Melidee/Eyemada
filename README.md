# Eyemada  
Eyemada v1.0.0 by Melidee <https://github.com/Melidee>  
Armada v1.0.2 by d0nutptr <d0nut@resync.gg>  

Eyemada is a graphical interface for the Armada port scanner  
**NOTE: Due to this program using the subprocess module it has permissions to run shell commands and should be used with caution**

**Install Guide**  
    Install Armada via resync.gg's github <https://github.com/resyncgg/armada>  
    Install tkinter with `sudo apt-get install python-tk`  
    Install sockets with `pip install sockets`  
    Install Validators with `pip install validators`  
    Download eyemada.py with `git clone https://github.com/Melidee/Eyemada.git`  

**Usage Guide**  
    Target - the target of the scan - accepts IPv4 or CIDR  
    Ports - sets which ports to scan - accepts a single port, a port range, or multiple ports  
    Scan Name - what the scan will be listed as - defaults to target ip  
    Scan - starts the port scan  
    Toggle Help Text - shows usage guide in GUI  
