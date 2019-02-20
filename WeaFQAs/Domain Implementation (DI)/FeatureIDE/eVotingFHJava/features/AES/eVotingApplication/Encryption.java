package eVotingApplication;

public class Encryption {
	public static Vote AESEncryption(String dni, String vote) {
		return new Vote(dni,"AESEncrypted");
	}
}