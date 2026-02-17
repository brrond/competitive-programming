#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

enum Result {
    FINE = 1,
    WEEKEND_WORK = 2,
    SERIOUS_TROUBLE = 3
};

class CPSolver {
public:
    CPSolver(bool debug);
    ~CPSolver();
    string get_string();
    int get_int();
    vector<int> get_ints(int n);
    void operator()();

    Result calc(int curr_piano_index) {
        if (curr_piano_index >= this->_start_end_days->size()) {
            return FINE;
        }

        auto &start_end_days = *this->_start_end_days;
        auto &capacity = *this->_capacity;

        Result final_result = SERIOUS_TROUBLE;
        // T(100)
        for (int today = start_end_days[curr_piano_index].first; today <= start_end_days[curr_piano_index].second; today++) {

            // try to move piano on "today"
            // if capacity allows
            if (capacity[today] > 0) {

                // Update state
                // O(1)
                capacity[today]--;

                // O(m)
                auto res = calc(curr_piano_index + 1);

                // Restore state
                // O(1)
                capacity[today]++;

                final_result = min(res, final_result);
                if ((today % 7 == 0 || today % 7 == 6) && final_result == FINE) {
                    final_result = WEEKEND_WORK;
                }
                if (final_result == FINE) break;
            }
        }

        return final_result;

        // Total complexity:
        // O(100 * m)
    }

    void solve() {
        int n = get_int();
        // O(n)
        while(n--) {

            int m = get_int();
            int p = get_int();

            int possible_moves_a_day = p / 2;
            // possible worked capacity (101 because I'm lazy to do -1)
            vector<int> capacity(101, possible_moves_a_day);
            this->_capacity = &capacity;

            vector<pair<int, int>> start_end_days(m, make_pair(0, 0));
            this->_start_end_days = &start_end_days;

            // read input
            // O(m)
            generate(start_end_days.begin(), start_end_days.end(), [this, &capacity]() {
                int b = this->get_int();
                int e = this->get_int();
                return make_pair(b, e);
            });

            if (debug) {
                for_each(start_end_days.begin(), start_end_days.end(), [](pair<int, int> se) { 
                    cout << se.first << " " << se.second << endl;
                });
            }

            // Case 1: if there are pianos with end_day == start_day
            // they can only be moved on that day.
            // In this case, if there are more piano to be moved -> impossible.
            bool possible = true;
            // O(m)
            start_end_days.erase(
                remove_if(start_end_days.begin(), start_end_days.end(), [&capacity, &possible](pair<int, int> se_day){
                    if ((se_day.second - se_day.first) == 0) {
                        // O(1)
                        capacity[se_day.first]--;

                        // O(1)
                        if (capacity[se_day.first] < 0) {
                            possible = false;
                        }

                        return true;
                    }
                    return false;
                }), 
                start_end_days.end()
            );
            if (!possible) {
                cout << "serious trouble" << endl;
                continue;
            }

            // Case 2: all others.
            // I assume it's DP.
            // mem[curr_piano_index] = {"ww", "f", "st"}
            // 100 * m
            auto res = calc(0);
            switch (res) {
                case FINE: cout << "fine" << endl; break;
                case WEEKEND_WORK: cout << "weekend work" << endl; break;
                case SERIOUS_TROUBLE: cout << "serious trouble" << endl; break;
            }
        }

        // Total complexity:
        // O(n * (2m + 100m)) = O(nm)
    }

private:
    vector<int>* _capacity = NULL;
    vector<pair<int, int>>* _start_end_days = NULL;


private:
    bool debug;
    istream* inp;
    ifstream* finp;
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
