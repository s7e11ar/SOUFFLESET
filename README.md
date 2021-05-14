# SOUFFLESET
Final project for Network Security. A selenium-based tool to measure Tor Browser loadtimes and latency for the Alexa Top 50 Websites.

## Overview
This toolset contains two primary parts:
1. headless.py: a Python script for automating Tor Browser page loads and measuring loadtimes.
2. ttfb_check.sh: a bash script for Curl-ing each target website via Torsocks.

## Recommended Usage:

## Requirements:
Python 3.8
tbselenium

## References: Resources helpful in building these tools
1. [What happens in a TLS handshake?](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)
2. [Torspec - Tor's protocol specifications](https://gitweb.torproject.org/torspec.git/tree/pt-spec.txt)
3. [Tor Project: Pluggable Transports](https://2019.www.torproject.org/docs/pluggable-transports.html.en)
4. [Tor: The Second-Generation Onion Router](https://www.usenix.org/legacy/publications/library/proceedings/sec04/tech/full_papers/dingledine/dingledine.pdf)
5. [Capturing HTTP/HTTPS Traffic with Tshark](https://reberhardt.com/blog/2016/10/10/capturing-https-traffic-with-tshark.html)
6. [How To Install And Use Tor (Client) As A Proxy In Ubuntu, Pop!_OS Or Linux Mint](https://www.linuxuprising.com/2018/10/how-to-install-and-use-tor-as-proxy-in.html)
7. [How to measure page load time of a website using Selenium-Python[forum]](https://www.edureka.co/community/52561/how-measure-page-load-time-of-website-using-selenium-python)
8. [Packet Capture with libpcap and other Low Level Network Tricks [PDF]](https://eecs.wsu.edu/~sshaikot/docs/lbpcap/libpcap-tutorial.pdf)
9. [Handling Tcpdump Output in Python[forum]](https://stackoverflow.com/questions/17904231/handling-tcpdump-output-in-python)
10. [HTTP GET & 200 in 1 filter[forum]](https://osqa-ask.wireshark.org/questions/9024/http-get-200-in-1-filter/)
11. [use Python + Selenium to Automate Web Timing](https://mkaz.blog/code/use-python-selenium-to-automate-web-timing/)
12. [Ping Multiple IPs Using Bash?[forum](https://askubuntu.com/questions/413367/ping-multiple-ips-using-bash)
13. [Curl Man Page](https://curl.se/docs/manpage.html)
14. [meek Wiki](https://gitlab.torproject.org/legacy/trac/-/wikis/doc/meek)
15. [webfp/tor-browser-selenium: Tor Browser automation with Selenium](https://github.com/webfp/tor-browser-selenium)
