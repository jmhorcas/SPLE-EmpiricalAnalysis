package encryption;

import java.security.Key;
import java.util.Base64;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

import org.bouncycastle.crypto.BlockCipher;
import org.bouncycastle.crypto.BufferedBlockCipher;
import org.bouncycastle.crypto.CryptoException;
import org.bouncycastle.crypto.engines.BlowfishEngine;
import org.bouncycastle.crypto.paddings.PaddedBufferedBlockCipher;
import org.bouncycastle.crypto.params.KeyParameter;

public class Blowfish_BouncyCastle {
	// mode CBC and padding PKCS5Padding by default.
	private static final String ALGO = "Blowfish";
    private static final byte[] keyValue = new byte[] { 'T', 'h', 'e', 'B', 'e', 's', 't', 'S', 'e', 'c', 'r','e', 't', 'K', 'e', 'y' };
    private static Cipher c;
    
    public Blowfish_BouncyCastle() throws Exception {
    	 //Key key = generateKey();
         //c = Cipher.getInstance(ALGO);
         //c.init(Cipher.ENCRYPT_MODE, key);
    }    
    
    public String encrypt(String Data) throws Exception {
    	/*
    	 * This will use a supplied key, and encrypt the data
    	 * This is the equivalent of DES/CBC/PKCS5Padding
    	 */
    	BlockCipher engine = new BlowfishEngine();
    	BufferedBlockCipher cipher = new PaddedBufferedBlockCipher(engine);

    	byte[] input = Data.getBytes();

    	Key key = generateKey();
    	cipher.init(true, new KeyParameter(keyValue));

    	byte[] cipherText = new byte[cipher.getOutputSize(input.length)];
    	
    	int outputLen = cipher.processBytes(input, 0, input.length, cipherText, 0);
    	try
    	{
    		cipher.doFinal(cipherText, outputLen);
    	}
    	catch (CryptoException ce)
    	{
    		System.err.println(ce);
    		System.exit(1);
    	}
    	return Base64.getEncoder().encodeToString(cipherText);
		//return new String(cipherText);
    }

    public String decrypt(String encryptedData) throws Exception {
       /* Key key = generateKey();
        Cipher c = Cipher.getInstance(ALGO);
        c.init(Cipher.DECRYPT_MODE, key);*/
        byte[] decordedValue = Base64.getDecoder().decode(encryptedData);
        byte[] decValue = c.doFinal(decordedValue);
        String decryptedValue = new String(decValue);
        return decryptedValue;
    }
    private Key generateKey() throws Exception {
        Key key = new SecretKeySpec(keyValue, ALGO);
        return key;
}

}
