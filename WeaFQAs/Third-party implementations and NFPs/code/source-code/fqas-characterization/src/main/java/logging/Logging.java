package logging;

import java.math.BigInteger;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import utils.MyUtils;

public class Logging {
	private static final Logger logger = LoggerFactory.getLogger(Logging.class);
	
	public static void main(String[] args) {
		BigInteger size = new BigInteger(args[0]);
		//BigInteger size = new BigInteger("10");
		String msg = MyUtils.getStringOfSize(size);
		
		logger.info(msg);
	}
}
