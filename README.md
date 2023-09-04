<h1>Intrusion Detection System</h1>


<h2>Description</h2>
This Python code uses the Pyshark library to analyze network traffic. The IDS first defines a list of suspicious ports, which are ports that are commonly used for malicious activity. Then, it defines a function called analyze_packet(), which extracts relevant information from a packet, such as the source and destination IP addresses and ports. The function then checks if the source or destination port is in the list of suspicious ports. If it is, the function prints a message indicating that suspicious traffic has been detected.    The IDS then starts a live capture of network traffic on the specified interface. For each packet that is captured, the analyze_packet() function is called to check for suspicious traffic. The IDS will continue to run until it is stopped.
<br />


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
