package project5;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.MessageDigest;
import java.util.Arrays;

public class P5
{
	public static void main(String[] args)
	{
		P5 project = new P5();
		project.findBytes();
	}
	/*
	 * This method finds the first two bytes of the SHA-256 hash 
	 * that will match any correct password for CodeBreaker2013.exe
	 * We are given an AES-128 key, the ciphertext, and the constant
	 * HMAC hash 
	 */
	public void findBytes()
	{
		byte[] key = { (byte) 0x23, (byte) 0x8E, (byte) 0x60, (byte) 0x0E1, (byte) 0x0D2, (byte) 0x96, (byte) 0x38,
				(byte) 0x0C7, (byte) 0x0A5, (byte) 0x0C0, (byte) 0x22, (byte) 0x74, (byte) 0x4F, (byte) 0x31,
				(byte) 0x5B, (byte) 0x0Cd};

		byte[] constantMac = { (byte) 0xbc, (byte) 0xb0, (byte) 0x78, (byte) 0x41, (byte) 0xaa, (byte) 0xd0, (byte) 0x06,
				(byte) 0x68, (byte) 0xdd, (byte) 0xa4, (byte) 0x74, (byte) 0x06, (byte) 0xd7, (byte) 0x1a, (byte) 0x2b,
				(byte) 0xd2, (byte) 0x9b, (byte) 0x0e, (byte) 0xdb, (byte) 0x0d, (byte) 0xf9, (byte) 0xce, (byte) 0xf4,
				(byte) 0xa7, (byte) 0xf9, (byte) 0x51, (byte) 0x6c, (byte) 0x99, (byte) 0xfc, (byte) 0xb6, (byte) 0x95,
				(byte) 0xf8};

		byte[] embeddedCiphertext = { (byte) 0x34, (byte) 0x3b, (byte) 0x71, (byte) 0x62, (byte) 0xba, (byte) 0x9f,
				(byte) 0x55, (byte) 0xb8, (byte) 0xd9, (byte) 0x88, (byte) 0x71, (byte) 0x98, (byte) 0x24, (byte) 0x41,
				(byte) 0x3e, (byte) 0x4d, (byte) 0xa4, (byte) 0xbd, (byte) 0x1a, (byte) 0xe1, (byte) 0x2c, (byte) 0xae,
				(byte) 0x2c, (byte) 0xff, (byte) 0x1d, (byte) 0x4e, (byte) 0x1a, (byte) 0x9e, (byte) 0x94, (byte) 0x8a,
				(byte) 0x4d, (byte) 0x07, (byte) 0x71, (byte) 0x5d, (byte) 0xc6, (byte) 0x1f, (byte) 0xef, (byte) 0x91,
				(byte) 0x09, (byte) 0x67, (byte) 0xda, (byte) 0xfa, (byte) 0x37, (byte) 0x96, (byte) 0x11, (byte) 0xe1,
				(byte) 0x67, (byte) 0xd6, (byte) 0x3e, (byte) 0xa1, (byte) 0x5e, (byte) 0x58, (byte) 0x0b, (byte) 0x81,
				(byte) 0xdd, (byte) 0xb2, (byte) 0xaf, (byte) 0x5d, (byte) 0xde, (byte) 0xde, (byte) 0x9d, (byte) 0x82,
				(byte) 0xb3, (byte) 0x72, (byte) 0x36, (byte) 0x86, (byte) 0xa6, (byte) 0x72, (byte) 0xea, (byte) 0x3e,
				(byte) 0x5a, (byte) 0xa0, (byte) 0x21, (byte) 0x4e, (byte) 0x94, (byte) 0xbf, (byte) 0x51, (byte) 0x12,
				(byte) 0xbe, (byte) 0xfc, (byte) 0xb6, (byte) 0x07, (byte) 0x3d, (byte) 0x51, (byte) 0x36, (byte) 0xcf,
				(byte) 0x76, (byte) 0x93, (byte) 0xab, (byte) 0xc6, (byte) 0x6c, (byte) 0x7b, (byte) 0x5f, (byte) 0xc8,
				(byte) 0x16, (byte) 0xa2, (byte) 0x11, (byte) 0xc0, (byte) 0xe6, (byte) 0x87, (byte) 0x9e, (byte) 0xab,
				(byte) 0x40, (byte) 0x56, (byte) 0xa4, (byte) 0xb7, (byte) 0xa5, (byte) 0x20, (byte) 0x44, (byte) 0xbf,
				(byte) 0xb0, (byte) 0xb7, (byte) 0x5b, (byte) 0x43, (byte) 0x4a, (byte) 0x02, (byte) 0x19, (byte) 0x09,
				(byte) 0x1d, (byte) 0xb2, (byte) 0x30, (byte) 0xbb, (byte) 0x15, (byte) 0xce, (byte) 0x1c, (byte) 0x97,
				(byte) 0xd8, (byte) 0x77, (byte) 0xbc, (byte) 0x42, (byte) 0x87, (byte) 0x14, (byte) 0x93, (byte) 0x85,
				(byte) 0xd2, (byte) 0x0a, (byte) 0x7d, (byte) 0xc4, (byte) 0x44, (byte) 0x0e, (byte) 0x82, (byte) 0x35,
				(byte) 0x3b, (byte) 0xc4, (byte) 0x40, (byte) 0x78, (byte) 0x7a, (byte) 0x59, (byte) 0xa1, (byte) 0x59,
				(byte) 0x18, (byte) 0x09, (byte) 0x22, (byte) 0x17, (byte) 0x68, (byte) 0xc0, (byte) 0xfc, (byte) 0x7a,
				(byte) 0x5f, (byte) 0x67, (byte) 0x5b, (byte) 0x2a, (byte) 0xb3, (byte) 0xfc, (byte) 0x53, (byte) 0xbc,
				(byte) 0xe0, (byte) 0x92, (byte) 0xff, (byte) 0x0d, (byte) 0x84, (byte) 0x74, (byte) 0x31, (byte) 0x1f,
				(byte) 0xf5, (byte) 0x16, (byte) 0x4f, (byte) 0x17, (byte) 0x50, (byte) 0x8d, (byte) 0x95, (byte) 0x51,
				(byte) 0x06, (byte) 0xf7, (byte) 0xbc, (byte) 0xda, (byte) 0x15, (byte) 0x05, (byte) 0x76, (byte) 0xb5,
				(byte) 0x10, (byte) 0x78, (byte) 0xa4, (byte) 0xa1, (byte) 0xf1, (byte) 0x45, (byte) 0xf1, (byte) 0x6e,
				(byte) 0x78, (byte) 0x2c, (byte) 0x3a, (byte) 0x01, (byte) 0x4e, (byte) 0x82, (byte) 0x68, (byte) 0x4f,
				(byte) 0xe8, (byte) 0x12, (byte) 0x69, (byte) 0xdd, (byte) 0x00, (byte) 0x77, (byte) 0x17, (byte) 0xec,
				(byte) 0x95, (byte) 0x76, (byte) 0xbc, (byte) 0x8c, (byte) 0x43, (byte) 0xc5, (byte) 0x99, (byte) 0x53,
				(byte) 0xba, (byte) 0x86, (byte) 0x4c, (byte) 0x6b, (byte) 0x46, (byte) 0x4a, (byte) 0x35, (byte) 0x82,
				(byte) 0xe1, (byte) 0x10, (byte) 0xee, (byte) 0x2a, (byte) 0x73, (byte) 0x4d, (byte) 0x80, (byte) 0x55,
				(byte) 0xdc, (byte) 0xbc};
		try 
		{
			byte[] finalKey = new byte[16];// the key used to create the HMAC hash
			
			// the two bytes used to created the finalKey
			byte one;
			byte two;
			
			// trying all combinations of bytes one and two from 
			// 0-255 to create the finalKey
			for (int ii = 0; ii < 256; ii++)
			{
				one = (byte) ii;

				for (int jj = 0; jj < 256; jj++)
				{
					two = (byte) jj;
					
					finalKey[0] = (byte) (two^key[0]);
					finalKey[1] = (byte) (one^key[1]);
					finalKey[2] = (byte) (finalKey[1]^key[2]);
					finalKey[3] = (byte) (finalKey[0]^key[3]);
					finalKey[4] = (byte) (finalKey[3]^key[4]);
					finalKey[5] = (byte) (finalKey[2]^key[5]);
					finalKey[6] = (byte) (finalKey[5]^key[6]);
					finalKey[7] = (byte) (finalKey[4]^key[7]);
					finalKey[8] = (byte) (finalKey[7]^key[8]);
					finalKey[9] = (byte) (finalKey[6]^key[9]);
					finalKey[10] = (byte) (finalKey[9]^key[10]);
					finalKey[11] = (byte) (finalKey[8]^key[11]);
					finalKey[12] = (byte) (finalKey[11]^key[12]);
					finalKey[13] = (byte) (finalKey[10]^key[13]);
					finalKey[14] = (byte) (finalKey[13]^key[14]);
					finalKey[15] = (byte) (finalKey[12]^key[15]);

					/*
					 * Java code snippet for HMAC-SHA256: if you have a 128-bit
					 * key in a byte array key, you can use the following code
					 * to generate MAC value on byte array embeddedCiphertext.
					 */
					SecretKeySpec sks = new SecretKeySpec(finalKey, "AES"); // creating an AES-128 key out of the bytes in finalKey

					Mac mac = Mac.getInstance("HmacSHA256"); // crates Mac object to create a HMAC hash
					mac.init(sks); // initliaizes the mac object with the AES-128 key
					byte[] macValue = mac.doFinal(embeddedCiphertext); // creates the HMAC has for the ciphertext
					
					// if the HMAC hashes of the ciphertext and and the finalKey match
					// then the first two bytes have been found
					if (Arrays.equals(macValue, constantMac))
					{
						System.out.println("WE FOUND A MATCH!");						
						byte[] twoBytes = {(byte) one, (byte) two}; // created a byte array for the two bytes for printing purposes
						System.out.println("The first two bytes of the SHA-256 hash are: " + Arrays.toString(twoBytes));
					}
				}
			}
		} 
		catch (Exception e)
		{
			System.out.println("Exception.");
		}
	}
}
		