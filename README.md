# Script to download high res images from Simony webcam 

- Enter date range in script (lines 13 & 14). Script builds url strings for images between the first and last dates set here. 
- The script loops through the images and downloads them to the current directory.
- The target (foto-webcam server) will refuse requests and throw a "Connection refused" error if there are numerous requests in a short period of time from the same IP. Try again later, use a VPN, use a different computer.
