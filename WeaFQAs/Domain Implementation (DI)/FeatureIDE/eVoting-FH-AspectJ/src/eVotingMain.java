import eVotingApplication.*; 

import javax.swing.JFrame; 

public  class  eVotingMain {
	
	
	public static void main(String[] args) {
		eVotingView view = new eVotingView();
		eVotingController controller = new eVotingController(view);
		view.addController(controller);
		
		JFrame frame = new JFrame("eVoting Application");
		
		frame.setContentPane(view);
		frame.pack();
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
	}


}
