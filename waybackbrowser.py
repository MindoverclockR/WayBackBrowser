#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: WayBackBrowser
Dev: MindoverclockR
Date Created: July 25, 2020
Last Modified: July 25, 2020

Editor: K4YT3X
Last Modified: July 25, 2020

Description: Browse randomly at random dates in the past (only to browser history)
"""

# built-in imports
import argparse
import contextlib
import datetime
import os
import pathlib
import random
import subprocess
import time

BROWSER_PROCESS = None


def parse_arguments():
    """ parse CLI arguments
    """
    parser = argparse.ArgumentParser(
        prog="waybackbrowser", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-s",
        "--smoke",
        type=pathlib.Path,
        help="path to smokescreen",
        default=pathlib.Path(
            "{}\\Downloads\\smokescreen-master\\index.htm".format(
                os.environ["USERPROFILE"]
            )
        ),
    )

    parser.add_argument(
        "-b",
        "--browser",
        type=pathlib.Path,
        help="path to browser",
        default=pathlib.Path(
            "{}\\Google\\Chrome\\Application\\chrome.exe".format(
                os.environ["PROGRAMFILES(X86)"]
            )
        ),
    )

    parser.add_argument(
        "--maximum", type=int, help="maximum times to go back a few days", default=10
    )

    return parser.parse_args()


def make_noise(
    maximum_times: int, browser: pathlib.Path, smoke: pathlib.Path
):
    """ start generating noise by opening URLs at random dates using the browser

    Args:
        maximum_days (int): maximum days to offset
        browser (pathlib.Path): path to the browser executable
        smoke (pathlib.Path): path to the smoke html
    """
    for i in range(maximum_times):
        # go back 1 - 5 days randomly
        time_delta = random.randint(1, 5)
        random_datetime = datetime.date.today() - datetime.timedelta(days=time_delta)

        # wait 15 - 30 secs randomly
        sleep_time = random.randint(15, 30)

        # print and change to the target system date
        print("Selected random date: {}".format(random_datetime.strftime("%m-%d-%y")))
        os.system("date " + random_datetime.strftime("%m-%d-%y"))

        # make BROWSER_PROCESS global so it can be killed outside of this function
        global BROWSER_PROCESS

        # open the browser as a subprocess for sleep_time
        BROWSER_PROCESS = subprocess.Popen([browser, smoke])
        time.sleep(sleep_time)

        BROWSER_PROCESS.terminate()


def main():

    # parse command line arguments
    args = parse_arguments()

    # synchronize current system time
    subprocess.run(["w32tm", "/resync"])

    # start to make noise
    try:
        make_noise(args.maximum, args.browser, args.smoke)

    # kill browser on KeyboardInterrupt
    except (KeyboardInterrupt, SystemExit):
        print("Program interrupted, terminating the browser process")
        with contextlib.suppress(Exception):
            if (
                isinstance(BROWSER_PROCESS, subprocess.Popen)
                and BROWSER_PROCESS.poll() is None
            ):
                BROWSER_PROCESS.terminate()

    finally:
        print("Execution completed, restoring system time")
        subprocess.run(["w32tm", "/resync"])


if __name__ == "__main__":
    main()
