package project5;

import java.security.MessageDigest;
import java.util.Random;
/*
 * Class designated to finding the password for Project5
 * after the first two bytes of the correct SHA-256 hash
 * have been found
 */
public class FindPassword
{
	
	public static void main(String args[])
	{
		boolean correct = false;
		while(!correct)
		{
			String temp = randomPassword("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", 8);
			correct = findPassword(temp);
			
			if(correct)
			{
				System.out.println("The password is: " + temp);
			}
		}
	}
	/*
	 * This method returns true if the first
	 * two bytes of the SHA-256 hash of the given
	 * password matches 18 and 2
	 * Takes a String temp which is the trial password
	 * Returns a boolean correct which is true if the 
	 * password given is correct
	 */
	public static boolean findPassword(String temp)
	{
		String tempPassword = temp;
		boolean correct = false;
		
		try
		{
			MessageDigest mDigest = MessageDigest.getInstance("SHA-256"); // creates a SHA-256 message instance
			byte [] result = mDigest.digest(tempPassword.getBytes()); // creates a SHA-256 hash from the given password
			
			if(result[0] == 18 && result[1] == 2) // if the first two bytes match 18 and 2 then the password is correct
			{
				correct = true;
			}
				 
		}
		catch(Exception e)
		{
			
		}
		
		return correct;
	}
	/*
	 * This method generates a random string based on a regular
	 * expression of characters and string length
	 * Takes a String candidateChars that designates what characters to choose from
	 * Takes an Integer length that designates how long the string will be
	 * Returns the randomly generated string
	 */
	public static String randomPassword(String candidateChars, int length)
	{
	    StringBuilder sb = new StringBuilder(); // creates a String builder object
	    Random random = new Random();
	    for (int i = 0; i < length; i++)
	    {
	        sb.append(candidateChars.charAt(random.nextInt(candidateChars
	                .length()))); // builds the string of the randomly generated characters
	    }
	    
	    return sb.toString();
	}
}
