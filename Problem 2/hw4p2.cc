// Derek Black - ME 701
// Problem 2 - Monte Carlo Methods & Midpoint for Integration

// Actual answers for the integrals were computed with WolfRamAlpha

#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


int main(int argc, char *argv[])
{
    // Prompt user for n and m
	int n;
	int m;
	n = atol(argv[1]);
	m = atol(argv[2]);
	double size;
	double actual;
	double relative;
	double absolute;
	//cout << "Enter # of dimensions n (n <= 10):";
	//cin >> n;
	//cout << "Enter # of divisions m :";
	//cin >> m;


	// End user input


	size = pow(m,n);
	cout << "# of evaluations:" << endl;
	cout << size << endl;


	vector<double> x1(size);
	vector<double> x2(size);
	vector<double> x3(size);
	vector<double> x4(size);
	vector<double> x5(size);
	vector<double> x6(size);
	vector<double> x7(size);
	vector<double> x8(size);
	vector<double> x9(size);
	vector<double> x10(size);

	vector<double> a(size);
	double bin = 0;
	double I=0;
	fstream file;
	file.open("output.txt",std::ios::out);

	// Generate vectors of random values for xi
	for (int i = 0; i<size; ++i)
	{
		x1[i] = (double)rand()/(double)RAND_MAX;
		x2[i] = (double)rand()/(double)RAND_MAX;
		x3[i] = (double)rand()/(double)RAND_MAX;
		x4[i] = (double)rand()/(double)RAND_MAX;
		x5[i] = (double)rand()/(double)RAND_MAX;
		x6[i] = (double)rand()/(double)RAND_MAX;
		x7[i] = (double)rand()/(double)RAND_MAX;
		x8[i] = (double)rand()/(double)RAND_MAX;
		x9[i] = (double)rand()/(double)RAND_MAX;
		x10[i] = (double)rand()/(double)RAND_MAX;
	}

	// Generate vectors of random values for ai
	for (double i = 0; i<size; ++i)
	{
		a[i] = (double)rand()/(double)RAND_MAX;
	}

	// Monte Carlo Quadrature
	if (n == 1)
	{
		for (double i = 0; i < size; ++i)
		{
			if (a[i] < sqrt(x1[i]))
			{
				bin = bin + 1;

			}

		}
		//actual = 0.66667;
	}
	else if (n == 2)
	{
		for (double i = 0; i < size; ++i)
		{
			if (a[i] < sqrt(x1[i]*x2[i]))
			{
				bin = bin + 1;
				//I = I + sqrt(x1[i]*x2[i]);
			}
		}
		//actual = 0.444444;
	}
	else if (n == 3)
	{
		for (double i = 0; i < size; ++i)
		{
			if (a[i] < sqrt(x1[i]*x2[i]*x3[i]))
			{
				bin = bin + 1;
				//I = I + sqrt(x1[i]*x2[i]*x3[i]);
			}
		}
		//actual = 0.296296;
	}
	else if (n == 4)
	{
		for (double i = 0; i < size; ++i)
		{
			if (a[i] < sqrt(x1[i]*x2[i]*x3[i]*x4[i]))
			{
				bin = bin + 1;
				//I = I + sqrt(x1[i]*x2[i]*x3[i]);
			}
		}
		//actual = 0.197531;
	}
	else if (n == 5)
	{
		for (double i = 0; i < size; ++i)
		{
			if (a[i] < sqrt(x1[i]*x2[i]*x3[i]*x4[i]*x5[i]))
			{
				bin = bin + 1;
				//I = I + sqrt(x1[i]*x2[i]*x3[i]);
			}
		}
		//actual = 0;
	}
	else if (n == 6)
	{
		for (double i = 0; i < size; ++i)
		{
			if (a[i] < sqrt(x1[i]*x2[i]*x3[i]*x4[i]*x5[i]*x6[i]))
			{
				bin = bin + 1;
				//I = I + sqrt(x1[i]*x2[i]*x3[i]);
			}
		}
		//actual = 0.105399;
	}
	else if (n == 7)
	{
		for (double i = 0; i < size; ++i)
		{
			if (a[i] < sqrt(x1[i]*x2[i]*x3[i]*x4[i]*x5[i]*x6[i]*x7[i]))
			{
				bin = bin + 1;
				//I = I + sqrt(x1[i]*x2[i]*x3[i]);
			}
		}
		//actual = 0.07244;
	}
	else if (n == 8)
	{
		for (double i = 0; i < size; ++i)
		{
			if (a[i] < sqrt(x1[i]*x2[i]*x3[i]*x4[i]*x5[i]*x6[i]*x7[i]*x8[i]))
			{
				bin = bin + 1;
				//I = I + sqrt(x1[i]*x2[i]*x3[i]);
			}
		}
		//actual = 0.049787;
	}
	else if (n == 9)
	{
		for (double i = 0; i < size; ++i)
		{
			if (a[i] < sqrt(x1[i]*x2[i]*x3[i]*x4[i]*x5[i]*x6[i]*x7[i]*x8[i]*x9[i]))
			{
				bin = bin + 1;
				//I = I + sqrt(x1[i]*x2[i]*x3[i]);
			}
		}
		//actual = 0.034218;
	}
	else if (n == 10)
	{
		for (double i = 0; i < size; ++i)
		{
			if (a[i] < sqrt(x1[i]*x2[i]*x3[i]*x4[i]*x5[i]*x6[i]*x7[i]*x8[i]*x9[i]*x10[i]))
			{
				bin = bin + 1;
				//I = I + sqrt(x1[i]*x2[i]*x3[i]);
			}
		}
		//actual = 0.023518;
	}
	else
	{
		cout << "# of dimensions exceeds 10" << endl;
	}

	// End of Monte Carlo Method

	actual = pow(0.66666666666,n);
	double answer;
	double rejected;
	rejected = size - bin;
	answer = bin/(bin+rejected);
	absolute = abs(actual-answer);
	relative = abs(absolute/actual);


	cout << "bin count:" << endl;
	cout << bin << endl;

	cout << "answer:" << endl;
	cout << answer << endl;

	cout << "Actual Answer = " << endl;
	cout << actual << endl;

	cout << "Absolute Error = " << endl;
	cout << absolute << endl;

	cout << "Relative Error = " << endl;
	cout << relative << endl;

	// End Monte Carlo Quadrature

	file << actual << " " << answer;
	file.close();
	return 0;
}



