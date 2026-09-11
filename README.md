# 🌐 Computer Networks: Traffic Analysis & Socket Programming

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-Packet%20Analysis-1679A7?style=flat&logo=wireshark&logoColor=white)
![Scapy](https://img.shields.io/badge/Scapy-Packet%20Crafting-red?style=flat)
![Sockets](https://img.shields.io/badge/TCP%2FIP-Socket%20Programming-brightgreen?style=flat)

A hands-on networking project covering end-to-end network traffic simulation, packet-level protocol inspection (HTTP/TCP/IP), and multi-client socket communication in Python.

---

## 📌 Project Overview

The project is structured into two core components:
1. **Traffic Synthesis & Protocol Inspection:** Replaying and injecting structured HTTP network flows from dataset inputs, capturing the live exchange into `.pcap` captures, and performing deep packet inspection.
2. **Client-Server Socket Architecture:** Implementing custom TCP client-server chat orchestration with concurrent connection handling and validating transmission integrity via packet captures.

---

## ⚙️ Components & Modules

### 🔹 Part 1: Packet Crafting & Traffic Analysis
* **Traffic Replay:** Reads and normalizes structured network activity records (`group23_http_input.csv`).
* **Packet Generation:** Constructs custom IP, TCP, and HTTP frames and transmits them across network interfaces.
* **PCAP Inspection:** Inspects packet flows (`network_capture.pcap`) using Wireshark and Python tools (`network_project.ipynb`), validating sequence numbers, acknowledgment flags, handshake integrity, and payload decoding.

### 🔹 Part 2: Multi-Client TCP Socket System
* **Chat Server (`chat_server.py`):** Multi-threaded socket server managing concurrent client connections, broadcast dispatching, and graceful disconnections.
* **Chat Client (`chat_client.py`):** Interactive terminal client establishing low-level socket connections with dedicated receive and send threads.
* **Verification (`capture.pcap`):** Network capture validating socket handshakes (SYN, SYN-ACK, ACK), payload delivery, and teardown states (FIN/RST).
* **Specifications & Guides:** Protocol specifications and socket execution documentation.

---

## 📂 Repository Structure

```text
├── part 1/
│   ├── network_project.ipynb              # Jupyter notebook for traffic analysis
│   ├── group23_http_input.csv             # Source HTTP dataset
│   └── network_capture.pcap               # Captured network traffic trace
├── part 2/
│   ├── chat_server.py                     # Multi-client TCP socket server
│   ├── chat_client.py                     # Interactive socket client
│   ├── capture.pcap                       # TCP socket exchange packet trace
│   ├── data_structure_specification.pdf   # Data structure definitions and protocol layout
│   └── client_server_guide.pdf            # Client-server setup and execution instructions
└── README.md                              # Repository documentation                    
```


## 🚀 Getting Started

1. Prerequisites
Clone the repository and install the required dependencies:

```text
git clone [https://github.com/ofirhotz/network-traffic-analysis-and-sockets.git](https://github.com/ofirhotz/network-traffic-analysis-and-sockets.git)
cd network-traffic-analysis-and-sockets
pip install scapy pandas matplotlib notebook
```



2. Running Part 1 (Traffic Analysis)
Launch the analysis notebook:
```text
cd "part 1"
jupyter notebook network_project.ipynb
```

  You can also open network_capture.pcap directly in Wireshark for packet-by-packet filtering.



3. Running Part 2 (Socket Chat)
Start the Server:
```text
cd "part 2"
python chat_server.py
```

Connect Clients (run in separate terminals):
```text
python chat_client.py
```






