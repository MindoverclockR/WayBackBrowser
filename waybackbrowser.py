#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: WayBackBrowser
Dev: MindoverclockR
Date Created: July 25, 2020
Last Modified: July 28, 2020

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
import platform
import random
import shlex
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
		help="path to smokescreen html",
		default=pathlib.Path(
			os.path.join(os.path.dirname(__file__), 'index.htm')
		),
	)

	parser.add_argument(
		"-b",
		"--browser",
		type=pathlib.Path,
		help="path to the browser executable",
		default=browser_path()
	)

	parser.add_argument(
		"--maximum", type=int, help="maximum times to offset", default=10
	)

	return parser.parse_args()

def is_windows():
	if (platform.system() == "Windows"):
		return True
	elif (platform.system() == "Linux"):
		return False
	else:
		print("Unsupported OS, quitting...")
		exit()

def browser_path():
	if (is_windows()):
		try:
			return (
				pathlib.Path(
				"{}\\Google\\Chrome\\Application\\chrome.exe".format(
					os.environ["PROGRAMFILES(X86)"]
					)
				)
			)
		except KeyError:
			pass
	else:
		return (
			pathlib.Path("chromium")
		)

def change_date(target_datetime):
	if (is_windows()):
		os.system("date " + target_datetime.strftime("%m-%d-%y"))
	else:
		subprocess.run(shlex.split("sudo date -s '%s'" % target_datetime.isoformat()))

def resync_datetime():
	if (is_windows()):
		subprocess.run(["w32tm", "/resync"])
	else:
		subprocess.run(shlex.split("sudo ntpdate pool.ntp.org"))

def make_noise(
	maximum_times: int, browser: pathlib.Path, smoke: pathlib.Path
):
	""" start generating noise by opening URLs at random dates using the browser

	Args:
		maximum_times (int): maximum times to offset
		browser (pathlib.Path): path to the browser executable
		smoke (pathlib.Path): path to smokescreen html
	"""
	for i in range(maximum_times):
		# go back 1 - 5 days randomly
		time_delta = random.randint(1, 5)
		random_date = datetime.date.today() - datetime.timedelta(days=time_delta)

		# wait 15 - 30 secs randomly
		sleep_time = random.randint(15, 30)

		# print and change to the target system date
		print("Selected random date: {}".format(random_date.strftime("%m-%d-%y")))
		change_date(random_date)

		# make BROWSER_PROCESS global so it can be killed outside of this function
		global BROWSER_PROCESS

		# open the browser as a subprocess for sleep_time, do not output errors to console
		BROWSER_PROCESS = subprocess.Popen([browser, smoke], stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
		time.sleep(sleep_time)

		BROWSER_PROCESS.terminate()


def main():
	# parse command line arguments
	args = parse_arguments()

	# synchronize current system time
	resync_datetime()

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
				exit()

	finally:
		print("Execution completed, restoring system time")
		resync_datetime()


if __name__ == "__main__":
	main()
