package eVotingApplication; 

public  class  eVoting {
	
	private String dni;

	
	private String vote;

	
	private String authMechanism;

	
	private String encMechanism;

	

   public eVoting(String dni, String vote, String authMechanism, String encMechanism) {
		this.dni = dni;
		this.vote = vote;
		this.authMechanism = authMechanism;
		this.encMechanism = encMechanism;
	}

	
	
	public void println(Object obj) {
		System.out.println(obj);
	}

	
	
	public String getAuthMechanism() {
		return authMechanism;
	}

	
	
	public String getEncMechanism() {
		return encMechanism;
	}

	
	
	public String getDni() {
		return dni;
	}

	
	
	public String getVote() {
		return vote;
	}

	
	
	public void vote() {
		Vote v = new Vote(dni,vote);
		println(v);
	}


}
