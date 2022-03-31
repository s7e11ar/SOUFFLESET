# SOUFFLESET
Final project for Network Security. A selenium-based tool to measure Tor Browser loadtimes and latency for the Alexa Top 50 Websites.

## Overview
This toolset contains two primary parts:
1. headless.py: a Python script for automating Tor Browser page loads and measuring loadtimes.
2. ttfb_check.sh: a bash script for Curl-ing each target website via Torsocks.

## Installation & Environment Preparation
Install GCC, make and perl if needed:
```
sudo apt install gcc make perl
```

### Get Tor Browser Bundle and Verify
Download the current version of the tor browser bundle(your version will be different):
```
wget https://www.torproject.org/dist/torbrowser/10.0.16/tor-browser-linux64-10.0.16_en-US.tar.xz
```

Grab the OpenPGP signature:
```
wget https://www.torproject.org/dist/torbrowser/10.0.16/tor-browser-linux64-10.0.16_en-US.tar.xz.asc
```

Import the Tor Browser Developers signing key:
```
gpg --auto-key-locate nodefault,wkd --locate-keys torbrowser@torproject.org
```

Save it to a file:
```
gpg --output ./tor.keyring --export 0xEF6E286DDA85EA2A4BA7DE684E2C6E8793298290
```

Finally, verify the signature:
```
gpgv --keyring ./tor.keyring ./tor-browser-linux64-10.0.16_en-US.tar.xz.asc  ./tor-browser-linux64-10.0.16_en-US.tar.xz
```
### Install Tor, Service Dependencies, and Other Tools We'll Need
```
sudo apt install tor tor-geoipdb torsocks privoxy curl whois python3 python-dev python3-pip software-properties-common
```
Install tbselenium with pip:
```
pip3 install tbselenium
```
Install PyVirtualDisplay with Pip3
```
pip3 install pyvirtualdisplay
```
Get Geckodriver
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
tar -xvzf geckodriver-v0.30.0-linux64.tar.gz
sudo mv geckodriver /usr/local/bin
```
Install X Virtual Frame Buffer (xvfb)
```
sudo apt install xvfb
```

## Recommended Usage:
Clone this repo:
```
git clone https://github.com/s7e11ar/SOUFFLESET.git
cd SOUFFLESET
```
Start tor if it isn't running:
```
tor
```
Run headless.py (with the path to your Tor Browser executable):
```
python3 headless.py /home/[your name]/Downloads/tor-browser_en-US/
```
Run ttfb_check.sh:
```
./ttfb_check.sh
```

## References: Resources helpful in building these tools
1. [Tor Project](https://www.torproject.org)
2. [What happens in a TLS handshake?](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)
3. [Torspec - Tor's protocol specifications](https://gitweb.torproject.org/torspec.git/tree/pt-spec.txt)
4. [Tor Project: Pluggable Transports](https://2019.www.torproject.org/docs/pluggable-transports.html.en)
5. [Tor: The Second-Generation Onion Router](https://www.usenix.org/legacy/publications/library/proceedings/sec04/tech/full_papers/dingledine/dingledine.pdf)
6. [Capturing HTTP/HTTPS Traffic with Tshark](https://reberhardt.com/blog/2016/10/10/capturing-https-traffic-with-tshark.html)
7. [How To Install And Use Tor (Client) As A Proxy In Ubuntu, Pop!_OS Or Linux Mint](https://www.linuxuprising.com/2018/10/how-to-install-and-use-tor-as-proxy-in.html)
8. [How to measure page load time of a website using Selenium-Python[forum]](https://www.edureka.co/community/52561/how-measure-page-load-time-of-website-using-selenium-python)
9. [Packet Capture with libpcap and other Low Level Network Tricks [PDF]](https://eecs.wsu.edu/~sshaikot/docs/lbpcap/libpcap-tutorial.pdf)
10. [Handling Tcpdump Output in Python[forum]](https://stackoverflow.com/questions/17904231/handling-tcpdump-output-in-python)
11. [HTTP GET & 200 in 1 filter[forum]](https://osqa-ask.wireshark.org/questions/9024/http-get-200-in-1-filter/)
12. [use Python + Selenium to Automate Web Timing](https://mkaz.blog/code/use-python-selenium-to-automate-web-timing/)
13. [Ping Multiple IPs Using Bash?[forum]](https://askubuntu.com/questions/413367/ping-multiple-ips-using-bash)
14. [Curl Man Page](https://curl.se/docs/manpage.html)
15. [meek Wiki](https://gitlab.torproject.org/legacy/trac/-/wikis/doc/meek)
16. [webfp/tor-browser-selenium: Tor Browser automation with Selenium](https://github.com/webfp/tor-browser-selenium)
