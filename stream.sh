#!/bin/bash
raspivid -o - -t 0 -vf -hf -fps 10 -b 300000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 64k -g 50 -strict experimental -f flv <enter stream url here>
