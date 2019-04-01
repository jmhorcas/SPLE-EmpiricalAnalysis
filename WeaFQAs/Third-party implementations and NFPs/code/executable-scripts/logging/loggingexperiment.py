#! /usr/bin/python
# -*- coding: utf-8 -*-

import energymeter

VARIABLE_VALUES = (10**exp for exp in range(0, 10)) # From 1 Byte to 1 GB
PROCESS_NAME = "Java(TM)"
INTERVALS_SECONDS = "0.001"
SAMPLES = 5
FILENAME = "energy-logging.csv"

if __name__ == "__main__":
	results = energymeter.experiment_variable_values("java -Xmx16g -Djava.util.logging.config.file=logging.properties -jar LoggingJava.jar ", VARIABLE_VALUES, PROCESS_NAME, INTERVALS_SECONDS, SAMPLES)
	energymeter.save_experiment_global_results(results, FILENAME)
