#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import ippetlauncher
import ippetparser
import energymeter

# CONSTANTS
IPPET_ENERGY_LOG_FILENAME_SUFIX = "_processes.xls"
IPPET_PROCESS_LOG_FILENAME_SUFIX = "_sys_info.xls"

VARIABLE_KEY = "Variable"
SAMPLE_KEY = "Sample"
PROCESS_KEY = "Process"
COMPUTATIONAL_TIME_KEY = "Computational Time (s)"
USAGE_CPU_KEY = "Usage CPU (%)"
CONSUMED_ENERGY_KEY = "Consumed energy (J)"
POWER_KEY = "Power (W)"

if __name__ == "__main__":
	if len(sys.argv) != 9:
		print("Usage:")
		print("usagemodel <process> <variable_min> <variable_max> <variable_increment> <process_name> <intervals_seconds> <samples> <filename>")
	else:
		command = sys.argv[1]
		command = '"' + command + ' "'
		variable_min = int(sys.argv[2])
		variable_max = int(sys.argv[3])
		variable_incr = int(sys.argv[4])
		process_name = sys.argv[5]
		intervals_seconds = sys.argv[6]
		samples = int(sys.argv[7])
		filename = sys.argv[8]

		# Launch command and monitor the energy consumption
		results = energymeter.experiment_variable(command, variable_min, variable_max, variable_incr, process_name, intervals_seconds, samples)
		energymeter.save_experiment_global_results(results, filename)
