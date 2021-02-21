package eVotingApplication;

public aspect Encryption {
	
	void around(eVoting eV): target(eV) && execution(void eVoting.vote()){
		String encM = eV.getEncMechanism();
		String dni = eV.getDni();
		String vote = eV.getVote();
		Vote encryptedVote = encryption(encM, dni, vote);
		eV.println(encryptedVote);
	}
	
	private Vote encryption(String encMechanism, String dni, String vote) {
		Vote v;
		if (encMechanism.equals("RSA")) {
			v = RSAEncryption(dni,vote);
		}else if (encMechanism.equals("DES")) {
			v = DESEncryption(dni,vote);
		}else {
			v = AESEncryption(dni,vote);
		}
		return v;
	}
	
	private Vote DESEncryption(String dni, String vote) {
		return new Vote(dni,"DESEncrypted");
	}

	private Vote RSAEncryption(String dni, String vote) {
		return new Vote(dni,"RSAEncrypted");
	}
	
	private Vote AESEncryption(String dni, String vote) {
		return new Vote(dni,"AESEncrypted");
	}
}
