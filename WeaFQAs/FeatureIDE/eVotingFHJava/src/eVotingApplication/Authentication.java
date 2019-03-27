package eVotingApplication; 

import java.io.FileWriter; 

import java.io.BufferedWriter; 
import java.io.PrintWriter; 
import java.io.IOException; 

public   class  Authentication {
	
	
	 private static void  println__wrappee__authentication  (Object obj) {
		System.out.println(obj);
	}

	
	
	private static void println(Object obj) {
		println__wrappee__authentication(obj);
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

	
	
	public static boolean votingKeyAuthentication() {
		println("Voting Key Authentication ... ");
		return Authentication.authentication();
	}

	
	
	public static boolean digitalCertificateAuthentication() {
		println("Digital Certificate Authentication ... ");
		return Authentication.authentication();
	}

	
	
	public static boolean fingerPrintAuthentication() {
		println("Finger Print Authentication ... ");
		return Authentication.authentication();
	}


}
