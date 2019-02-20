package eVotingApplication;

public class eVoting{
	
	private Vote encryption(String encMechanism, String dni, String vote) {
		if (encMechanism.equals("RSA")) {
			return Encryption.RSAEncryption(dni,vote);
		}
		return original(encMechanism,dni,vote);
	}
	
}
