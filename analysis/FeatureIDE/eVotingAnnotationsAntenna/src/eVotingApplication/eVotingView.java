package eVotingApplication;

import java.awt.*;
import java.awt.event.ActionListener;

import javax.swing.*;

@SuppressWarnings("serial")
public class eVotingView extends JPanel implements eVotingInterface{
	JComboBox<String> authOptions;
	JComboBox<String> encOptions;
	JComboBox<String> voteOptions;
	JTextArea textArea;
	JButton voteB;
	
	public eVotingView() {
		this.setLayout(new BorderLayout());
		
		// #if votingMachine
//@		add(new JLabel("Wellcome to the Online Voting System through a Voting Machine     "),BorderLayout.NORTH);
		// #endif
		// #if mobileDevice
//@		add(new JLabel("Wellcome to the Online Voting System through your mobile Device     "),BorderLayout.NORTH);
		// #endif
		// #if desktopComputer
		add(new JLabel("Wellcome to the Online Voting System through your desktop Computer     "),BorderLayout.NORTH);
		// #endif
		
		JPanel authentication = new JPanel();
		authentication.setLayout(new BorderLayout());
		authOptions= new JComboBox<>();
		// #if fingerPrint
//@		authOptions.addItem("fingerPrint");
		// #endif
		// #if votingKey
		authOptions.addItem("votingKey");
		// #endif
		// #if digitalCertificate
		authOptions.addItem("digitalCertificate");
		// #endif
		authentication.add(new JLabel("Select Authentication Mechanism:  "),BorderLayout.WEST);	
		authentication.add(authOptions,BorderLayout.CENTER);
		add(authentication,BorderLayout.WEST);
		
		JPanel encryption = new JPanel();
		encryption.setLayout(new BorderLayout());
		encOptions= new JComboBox<>();
		// #if AES
		encOptions.addItem("AES");
		// #endif
		// #if RSA
		encOptions.addItem("RSA");
		// #endif
		// #if DES
		encOptions.addItem("DES");
		// #endif
		encryption.add(new JLabel("Select Encryption Mechanism:  "),BorderLayout.WEST);	
		encryption.add(encOptions,BorderLayout.CENTER);
		add(encryption,BorderLayout.CENTER);
		
		JPanel vote = new JPanel();
		vote.setLayout(new BorderLayout());
		JPanel id = new JPanel();
		id.setLayout(new BorderLayout());
		id.add(new JLabel("Introduce your id: "),BorderLayout.WEST);
		textArea = new JTextArea(2,20);
		textArea.setText("");
		id.add(textArea,BorderLayout.CENTER);
		vote.add(id,BorderLayout.NORTH);
		vote.add(new JLabel("Introduce your selection:   "),BorderLayout.WEST);
		voteOptions= new JComboBox<>();
		voteOptions.addItem("Option1");
		voteOptions.addItem("Option2");
		voteOptions.addItem("Option3");
		vote.add(voteOptions,BorderLayout.CENTER);
		voteB = new JButton("Vote");
		vote.add(voteB,BorderLayout.EAST);
		add(vote,BorderLayout.SOUTH);
	}
	
	public String getId() {
		return textArea.getText();
	}
	
	public void setErrorId() {
		textArea.setText("ERROR. You must introduce your id");
	}
	
	public String getAuthenticationMechanism() {
		return (String) authOptions.getSelectedItem();
	}
	
	public String getEncryptionMechanism() {
		return (String) encOptions.getSelectedItem();
	}
	
	public String getVote() {
		return (String) voteOptions.getSelectedItem();
	}
	
	public void addController(ActionListener ctr) {
		voteB.addActionListener(ctr);
		voteB.setActionCommand(eVotingInterface.VOTING);
	}
	
}
