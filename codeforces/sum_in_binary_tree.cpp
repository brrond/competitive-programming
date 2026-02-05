#include <iostream>
#include <fstream>
#include <istream>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

class CPSolver {
public:
    CPSolver(bool debug) : debug(debug) {
        if (debug) {
            fstream* fin = new fstream();
            fin->open("../input.txt");
            inp = fin;
        } else {
            inp = &cin;
        }
    }

    void solve();
private:
    istream *inp;
    bool debug;

    int get_int() {
        int n;
        (*inp) >> n;
        return n;
    }   
};

int main() {
    auto solver = CPSolver(true);
    solver.solve();

    return 0;
}

void CPSolver::solve() {
    int t = this->get_int();
    while (t--) {

        ll n = this->get_int();
        ll sum = n;

        while (n != 1) {
            n = n >> 1; // TODO: what's wrong here? :(
            sum += n;
        }

        cout << sum << endl;
    }
}

