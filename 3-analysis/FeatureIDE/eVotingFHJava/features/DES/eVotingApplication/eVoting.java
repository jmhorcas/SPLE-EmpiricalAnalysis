package eVotingApplication;

public class eVoting{
	
	private Vote encryption(String encMechanism, String dni, String vote) {
		if (encMechanism.equals("DES")) {
			return Encryption.DESEncryption(dni,vote);
		}
		return original(encMechanism,dni,vote);
	}
	
}
