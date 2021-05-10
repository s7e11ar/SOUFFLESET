from argparse import ArgumentParser
from tbselenium.tbdriver import TorBrowserDriver
from tbselenium.utils import start_xvfb, stop_xvfb
from os.path import join, dirname, realpath
import time
import csv

URLS = 0
VANILLA = 1
OBFS4 = 2
MEEK = 3

BRIDGE_TYPE = ["obfs4", "meek-azure"]

fields = ['URL', 'Vanilla', 'OBFS4', 'MEEK-Azure']
load_table = [['https://www.google.com', 0, 0, 0, 0],
        ['https://www.youtube.com', 0, 0, 0, 0],
        ['https://www.amazon.com', 0, 0, 0, 0],
        ['https://www.yahoo.com', 0, 0, 0, 0],
        #['https://www.zoom.us', 0, 0, 0], exclude - hang
        ['https://www.facebook.com', 0, 0, 0, 0],
        ['https://www.reddit.com', 0, 0, 0, 0],
        ['https://www.wikipedia.org', 0, 0, 0, 0],
        ['https://www.myshopify.com', 0, 0, 0, 0],
        ['https://www.office.com', 0, 0, 0, 0],
        ['https://www.ebay.com', 0, 0, 0, 0],
        ['https://www.bing.com', 0, 0, 0, 0],
        ['https://www.live.com', 0, 0, 0, 0],
        ['https://www.microsoft.com', 0, 0, 0, 0],
        ['https://www.instructure.com', 0, 0, 0, 0],
        ['https://www.chase.com', 0, 0, 0, 0],
        ['https://www.instagram.com', 0, 0, 0, 0],
        #['https://www.netflix.com', 0, 0, 0], exclude - hang
        #['https://www.microsoftonline.com', 0, 0, 0], exclude - hang
        ['https://www.zillow.com', 0, 0, 0, 0],
        ['https://www.twitch.tv', 0, 0, 0, 0],
        ['https://www.force.com', 0, 0, 0, 0],
        ['https://www.intuit.com', 0, 0, 0, 0],
        ['https://www.linkedin.com', 0, 0, 0, 0],
        ['https://www.etsy.com', 0, 0, 0, 0],
        ['https://www.apple.com', 0, 0, 0, 0],
        ['https://www.adobe.com', 0, 0, 0, 0],
        ['https://www.chaturbate.com', 0, 0, 0, 0],
        ['https://www.cnn.com', 0, 0, 0, 0],
        ['https://www.walmart.com', 0, 0, 0, 0],
        #['https://www.espn.com', 0, 0, 0], exclude - hang
        ['https://www.twitter.com', 0, 0, 0, 0],
        ['https://www.dropbox.com', 0, 0, 0, 0],
        ['https://www.indeed.com', 0, 0, 0, 0],
        ['https://www.nytimes.com', 0, 0, 0, 0],
        ['https://www.wellsfargo.com', 0, 0, 0, 0],
        ['https://www.okta.com', 0, 0, 0, 0],
        ['https://www.salesforce.com', 0, 0, 0, 0],
        ['https://www.craigslist.org', 0, 0, 0, 0],
        ['https://www.homedepot.com', 0, 0, 0, 0],
        #['https://www.ca.gov', 0, 0, 0], exclude - govt
        ['https://www.hulu.com', 0, 0, 0, 0],
        ['https://www.quizlet.com', 0, 0, 0, 0],
        #['https://www.aliexpress.com', 0, 0, 0], exclude - hang
        ['https://www.imdb.com', 0, 0, 0, 0],
        ['https://www.usps.com', 0, 0, 0, 0],
        ['https://www.imgur.com', 0, 0, 0, 0],
        #['https://www.amazonaws.com', 0, 0, 0], exclude - killed
        ['https://www.canva.com', 0, 0, 0, 0],
        ['https://www.fidelity.com', 0, 0, 0, 0]]

def headless_visit(tbb_dir):
    out_img = join(dirname(realpath(__file__)), "headless_screenshot.png")
    # start a virtual display
    xvfb_display = start_xvfb()
    with TorBrowserDriver(tbb_dir) as driver:
        for i in range(len(load_table)):
            start_time = time.clock_gettime_ns(time.CLOCK_REALTIME)
            driver.load_url(load_table[i][URLS])
            end_time = time.clock_gettime_ns(time.CLOCK_REALTIME)
            
            driver.get_screenshot_as_file(out_img)
            print("Screenshot is saved as %s" % out_img)
            
            elapsed_time = (end_time - start_time) / 1000000000
            print("Load time: ", str(elapsed_time) + "s")
            load_table[i][VANILLA] = elapsed_time
    
    col = -1
    for bridge in BRIDGE_TYPE:
        with TorBrowserDriver(tbb_dir, default_bridge_type=bridge) as bdriver:
            if bridge == "obfs4": 
                col = 2
                print("obfs4..........")
            if bridge == "meek-azure": 
                col = 3
                print("meek-azure..........")
            if col == -1: 
                break

            for i in range(len(load_table)):
                start_time = time.clock_gettime_ns(time.CLOCK_REALTIME)
                bdriver.load_url(load_table[i][URLS])
                end_time = time.clock_gettime_ns(time.CLOCK_REALTIME)
            
                bdriver.get_screenshot_as_file(out_img)
                print("Screenshot is saved as %s" % out_img)
            
                elapsed_time = (end_time - start_time) / 1000000000
                print("Load time: ", str(elapsed_time) + "s")
                load_table[i][col] = elapsed_time
    print("About to print..........")
    write_csv()
    stop_xvfb(xvfb_display)


def main():
    desc = "Headless visit and screenshot of check.torproject.org using XVFB"
    parser = ArgumentParser(description=desc)
    parser.add_argument('tbb_path')
    args = parser.parse_args()
    headless_visit(args.tbb_path)

def write_csv():
    print("Inside write_csv..........")
    with open('/home/chive/output/test_results.csv', 'w') as f:
        # using csv.writer, write to a csv file
        write = csv.writer(f)

        write.writerow(fields)
        write.writerows(load_table)
        print(fields)

if __name__ == '__main__':
    main()
