#!/bin/sh
# Get the local IP address
LOCAL_IP_ADDRESS=$(ifconfig | grep 'inet ' | grep -v '127.0.0.1' | awk '{print $2}' | head -n 1)

# Export it as an environment variable
export LOCAL_IP_ADDRESS

# Print the value
echo "Local IP address set as: $LOCAL_IP_ADDRESS"

# streamlit run pages/1_Home.py --server.port=8501 --server.address=$LOCAL_IP_ADDRESS
streamlit run login.py --server.port=8501 --server.address="$LOCAL_IP_ADDRESS"
