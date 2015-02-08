#include "stdio.h"

main()
{
	char * str1 = "6053e1cc67935bc63cfc5c48ee37e2f58de7eaa85324de148cd87c501dc1a8d9";
	char * str2 = "f44da30ff36a2b5c056900c39b280b850752293ccf4cb84c2a4bf8916c047830";
	int n,m;
	int j = 0;
	unsigned int count = 0;
	for(j = 0; j < 64; j++)
	{
		n = str1[j];
		m = str2[j];
		int i=0;
		for(i=0; i<8; i++)
		{
			if( (n&1) != (m&1) ) 
			{
			    count++;
			}
			n >>= 1;
			m >>= 1;
		}
	}
	printf("Hamming dist:%u\n", count);
}