package eVotingApplication;

public aspect Authentication {
	
	declare precedence: Authentication, Encryption;

	void around(eVoting eV): target(eV) && execution(void eVoting.vote()){
		String authM = eV.getAuthMechanism();
		if (authenticated(authM)) {
			proceed(eV);
		}else {
			eV.println("Invalid User...");
		}
		
	}
	
	private boolean authenticated(String authMechanism) {
		boolean auth = false;
		if (authMechanism.equals("digitalCertificate")) {
			auth = digitalCertificateAuthentication();
		}else if (authMechanism.equals("fingerPrint")) {
			auth = fingerPrintAuthentication();
		}else if (authMechanism.equals("votingKey")){
			auth = votingKeyAuthentication();
		}
		return auth;
	}
	
	public boolean fingerPrintAuthentication() {
		println("Finger Print Authentication ... ");
		return authentication();
	}
	
	public boolean digitalCertificateAuthentication() {
		println("Digital Certificate Authentication ... ");
		return authentication();
	}
	
	public boolean votingKeyAuthentication() {
		println("Voting Key Authentication ... ");
		return authentication();
	}
	
	private void println(Object obj) {
		System.out.println(obj);
	}
	
	private boolean authentication() {
		boolean authenticated;
		
		int auth =  new java.util.Random().nextInt(2);
		if (auth == 1) {
			authenticated = true;
		}else {
			authenticated = false;
		}
		return authenticated;
	}
}
