#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
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
        int t = get_int();
        while (t--) {

            int n = get_int();
            vector<int> a = get_ints(n);

            long long ans = 0;
            vector<long long> sums;
            map<long long, long long> seen_sums;
            for (int i = 0; i < n - 4; i++) {
                long long s = a[i] + a[i + 2] - a[i + 4];
                if (seen_sums.find(s) == seen_sums.end()) {
                    seen_sums[s] = 0;
                }

                ans += seen_sums[s];
                seen_sums[s]++;

                sums.push_back(s);
                if (i >= 2 && sums[i - 2] == s)
                    ans--;
                if (i >= 4 && sums[i - 4] == s)
                    ans--;
            }

            cout << ans << endl;
        }
    }

  private:
    bool debug;
    istream *inp;
    ifstream *finp;
};

int main() {
    CPSolver solver(false);
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

void CPSolver::operator()() { solve(); }

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
    if (n <= 0)
        return {};
    vector<int> ret;
    while (n--) {
        ret.push_back(get_int());
    }
    return ret;
}
