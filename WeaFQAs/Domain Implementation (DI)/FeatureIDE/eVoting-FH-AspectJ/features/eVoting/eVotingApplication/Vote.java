package eVotingApplication;

class Vote{
	private String dni;
	private String vote;
	
	public Vote(String dni, String vote) {
		this.dni = dni;
		this.vote = vote;
	}
	
	public String toString() {
		return "(" + dni+","+ vote+")";
	}
}