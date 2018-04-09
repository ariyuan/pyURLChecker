import requests
import sys
import argparse
import time


def call_url(url):
    try:
        request = requests.get(url)
        return request.status_code
    except:
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Utility for checking URL is accessible')
    parser.add_argument('url', help='URL to check')
    parser.add_argument('-w', '--wait_time', type=int, help='wait time')
    args = parser.parse_args()

    if args.wait_time is None:
        args.wait_time = 0
    while args.wait_time >= 0:
        response = call_url(args.url)
        if response == 200:
            print('Web site exists')
            sys.exit(0)
        else:
            print('Web site does not exist, wait for 1 minutes...')
            args.wait_time -= 1
            time.sleep(60)
    sys.exit(1)

