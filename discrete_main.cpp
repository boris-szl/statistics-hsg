#include "discrete.hpp"

using std::cin;
using std::cout;
using std::endl;

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