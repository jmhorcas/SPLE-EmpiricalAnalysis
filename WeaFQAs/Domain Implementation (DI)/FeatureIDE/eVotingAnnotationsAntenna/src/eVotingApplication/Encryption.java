package eVotingApplication;

public class Encryption {
	//if #AES
	public static Vote AESEncryption(String dni, String vote) {
		return new Vote(dni,"AESEncrypted");
	}
	//endif
	
	//if #RSA
	public static Vote RSAEncryption(String dni, String vote) {
		return new Vote(dni,"RSAEncrypted");
	}
	//endif
	
	//if #DES
	public static Vote DESEncryption(String dni, String vote) {
		return new Vote(dni,"DESEncrypted");
	}
	//endif
}