package eVotingApplication;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class Authentication{
	
	// #if fingerPrint
//@	public static boolean fingerPrintAuthentication() {
//@		println("Finger Print Authentication ... ");
//@		return Authentication.authentication();
//@	}
	// #endif
		
	// #if digitalCertificate
	public static boolean digitalCertificateAuthentication() {
		println("Digital Certificate Authentication ... ");
		return Authentication.authentication();
	}
	// #endif
		
	// #if votingKey
	public static boolean votingKeyAuthentication() {
		println("Voting Key Authentication ... ");
		return Authentication.authentication();
	}
	// #endif

	private static boolean authentication() {
		boolean authenticated;
		
		int auth =  new java.util.Random().nextInt(2);
		if (auth == 1) {
			authenticated = true;
		}else {
			authenticated = false;
		}
		return authenticated;
	}
	
	private static void println(Object obj) {
		System.out.println(obj);
		// #if logging
		try(FileWriter fw = new FileWriter("LoggingFile.txt", true);
			BufferedWriter bw = new BufferedWriter(fw);
			PrintWriter pw = new PrintWriter(bw))
		{
			pw.println(obj);
		}catch(IOException e) {
			System.err.println("Error opening the logging file");
		}
		// #endif
	}
}
