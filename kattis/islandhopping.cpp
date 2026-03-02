#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

struct Edge {
    int from;
    int to;
    float cost;

    Edge(int from, int to, float cost) : from(from), to(to), cost(cost) {}

    bool operator<(Edge e2) const { return cost > e2.cost; }
};

class CPSolver {
  public:
    CPSolver(bool debug);
    ~CPSolver();
    string get_string();
    int get_int();
    float get_float();
    vector<int> get_ints(int n);
    void operator()();

    float get_cost(int i, int j) {
        pair<float, float> i1 = islands[i];
        pair<float, float> i2 = islands[j];

        return sqrt(pow(i2.second - i1.second, 2) +
                    pow(i2.first - i1.first, 2));
    }

    void add_edges(int node) {
        visited[node] = true;

        for (int i = 0; i < islands.size(); i++) {
            if (visited[i])
                continue;

            pq_pointer->push(Edge(node, i, get_cost(node, i)));
        }
    }

    void solve() {
        int n = get_int();

        while (n--) {
            islands.clear();
            visited.clear();

            int m = get_int();

            for (int i = 0; i < m; i++) {
                float x = get_float();
                float y = get_float();

                islands.push_back(make_pair(x, y));
                visited.push_back(false);
            }

            priority_queue<Edge> pq;
            pq_pointer = &pq;
            add_edges(0);

            float total_cost = 0;
            int mst_nodes = 1;

            while (pq.size() != 0 && mst_nodes < m) {
                Edge e = pq.top();
                pq.pop();

                if (visited[e.to])
                    continue;

                mst_nodes += 1;
                total_cost += e.cost;
                add_edges(e.to);
            }

            cout << total_cost << endl;
        }
    }

  private:
    vector<pair<float, float>> islands;
    vector<bool> visited;
    priority_queue<Edge> *pq_pointer;

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

float CPSolver::get_float() {
    float n;
    (*inp) >> n;
    return n;
}
