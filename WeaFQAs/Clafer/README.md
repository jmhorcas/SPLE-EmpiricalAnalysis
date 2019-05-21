# Clafer
The FQAs variability model in Clafer.  
The model has been imported from S.P.L.O.T by using [SPLOT2Clafer](https://github.com/jmhorcas/SPLOT2Clafer).

## Artifacts
* The [FQAs feature model](FQAs-featuremodel.txt) in Clafer format (.txt).
* The [FQAs feature model](FQAs-featuremodel.js) compiled with Clafer (.js) to be analyzed with ChocoSolver.

## Procedure
Here are the instructions to manage and work with the FQAs variability model in Clafer:

###### Download and install Clafer:
1. Download the latest version of Clafer [here](https://gsd.uwaterloo.ca/clafer-tools-binary-distributions.html).
2. Unzip and place the files in the desired device path (e.g., C:\Program Files\clafer-tools-0.4.5).
3. Add Clafer to the environment path to allow executing it from the console.

###### Modify, save, and export the variability model:
The Clafer model (.txt) can be modified within any text plain editor. For further information about Clafer notations please visit the official [Clafer website](https://www.clafer.org/).

###### Compile the FQAs variability model:
1. Download the [FQAs feature model](FQAs-featuremodel.txt) in the Clafer format (.txt).
2. In a console, type: `clafer -m choco FQAs-featuremodel.txt`  
This generates the [compiled FQAs feature model](FQAs-featuremodel.js) (.js file).

###### Generate all product configurations from the FQAs variability model:
1. In a console, type: `java -jar chocosolver.jar --file FQAs-featuremodel.js`  
**Note:** To save the generated configurations in a file add the following option: `--output <<file.txt>>`

###### Calculate numbers of configurations of the FQAs variability model:
1. In a console, type: `java -jar chocosolver.jar --no-print --file FQAs-featuremodel.js`   
**Note:** Clafer generates all configurations in order to enumerate and count them.

For further options in Clafer and in ChocoSolver use the `--help` option.

## References
* [Clafer](https://www.clafer.org/)
* [SPLOT2Clafer](https://github.com/jmhorcas/SPLOT2Clafer)
