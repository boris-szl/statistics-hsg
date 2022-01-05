#include <cmath>
#include <cstdlib>
#include <cassert>
#include <iostream>




using std::cin;
using std::cout;
using std::endl;


int binomial(int n,int k) {
	assert(k >= 0);
	assert(n >= k);
	int nominator = 1;
	int denominator = 1;
	for (int i=0;i<k;i++) {
		nominator *= n - i;
		denominator *= k - i;
	}
	return nominator / denominator;
}

double probability(int n, int N) {
	return n / N;
}

double binDistribution(int n, int k, double mu) {
	return binomial(n,k)*pow(mu,n)*pow((1-mu),(n-k));
}

int main() {

	int N;
	int n, k;
	double mu;
	cout<<"Choose n and k"<<endl;
	cin>>n>>k;
	mu = probability(1,9);
	cout<<binomial(n,k)<<endl;
	cout<<binDistribution(n,k,mu)<<endl;


	return 0;
}