CONFIGURATIONS FOR LOGGING FRAMEWORKS (SLF4J)

How to configure each framework:
http://saltnlight5.blogspot.com.es/2013/08/how-to-configure-slf4j-with-different.html

https://dzone.com/articles/how-configure-slf4j-different

***************************************************************************************
1. Java.util.logging
- Configuration file: logging.properties
- It requires to be included as a system property using the following command line:
	-Djava.util.logging.config.file=logging.properties

***************************************************************************************
2. Log4J
- Configuration file: log4j.properties

***************************************************************************************
3. LogBack
- Configuration file: logback.xml

***************************************************************************************
4. Simple Implementation
- Configuration file: No needed.
- It requires the following command line:
	-Dorg.slf4j.simpleLogger.logFile=log-simple.log

