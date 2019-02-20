package eVotingApplication; 

import java.awt.event.*; 

public  class  eVotingController  implements ActionListener {
	
	private eVotingInterface view;

	
	
   public eVotingController(eVotingInterface view) {
		this.view = view;
	}

	
	
	public void actionPerformed(ActionEvent e) {
		try {
			if (e.getActionCommand().equals(eVotingInterface.VOTING)) {
				String id = view.getId();
				if (id.equals("")) {
					view.setErrorId();
				}else {
					String vote = view.getVote();
					String authMethod = view.getAuthenticationMechanism();
					String encMethod = view.getEncryptionMechanism();
					eVoting model = new eVoting(id,vote,authMethod,encMethod);
					model.vote();					
				}
			}
		}catch(Exception ex) {
			System.err.println("ERROR: " + ex.getMessage());
		}
	}


}
