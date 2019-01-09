# Live-Racing
Raspberry pi mounted on the camera can be controlled via internet through MQTT and streamed to YouTube.

Am using cloudmqtt.com as the message broker.

Replace user and password with your own in app.py

Replace your own streaming url and key in stream.sh and run it. Using ffmpeg. Had 8ms latency. You need to setup raspivid on your pi.

Youtube > Your Channel > Other features > Live Streaming > Encoder setup > <server_url>/<key> [Eg: rtmp://a.rtmp.youtube.com/live2/abcd-1b4u-k9g9-ads0]
  
Replace userName and password in the .html file in lines 101 and 102

Replace/modify the pins accordingly for your own setup. I had a L298N motordriver with 4 pins for left, right, back, forward and connected them to the RPi. (The car is a basic RC one with two motors).
