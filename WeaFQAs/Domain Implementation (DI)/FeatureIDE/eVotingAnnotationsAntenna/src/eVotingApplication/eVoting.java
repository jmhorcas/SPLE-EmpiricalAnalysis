package eVotingApplication;

//#if logging
import java.io.FileWriter;

import java.io.BufferedWriter;
import java.io.PrintWriter;
import java.io.IOException;
//#endif

public class eVoting{
	private String dni;
	private String vote;
	private String authMechanism;
	private String encMechanism;

	
   public eVoting(String dni, String vote, String authMechanism, String encMechanism) {
		this.dni = dni;
		this.vote = vote;
		this.authMechanism = authMechanism;
		this.encMechanism = encMechanism;
	}
	
	private void println(Object obj) {
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
	
	public void vote() {
		if (authMechanism.equals("votingKey")){
			if (Authentication.votingKeyAuthentication()) {
				println("User correctly authenticated...");
				Vote encryptedVote = encryptVote(encMechanism,dni,vote);
				println(encryptedVote);
			}else {
				println("Invalid user ...");
			}
		}
		// #if mobileDevice || desktopComputer
		else {
			// #if mobileDevice
//@			if (Authentication.fingerPrintAuthentication()) {
//@				println("User correctly authenticated...");
//@				Vote encryptedVote = encryptVote(encMechanism,dni,vote);
//@				println(encryptedVote);
//@			}else {
//@				println("Invalid user ...");
//@			}
			// #endif
			// #if desktopComputer
			if (Authentication.digitalCertificateAuthentication()) {
				println("User correctly authenticated...");
				Vote encryptedVote = encryptVote(encMechanism,dni,vote);
				println(encryptedVote);
			}else {
				println("Invalid user ...");
			}		
			// #endif
		}
		//#endif
	}
	
	private Vote encryptVote(String encMechanism, String dni, String vote) {
		Vote v = new Vote(dni,vote);
		
		if (encMechanism.equals("AES")) {
			v = Encryption.AESEncryption(dni,vote);
		}
		// #if desktopComputer || votingMachine
		else if (encMechanism.equals("RSA")) {
			v = Encryption.RSAEncryption(dni,vote);
		}else if (encMechanism.equals("DES")){
			v = Encryption.DESEncryption(dni,vote);
		}
		// #endif
		
		
		return v;
	}
	
}

class Vote{
	private String dni;
	private String vote;
	
	public Vote(String dni, String vote) {
		this.dni = dni;
		this.vote = vote;
	}
	
	public String toString() {
		return "(" + dni+","+ vote+")";
	}
}
