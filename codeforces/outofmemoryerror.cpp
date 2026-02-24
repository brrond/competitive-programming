#include <algorithm>
#include <cstring>
#include <fstream>
#include <iostream>
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
            int m = get_int();
            int h = get_int();

            // Original array
            // O(n)
            int *arr_original = new int[n];
            for (int i = 0; i < n; i++) {
                *this->inp >> arr_original[i];
            }

            // Array to work with
            // O(1)
            int *arr = new int[n];
            memcpy(arr, arr_original, 4 * n);

            // O(m)
            vector<pair<int, int>> operations;
            while (m--) {
                int i = get_int() - 1;
                int c = get_int();
                operations.push_back(make_pair(i, c));

                // Ignore operations that are simply impossible to do
                if (arr[i] + c > h) {
                    operations.clear();
                }
            }

            // Apply the rest of the iterations
            // O(m)
            for (auto it = operations.begin(); it < operations.end(); it++) {
                if (arr[it->first] + it->second > h) {
                    // Reset
                    // O(?)
                    memcpy(arr, arr_original, 4 * n);
                } else {
                    arr[it->first] += it->second;
                }
            }

            // Print output
            for (int i = 0; i < n; i++) {
                cout << arr[i];
                if (i != n - 1) {
                    cout << " ";
                }
            }
            cout << endl;
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
