import speedtest

def format_speed(bps):
   
    return f"{bps / (1024 * 1024):.2f} Mbps"

def test_speed():
    print("\n Network Speed Tester")
    print("-" * 30)
    st = speedtest.Speedtest()

    print(" Finding best server...")
    st.get_best_server()

    print("Testing download speed...")
    download_speed = st.download()

    print(" Testing upload speed...")
    upload_speed = st.upload()

    print(" Testing ping...")
    ping_result = st.results.ping

    print("\n Speed Test Results:")
    print(f"  Download: {format_speed(download_speed)}")
    print(f"  Upload:   {format_speed(upload_speed)}")
    print(f"  Ping:     {ping_result:.2f} ms")

if __name__ == "__main__":
    test_speed()
