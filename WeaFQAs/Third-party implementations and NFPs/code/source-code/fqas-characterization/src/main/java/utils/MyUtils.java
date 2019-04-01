package utils;

import java.math.BigInteger;

public class MyUtils {

	public static String getStringOfSize(BigInteger bytes) {
		StringBuilder sb = new StringBuilder();
		for (BigInteger i = BigInteger.ONE; i.compareTo(bytes) <= 0; i = i.add(BigInteger.ONE)) {
			sb.append('a');	// 1 byte
		}
		return sb.toString();
	}
}
