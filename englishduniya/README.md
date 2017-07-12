# debug over wifi

1. connect device with USB
    >>> adb tcpip 5555

2. get the ip of device
    >>> adb shell ip -f inet addr show wlan0

3. adb over wifi
    >>> adb connect 192.168.1.26
    >>> adb connect DEVICE_IP
