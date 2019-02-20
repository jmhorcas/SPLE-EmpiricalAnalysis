package eVotingApplication;

public class eVoting{
	
	private boolean authenticated(String authMechanism) {
		if (authMechanism.equals("fingerPrint")) {
			return Authentication.fingerPrintAuthentication();
		}
		return original(authMechanism);
	}
	
}
