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
[What happens in a TLS handshake?](https://www.cloudflare.com/learning/ssl/what-happens-in-a-tls-handshake/)
[Torspec - Tor's protocol specifications](https://gitweb.torproject.org/torspec.git/tree/pt-spec.txt)
[Tor Project: Pluggable Transports](https://2019.www.torproject.org/docs/pluggable-transports.html.en)
