package eVotingApplication;

public class Encryption {
	
	public static Vote RSAEncryption(String dni, String vote) {
		return new Vote(dni,"RSAEncrypted");
	}
	
}