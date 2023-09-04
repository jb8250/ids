import pyshark

# Define the list of suspicious ports
suspicious_ports = ["80", "443", "22", "23", "445", "3389", "8080", "3306"]
# Add more ports as needed

def analyze_packet(packet):
    # Extract relevant information from the packet
    src_ip = packet.ip.src
    dst_ip = packet.ip.dst
    src_port = packet[packet.transport_layer].srcport
    dst_port = packet[packet.transport_layer].dstport

    # Check if the source or destination port is in the list of suspicious ports
    if src_port in suspicious_ports or dst_port in suspicious_ports:
        print(f"Suspicious traffic detected - Source: {src_ip}:{src_port}, Destination: {dst_ip}:{dst_port}")

# Replace 'eth0' with your network interface
cap = pyshark.LiveCapture(interface='en0', display_filter='tcp')

print("Intrusion Detection System (IDS) is running...")

for packet in cap.sniff_continuously():
    analyze_packet(packet)

