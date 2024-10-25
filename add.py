// C++ implementation of the above approach
#include<bits/stdc++.h>
using namespace std;

// Function to print sum of 2 numbers
// without propagating carry
int printSum(int a, int b)
{
	int res = 0;
	
	int temp1 = 0, temp2 = 0;
	
	// Reverse a
	while(a)
	{
	temp1 = temp1*10 + (a%10);
	a /= 10;
	}
	a = temp1;
	
	// Reverse b
	while(b)
	{
	temp2 = temp2*10 + (b%10);
	b /= 10;
	}
	b = temp2;
	
	// Generate sum
	// Since length of both a and b are same,
	// take any one of them.
	while(a)
	{ 
		// Extract digits from a and b and add
		int sum = (a%10 + b%10);
		
		// If sum is single digit
		if(sum/10 == 0) 
			res = res*10 + sum;
		else
		{
			// If sum is not single digit
			// reverse sum
			temp1 = 0;
			while(sum)
			{
				temp1 = temp1*10 + (sum%10);
				sum /= 10;
			}
			sum = temp1;
			
			// Extract digits from sum and append
			// to result
			while(sum)
			{
				res = res*10 + (sum%10);
				sum /=10;
			}
		}
		
		a/=10;
		b/=10;
	}
	
	return res;
}

// Driver code
int main()
{
	int a = 7752, b = 8834;
	cout<<printSum(a, b);
	
	return 0;
}
