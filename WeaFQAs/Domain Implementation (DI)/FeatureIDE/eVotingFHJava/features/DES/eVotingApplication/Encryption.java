package eVotingApplication;

public class Encryption {
	public static Vote DESEncryption(String dni, String vote) {
		return new Vote(dni,"DESEncrypted");
	}
}