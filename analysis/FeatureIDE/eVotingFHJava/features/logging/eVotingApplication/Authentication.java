package eVotingApplication;

import java.io.FileWriter;

import java.io.BufferedWriter;
import java.io.PrintWriter;
import java.io.IOException;

public class Authentication{
	
	private static void println(Object obj) {
		original(obj);
		try{
			FileWriter fw = new FileWriter("LoggingFile.txt", true);
			BufferedWriter bw = new BufferedWriter(fw);
			PrintWriter pw = new PrintWriter(bw);
			pw.println(obj);
			pw.close();
		}catch(IOException e) {
			System.err.println("Error opening the logging file");
		}
	}
}
