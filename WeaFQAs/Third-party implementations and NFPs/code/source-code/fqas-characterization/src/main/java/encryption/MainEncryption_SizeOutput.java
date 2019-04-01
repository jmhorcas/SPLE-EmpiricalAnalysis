package encryption;

import java.math.BigInteger;

import utils.MyUtils;

public class MainEncryption_SizeOutput { 
	
	public static void main(String[] args) throws Exception {
		//BigInteger size = new BigInteger(args[0]);
		//String msg = MyUtils.getStringOfSize(size);
		String msg = "mypassword";
		// j9slj2w2Fg+RyCERvRRjpg==
		
		AES encryption = new AES();
		String encryptedText = encryption.encrypt(msg);
		
		System.out.println("Input size: " + msg.getBytes().length);
		System.out.println("Output size: " + encryptedText.getBytes().length);
		///System.out.println("Plain Text : " + msg);
		//System.out.println("Encrypted Text : " + encryptedText);
		//System.out.println("Decrypted Text : " + msg);
	}
}

