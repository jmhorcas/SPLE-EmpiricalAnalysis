package eVotingApplication;

public class eVoting{
	
	private boolean authenticated(String authMechanism) {
		return false;
	}
	
	public void vote(){
		if (authenticated(authMechanism)) {
			println("User correctly authenticated...");
			original();
		}else {
			println("User Invalid...");
		}
	}
}
