package encapsulation;

public class Test {
	
	public static void main(String[] args) 
	{
		myBankAccount m = new myBankAccount();
		m.setBalance(70000);
		System.out.println(m.getBalance());
	}

}
