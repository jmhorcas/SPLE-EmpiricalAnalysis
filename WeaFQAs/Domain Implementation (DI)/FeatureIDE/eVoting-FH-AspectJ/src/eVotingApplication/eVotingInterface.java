package eVotingApplication; 

import java.awt.event.ActionListener; 

public  interface  eVotingInterface {
	
	
	public final String VOTING = "VOTING";

	
	
	public String getId();

	
	public void setErrorId();

	
	public String getAuthenticationMechanism();

	
	public String getEncryptionMechanism();

	
	public String getVote();

	
	public void addController(ActionListener ctr);


}
