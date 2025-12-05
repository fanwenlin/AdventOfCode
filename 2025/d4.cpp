#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>

using namespace std;
typedef long long ll;
char s[200][300];
int n, m;
int countSurround(int x, int y) {
    int ans = 0;
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            if (i == 0 && j == 0)
                continue;
            int nx = x + i, ny = y + j;
            if (nx >= 1 && nx <= n && ny >= 1 && ny <= m && s[nx][ny] == '@') {
                ans++;
            }
        }
    }
    return ans;
}

int main() {
    // ios::sync_with_stdio(false);
    // cin.tie(0);
#ifdef FWL
    freopen("data.in", "r", stdin);
    // freopen("data.out", "w", stdout);
#endif
    n = 1;

    while (scanf("%s", s[n] + 1) == 1) {
        n++;
    }
    n--;
    m = strlen(s[1] + 1);
    int ans = 0;
    int ans2 = 0;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (countSurround(i, j) < 4 && s[i][j] == '@') {
                ans++;
            }
        }
    }
    int removable = ans;
    queue<pair<int, int>> q;
    while (removable > 0) {
        ans2 += removable;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (countSurround(i, j) < 4 && s[i][j] == '@') {
                    q.push({i, j});
                }
            }
        }
        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();
            s[x][y] = '.';
        }
        removable = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (countSurround(i, j) < 4 && s[i][j] == '@') {
                    removable++;
                }
            }
        }
    }
    cout << ans << endl;
    cout << ans2 << endl;
}