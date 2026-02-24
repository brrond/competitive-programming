#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

class CPSolver {
public:
    CPSolver(bool debug);
    ~CPSolver();
    string get_string();
    int get_int();
    vector<int> get_ints(int n);
    void operator()();

    void solve() {
        // Solution goes here

    }
private:
    bool debug;
    istream* inp;
    ifstream* finp;
};

int main() {
    CPSolver solver(true);
    solver();

    return 0;
}

CPSolver::CPSolver(bool debug) {
    this->debug = debug;
    if (debug) {
        finp = new ifstream();
        finp->open("../input.txt");
        inp = finp;
    } else {
        inp = &cin;
    }
}

CPSolver::~CPSolver() {
    if (debug) {
        finp->close();
    }
}

void CPSolver::operator()() {
    solve();
}

string CPSolver::get_string() {
    string str;
    getline(*inp, str);
    return str;
}

int CPSolver::get_int() {
    int n;
    (*inp) >> n;
    return n;
}

vector<int> CPSolver::get_ints(int n) {
    if (n <= 0) return {};
    vector<int> ret;
    while (n--) {
        ret.push_back(get_int());
    }
    return ret;
}
