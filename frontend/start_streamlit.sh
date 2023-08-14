#!/bin/bash
if [[ "$OSTYPE" == "darwin"* ]]; then
  # macOS command to get local IP address
  LOCAL_IP_ADDRESS=$(ifconfig | grep 'inet ' | grep -v '127.0.0.1' | awk '{print $2}' | head -n 1)
  # Run Streamlit with the LOCAL_IP_ADDRESS
  streamlit run login.py --server.port=8501 --server.address="$LOCAL_IP_ADDRESS"
else
  # Assuming a Linux environment, just run Streamlit without specifying the address
  streamlit run login.py --server.port=8501 --server.address="0.0.0.0"
fi
