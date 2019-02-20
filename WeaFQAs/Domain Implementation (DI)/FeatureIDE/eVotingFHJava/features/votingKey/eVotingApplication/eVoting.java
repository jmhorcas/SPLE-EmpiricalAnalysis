package eVotingApplication;

public class eVoting{
	
	private boolean authenticated(String authMechanism) {
		if (authMechanism.equals("votingKey")) {
			return Authentication.votingKeyAuthentication();
		}
		return original(authMechanism);
	}
	
}
