package eVotingApplication; 

import java.io.FileWriter; 

import java.io.BufferedWriter; 
import java.io.PrintWriter; 
import java.io.IOException; 

public   class  eVoting {
	
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

	
	
	 private void  println__wrappee__eVoting  (Object obj) {
		System.out.println(obj);
	}

	
	private void println(Object obj) {
		println__wrappee__eVoting(obj);
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

	
	
	 private void  vote__wrappee__encryption  () {
		Vote encryptedVote = encryption(encMechanism,dni,vote);
		println(encryptedVote);
	}

	
	
	public void vote(){
		if (authenticated(authMechanism)) {
			println("User correctly authenticated...");
			vote__wrappee__encryption();
		}else {
			println("User Invalid...");
		}
	}

	
	
	 private Vote  encryption__wrappee__encryption  (String encMechanism, String dni, String vote) {
		return new Vote(dni,vote);
	}

	
	
	 private Vote  encryption__wrappee__DES  (String encMechanism, String dni, String vote) {
		if (encMechanism.equals("DES")) {
			return Encryption.DESEncryption(dni,vote);
		}
		return encryption__wrappee__encryption(encMechanism,dni,vote);
	}

	
	
	private Vote encryption(String encMechanism, String dni, String vote) {
		if (encMechanism.equals("AES")) {
			 return Encryption.AESEncryption(dni,vote);
		}
		return encryption__wrappee__DES(encMechanism,dni,vote);
	}

	
	
	 private boolean  authenticated__wrappee__authentication  (String authMechanism) {
		return false;
	}

	
	
	 private boolean  authenticated__wrappee__votingKey  (String authMechanism) {
		if (authMechanism.equals("votingKey")) {
			return Authentication.votingKeyAuthentication();
		}
		return authenticated__wrappee__authentication(authMechanism);
	}

	
	
	 private boolean  authenticated__wrappee__digitalCertificate  (String authMechanism) {
		if (authMechanism.equals("digitalCertificate")) {
			return Authentication.digitalCertificateAuthentication();
		}
		return authenticated__wrappee__votingKey(authMechanism);
	}

	
	
	private boolean authenticated(String authMechanism) {
		if (authMechanism.equals("fingerPrint")) {
			return Authentication.fingerPrintAuthentication();
		}
		return authenticated__wrappee__digitalCertificate(authMechanism);
	}


}
