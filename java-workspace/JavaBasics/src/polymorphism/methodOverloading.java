package polymorphism;

public class methodOverloading 
{
	
	static void add(int a, int b)
	{
		int c = a + b;
		System.out.println("C = " + c);
	}
	
	static void add(int a, int b, int c)
	{
		int d = a + b + c;
		System.out.println("D = " + d);
	}
	
	static void add(int a, float b)
	{
		float c = a * b;
		System.out.println("C = " + c);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		add(2,3,9);

	}

}
