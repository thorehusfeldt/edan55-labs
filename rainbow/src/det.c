/* Call init_inverses once at startup */

#define PRIME (32479)
#define PRIME2 (PRIME*PRIME)
#define MAXN (25)

static int inv[PRIME];
static int vis[MAXN];

/* The input matrix A is an array with element at row i and column j at index i*n+j */
int det(int *A, int n)
{
 int i, j, k;
 int rs[n];
 int d = 1;
 int sgn = 0;
 for (i = 0; i < n; i++) {
  rs[i] = 0;
 }

 for (i = 0; i < n; i++) {
  int who = -1;

 for (j = 0; j < n; j++) 
  if (rs[j] == 0 && A[j * n + i]) {
   rs[j] = i+1;
   who = j;
   d = (d * A[j * n + i]) % PRIME;
   break;
  }
  if (who == -1) {
   d = 0;
   break;
  }
  for (j = 0; j < n; j++) 
   if (rs[j] == 0 && A[j * n + i]) {
    d = (d * inv[A[who * n + i]]) % PRIME;
 
    for (k = n - 1; k >= i; k--) {
     A[j * n + k] = (A[who * n + i] * A[j * n + k] - A[j * n + i] * A[who * n + k] + PRIME2) % PRIME;
    }
   }
 }
 if (d) {
  sgn = n;
  for (i = 0; i < n; i++) {
   vis[i] = 0; 
  }
  for (i = 0; i< n ; i++) {
   if (!vis[i]) {
    sgn--;
    j = i;
    while (vis[j] == 0) {
     vis[j] = 1;
     j = rs[j] - 1;
    }
   }
  }
 
  if (sgn&1)
   d = PRIME - d; 
 }
 return d;

}

int modexp(int a, int e)
{
 if (e == 1) {
  return a;
 } else {
  int sq = modexp(a, e/2);
  sq = (sq * sq) % PRIME;
  if (e & 1) {
   sq = (sq * a) % PRIME;
  }
  return sq;
 }
}

void init_inverses()
{
 int i;
 for (i = 1; i < PRIME; i++) {
  inv[i] = modexp(i, PRIME-2);
 }
}
