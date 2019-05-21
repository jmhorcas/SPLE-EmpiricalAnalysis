# FeatureIDE
This project contains the FQAs variability model in FeatureIDE as well as some of the FQAs's artifacts implemented in FeatureIDE.  
The variability model has been imported from S.P.L.O.T..

We have implemented the **Authentication**, **Encryption**, and **Logging** FQAs for an [electronic voting (e-voting)](https://doi.org/10.1016/j.jss.2015.11.005) application following several variability approaches supported by FeatureIDE. These FQAs have been represented as *feature*, *aspects*, *annotations*, or a combination of them, based on the specific approach, and implemented as black boxs to be filled with the desired framework/library third-party implementation.  
The e-voting application serves as case study where the FQAs has been integrated. The main functionality of the e-voting application is exposed through its interface (`eVotingInterface.java`). The application has been implemented following the MVC pattern (see `eVoting.java`, `eVotingController.java` and `eVotingView.java` classes).

## Artifacts
* The [FQAs variability model](FQAsVariabilityModel/) project with the FQAs feature model imported from the S.P.L.O.T. tool.
* The [Antenna](eVotingAnnotationsAntenna/) project with the FQAs components implemented using annotations.
* The [Feature House and Java](eVotingFHJava/) project with the FQAs components implemented using the Feature-Oriented Programming (FOP) paradigm.
* The [Feature House and AspectJ](eVoting-FH-AspectJ/) project with the FQAs components implemented using a combination of both FOP and Aspect-Oriented Programming (AOP) paradigm.

## Procedure
Here are the instructions to manage and work with the WeaFQAs artifacts in FeatureIDE:

###### Download, install, and setup FeatureIDE:
1. Download the latest version of FeatureIDE from [here](http://www.featureide.com/).
2. Install FeatureIDE as any usual Eclipse version.
3. Configure the workspace to be used.

###### Import, compile and execute the FeatureIDE's projects:
1. For each FeatureIDE project in this repository, download it, and place it in the workspace location.
2. In FeatureIDE, import each project as an existing Java project in the workspace.
3. The project will be automatically compiled in Java.
4. For each project, launch the application `eVotingMain.java` by clicking on `Run as → Java Application`.

## References
* [FeatureIDE](http://www.featureide.com/)
* [Antenna](http://antenna.sourceforge.net/)  
* [Feature House](http://www.fosd.de/fh)  
* [Java](https://www.oracle.com/technetwork/java/index.html)  
* [AspectJ](https://www.eclipse.org/aspectj/index.php)  
* [The e-voting case study](https://doi.org/10.1016/j.jss.2015.11.005)  
