package eVotingApplication;

public class eVoting{
	
	private Vote encryption(String encMechanism, String dni, String vote) {
		return new Vote(dni,vote);
	}
	
	public void vote() {
		Vote encryptedVote = encryption(encMechanism,dni,vote);
		println(encryptedVote);
	}
}
