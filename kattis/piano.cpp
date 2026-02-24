#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

struct Piano {
    int first_day;
    int last_day;

    Piano() : Piano(0, 0) {}
    Piano(int f, int l) : first_day(f), last_day(l) {}
    int get_span() { return last_day - first_day; }
};

class CPSolver {
  public:
    CPSolver(bool debug);
    ~CPSolver();
    string get_string();
    int get_int();
    vector<int> get_ints(int n);
    void operator()();

    void solve() {
        int n = get_int();
        // O(n)
        while (n--) {

            int m = get_int();
            int p = get_int();
            int possible_moves_a_day = p / 2;
            if (debug) {
                cout << "Number of available moves per day: "
                     << possible_moves_a_day << endl;
            }
            if (m == p && m == 0) {
                cout << "fine" << endl;
                continue;
            }

            vector<Piano> pianos(m, Piano());

            // read input
            // O(m)
            generate(pianos.begin(), pianos.end(), [this]() {
                int f = this->get_int();
                int l = this->get_int();
                return Piano(f, l);
            });

            // O(m log m)
            sort(pianos.begin(), pianos.end(),
                 [](Piano &piano1, Piano &piano2) {
                     return piano1.first_day < piano2.first_day;
                 });

            if (debug) {
                cout << "Print all sorted piano deliveries:" << endl;
                for_each(pianos.begin(), pianos.end(), [](Piano pm) {
                    cout << pm.first_day << " " << pm.last_day << endl;
                });
            }

            // Try to make all moves NOT on weekends
            priority_queue<int, vector<int>, greater<int>> latest_delivery_day;
            int piano_i = 0;
            bool possible = possible_moves_a_day > 0;
            for (int today = 0; today <= 100 && possible; today++) {

                // Skip weekends for now
                if ((today % 7) == 0) {
                    continue;
                } else if ((today % 7) == 6) {
                    continue;
                }

                // Take all pianos of this day
                while (piano_i < pianos.size() &&
                       pianos[piano_i].first_day <= today) {
                    latest_delivery_day.push(pianos[piano_i++].last_day);
                }

                // Until capacity allows
                int capacity = possible_moves_a_day;
                while (capacity != 0 && !latest_delivery_day.empty()) {

                    // take piano that can't wait
                    int latest_day = latest_delivery_day.top();
                    latest_delivery_day.pop();
                    if (latest_day < today) {
                        possible = false;
                        break;
                    }
                    capacity--;
                }
            }

            if (possible && latest_delivery_day.empty() && piano_i == m) {
                cout << "fine" << endl;
                continue;
            }

            // Try to make all moves
            priority_queue<int, vector<int>, greater<int>>
                latest_delivery_day_2;
            piano_i = 0;
            possible = possible_moves_a_day > 0;
            for (int today = 0; today <= 100 && possible; today++) {

                // Take all pianos of this day
                while (piano_i < pianos.size() &&
                       pianos[piano_i].first_day <= today) {
                    latest_delivery_day_2.push(pianos[piano_i++].last_day);
                }

                // Until capacity allows
                int capacity = possible_moves_a_day;
                while (capacity != 0 && !latest_delivery_day_2.empty()) {

                    // take piano that can't wait
                    int latest_day = latest_delivery_day_2.top();
                    latest_delivery_day_2.pop();
                    if (latest_day < today) {
                        possible = false;
                        break;
                    }
                    capacity--;
                }
            }

            if (possible && latest_delivery_day_2.empty() && piano_i == m) {
                cout << "weekend work" << endl;
            } else {
                cout << "serious trouble" << endl;
            }
        }
    }

  private:
  private:
    bool debug;
    istream *inp;
    ifstream *finp;
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
