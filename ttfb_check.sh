#!/bin/bash
# Program name: ttfb_check.sh

date
cat $PWD/url_list.txt | while read output
do
	torsocks curl --silent -o /dev/null -w "Connect: %{time_connect} TTFB: %{time_starttransfer} Total time: %{time_total} Target: $output\n" $output
done
