#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import ippetlauncher
import ippetparser
import csv
import statistics

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

def experiment_variable_values(process, values, process_name, intervals_seconds, samples):
	global_results = []
	for i in values:
		results = experiment(process + str(i), process_name, intervals_seconds, samples)
		metrics_resume = get_energy_metrics_resume(results)
		global_results.append([metrics_resume[0]] + [i] + metrics_resume[1:])

	return global_results

def experiment_variable(process, variable_min, variable_max, variable_increment, process_name, intervals_seconds, samples):
	global_results = []
	for i in range(variable_min, variable_max+1, variable_increment):
		results = experiment(process + str(i), process_name, intervals_seconds, samples)
		metrics_resume = get_energy_metrics_resume(results)
		global_results.append([metrics_resume[0]] + [i] + metrics_resume[1:])

	return global_results

def experiment(process, process_name, intervals_seconds, samples):
	""" Execute an experiment that consists on launching n times (samples) the application (process).
	intervals_seconds is the frequency to measure the power with the IPPET tool.
	Return for each sample (process name, computational time, usage cpu, total joules, watts)
	"""
	results = []
	for i in range(samples):
		filename = ippetlauncher.monitor_process(process, intervals_seconds)
		energy_log_filename = filename + IPPET_ENERGY_LOG_FILENAME_SUFIX
		energy_profile = ippetparser.get_energy_profile(energy_log_filename, process_name)
		results.append([i+1] + list(energy_profile))

	try:
		os.remove(filename + IPPET_ENERGY_LOG_FILENAME_SUFIX)
		os.remove(filename + IPPET_PROCESS_LOG_FILENAME_SUFIX)
	except:
		pass

	return results

def save_experiment_results(results, filename='energy_profile_samples.csv'):
	"""
	The result is a .csv file (filename) with the energy profile of the application for an execution with multiple samples.
	"""
	with open(filename, 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([SAMPLE_KEY, PROCESS_KEY, COMPUTATIONAL_TIME_KEY, USAGE_CPU_KEY, CONSUMED_ENERGY_KEY, POWER_KEY])
		for r in results:
			spamwriter.writerow(r)

def save_experiment_global_results(results, filename='energy_profile_experiment.csv'):
	"""
	The result is a .csv file (filename) with the global energy profile of the application with multiple variables.
	"""
	with open(filename, 'w', newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow([PROCESS_KEY, VARIABLE_KEY, COMPUTATIONAL_TIME_KEY, USAGE_CPU_KEY, CONSUMED_ENERGY_KEY, POWER_KEY])
		for r in results:
			spamwriter.writerow(r)

def get_energy_metrics_resume(results):
	metrics = list(zip(*results))
	computational_time_median = statistics.median(metrics[2])
	usage_cpu_median = statistics.median(metrics[3])
	consumed_energy_median = statistics.median(metrics[4])
	power_median = statistics.median(metrics[5])

	return [metrics[1][0], computational_time_median, usage_cpu_median, consumed_energy_median, power_median]

def print_metrics_resume(metrics_resume):
	print("Process name: " + metrics_resume[0])
	print("Computational time (s): ", metrics_resume[1])
	print("CPU usage (%): ", metrics_resume[2])
	print("Consumed energy (J): ", metrics_resume[3])
	print("Consumed power (W): ", metrics_resume[4])

if __name__ == "__main__":
	if len(sys.argv) != 6:
		print("Usage:")
		print("energymeter <process with args> <process_name> <intervals_seconds> <samples> <filename>")
	else:
		command = sys.argv[1]
		command = '"' + command + '"'
		process_name = sys.argv[2]
		intervals_seconds = sys.argv[3]
		samples = int(sys.argv[4])
		filename = sys.argv[5]

		# Launch command and monitor the energy consumption
		results = experiment(command, process_name, intervals_seconds, samples)
		save_experiment_results(results, filename)
		metrics_resume = get_energy_metrics_resume(results)
		print_results(metrics_resume)
