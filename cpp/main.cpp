#include <bits/stdc++.h>

using namespace std;

using db = double;

const int H = 3;
const int N = 10000;

struct Point {
    db x, y;

    db getAbs(Point other) {
        return (x-other.x)*(x-other.x)+(y-other.y)*(y-other.y);
    }
};

struct Cluster {
    db xs;
    db ys;
    vector<Point> p = {};

    bool in(Point point) {
        return point.x >= xs && point.x <= xs + H && point.y >= ys && point.y <= ys + H;
    }

    void add(Point point) {
        p.push_back(point);
    }

    Point getCentroid() {
        db minsum = INT_MAX;
        int index = 0;
        for (int i = 0; i < p.size(); i++) {
            db sum = 0;
            for (int j = 0; j < p.size(); j++) {
                sum += p[i].getAbs(p[j]);
            }
            if (minsum > sum) {
                minsum = sum;
                index = i;
            }
        }
        return p[index];
    }
};


void solve() {
    Cluster A_1, A_2, A_3;
    A_1.xs = 0, A_1.ys = 0;
    A_2.xs = 5, A_2.ys = 4;
    A_3.xs = 2, A_3.ys = 7.5;

    for (int b = 0; b < N; b++) {
        Point point;
        cin >> point.x >> point.y;
        if (A_1.in(point)) {
            A_1.add(point);
        }
        else if (A_2.in(point)) {
            A_2.add(point);
        }
        else A_3.add(point);
    }

    Point c_1 = A_1.getCentroid();
    Point c_2 = A_2.getCentroid();
    Point c_3 = A_3.getCentroid();
    cout << ((c_1.x + c_2.x + c_3.x) / double(3))*10000 << '\n' << ((c_1.y + c_2.y + c_3.y) / double(3))*double(10000);
}

int main() {
    solve();
    return 0;
}
