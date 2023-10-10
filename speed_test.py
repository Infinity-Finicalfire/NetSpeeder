import speedtest

def test_speed():
    st = speedtest.Speedtest()
    
    # Get best server based on ping
    st.get_best_server()
    
    # Get ping (latency)
    ping = st.results.ping
    
    # Measure download and upload speeds
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6      # Convert to Mbps
    
    return ping, download_speed, upload_speed

def main():
    print("Testing your internet speed... Please wait.")
    ping, download, upload = test_speed()
    
    print(f"Ping (Latency): {ping} ms")
    print(f"Download Speed: {download:.2f} Mbps")
    print(f"Upload Speed: {upload:.2f} Mbps")

if __name__ == "__main__":
    main()
