//============================================================================
// Name        : hw04p2.cpp
// Author      : Li Lun
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================


#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <cstdlib>
using namespace std;

int main()
{

	ofstream volume_stream("output.txt", ios::app);
	int m, n;
	cout <<"m=";
	cin >> m;
	cout <<endl;
	cout <<"n=";
	cin >> n;
	int i,j;
	double I_mp=1, I_mc,I;
	I=pow(2.0/3.0,n);
	double value;
	for(i=0;i<n;i++)
	{
		value=0;
		for(j=0;j<m;j++)
		{
			double k= double(m);
			value = value+sqrt(1/k*j+1/(2*k))*(1/k);
		}
		I_mp=I_mp*value;
//		volume_stream << value << "\t"<<I_middle_point << endl;
	}

	double count=0;
	srand(time(NULL));
	for(i=0;i<m;i++)
	{
		//srand(time(NULL));
		double a=rand()%10000;
		double aa=a/10000;
		double f=1;
		for(j=0;j<n;j++)
		{
			//srand(time(NULL));
			double x =rand()%10000;
			double xx=x/10000;
			//volume_stream <<aa<< xx << endl;
			f=f*sqrt(xx);
		}
		if(aa<=f)
		{
			count++;
		}
		//count=count+f;
		//cout << count << endl;
		//cout << i << endl;
	}
	I_mc=double(count)/double(m);
	volume_stream << I <<"\t"<<I_mp<<"\t"<< I_mc << endl;


}
