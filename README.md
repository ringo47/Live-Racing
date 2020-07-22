# Live-Racing
Raspberry pi mounted on the camera can be controlled via internet through MQTT and streamed to YouTube. Has a web interface [here](https://picam.000webhostapp.com/) and on Hackaday.io [here](https://hackaday.io/project/163091-live-racing-rpi)

I'm using cloudmqtt.com as the message broker. Replace username and password with your own in app.py

Replace your own streaming url and key in stream.sh and run it. Uses ffmpeg. Had 8ms latency. You need to setup raspivid on your Pi.You can find your key by going to Youtube > Your Channel > Other features > Live Streaming > Encoder setup > <server_url>/<key> [Eg: rtmp://a.rtmp.youtube.com/live2/abcd-1b4u-k9g9-ads0]

Replace the live stream embed url in the .html file @line 138.

Replace userName and password in the .html file in lines 101 and 102

Replace/modify the pins accordingly for your own setup. I had a L298N motordriver with 4 pins for left, right, back, forward and connected them to the RPi. (The car is a basic RC one with two motors).
