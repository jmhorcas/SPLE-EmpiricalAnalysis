#! /usr/bin/python
# -*- coding: utf-8 -*-

import energymeter

#VARIABLE_VALUES = (10**exp for exp in range(0, 10)) # From 1 Byte to 1 GB
#VARIABLE_VALUES = [0, 200000, 400000, 600000, 800000, 1000000]
#VARIABLE_VALUES = [0, 200, 400, 600, 800, 1000]
#VARIABLE_VALUES = [0, 20, 40, 60, 80, 100]
#VARIABLE_VALUES = [0, 2, 4, 6, 8, 10]
SIZE = 200
VARIABLE_VALUES = [0, int(0.2*SIZE), int(0.4*SIZE), int(0.6*SIZE), int(0.8*SIZE), SIZE]
PROCESS_NAME = "Java(TM)"
INTERVALS_SECONDS = "0.001"
SAMPLES = 5
FILENAME = "energy-caching.csv"

if __name__ == "__main__":
	results = energymeter.experiment_variable_values("java -Xmx16g -jar Caching-Consult-200.jar ", VARIABLE_VALUES, PROCESS_NAME, INTERVALS_SECONDS, SAMPLES)
	energymeter.save_experiment_global_results(results, FILENAME)
