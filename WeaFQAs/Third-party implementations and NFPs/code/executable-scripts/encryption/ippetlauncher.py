#! /usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os

# CONSTANTS
IPPET_LOG_FILENAME = "energy"
IPPET_STDOUT = "ippet-stdout.tmp"

def monitor_process(process, intervals_seconds):
	""" Launch the process and monitor the power consumption using the IPPET tool.
	Return the name of the .xls file generated with the power information for all process in the system."""
	ippet = subprocess.run(["ippet", "-auto_load", "n", "-enable_web", "n", "-log_file", IPPET_LOG_FILENAME, "-zip", "n", "-stdout", IPPET_STDOUT, "-interval", intervals_seconds, "-cmd_to_run", process], shell=True)
	#ippet = subprocess.run(["ippet", "-auto_load", "n", "-enable_web", "n", "-log_file", IPPET_LOG_FILENAME, "-zip", "n", "-interval", intervals_seconds, "-cmd_to_run", process], shell=True)
	try:
		os.remove(IPPET_STDOUT)
	except:
		pass
	return IPPET_LOG_FILENAME

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage:")
		print("python ippetlauncher <process with args> <intervals_seconds>")
	else:
		command = sys.argv[1]
		command = '"' + command + '"'
		intervals_seconds = sys.argv[2]

		# Launch command and monitor the energy consumption
		monitor_process(command, intervals_seconds)
