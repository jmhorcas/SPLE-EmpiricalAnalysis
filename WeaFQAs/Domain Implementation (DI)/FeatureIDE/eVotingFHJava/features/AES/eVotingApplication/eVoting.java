package eVotingApplication;

public class eVoting{
	
	private Vote encryption(String encMechanism, String dni, String vote) {
		if (encMechanism.equals("AES")) {
			 return Encryption.AESEncryption(dni,vote);
		}
		return original(encMechanism,dni,vote);
	}
	
}
