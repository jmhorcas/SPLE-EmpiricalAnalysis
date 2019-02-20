package eVotingApplication;

public class Authentication{
	
	private static void println(Object obj) {
		System.out.println(obj);
	}
	
	private static boolean authentication() {
		boolean authenticated;
		
		int auth =  new java.util.Random().nextInt(2);
		if (auth == 1) {
			authenticated = true;
		}else {
			authenticated = false;
		}
		return authenticated;
	}
}
