package eVotingApplication;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public aspect loggingAspect {
	after(Object obj): execution(void eVoting.println(Object)) && args(obj){
		print("LoggingFile.txt",obj);
	}
	
	after(Object obj): execution(void Authentication.println(Object)) && args(obj){
		print("LoggingFile.txt",obj);
	}
	
	private void print(String fileName, Object obj) {
		try{
			FileWriter fw = new FileWriter(fileName, true);
			BufferedWriter bw = new BufferedWriter(fw);
			PrintWriter pw = new PrintWriter(bw);
			pw.println(obj);
			pw.close();
		}catch(IOException e) {
			System.err.println("Error opening the logging file");
		}
	}
}
