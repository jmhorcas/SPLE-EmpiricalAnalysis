package eVotingApplication;

public class eVoting{
	
	private boolean authenticated(String authMechanism) {
		if (authMechanism.equals("digitalCertificate")) {
			return Authentication.digitalCertificateAuthentication();
		}
		return original(authMechanism);
	}
	
}
