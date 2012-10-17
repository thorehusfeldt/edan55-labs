/* Call init_inverses(prime) once at startup and then determinant(A,prime) to compute det(A) mod prime.

 Make sure the entries in the input A matrix all are in the range [0..p-1]
*/

static int inv[];
public static int modexp(int a, int e, int p)
{
 if (e == 1) {
  return a;
 } else {
  int sq = modexp(a, e/2, p);
  sq = (sq * sq) % p;
  if ((e & 1) == 1) {
   sq = (sq * a) % p;
  }
  return sq;
 }
}
public static void init_inverses(int p)
{
 int i;
 inv = new int[p];
 for (i = 1; i < p; i++) {
  inv[i] = modexp(i, p-2, p);
 }
}
public static int determinant(int[][] A, int p) { 
 int n = A[0].length;
 int i, j, k;
 int rs[],vis[];
 int d = 1;
 int sgn = 0;
 rs = new int[n];
 vis = new int[n];
 for (i = 0; i < n; i++) {
  rs[i] = 0;
 }
 for (i = 0; i < n; i++) {
  int who = -1;
  for (j = 0; j < n; j++) 
   if (rs[j] == 0 && A[j][i]>0) {
    rs[j] = i+1;
    who = j;
    d = (d * A[j][i]) % p;
    break;
   }
  if (who == -1) {
   d = 0;
   break;
  }
  for (j = 0; j < n; j++) 
   if (rs[j] == 0 && A[j][i]>0) {
    d = (d * inv[A[who][i]]) % p;
 
    for (k = n-1; k >= i; k--) {
     A[j][k] = (A[who][i] * A[j][k] - A[j][i] * A[who][k] + p*p) % p;
   }
  }
 }
 if (d > 0) {
  sgn = n;
  for (i = 0; i < n; i++) {
   vis[i] = 0; 
  }
  for (i = 0; i < n ; i++) {
   if (vis[i] == 0) {
    sgn--;
    j = i;
    while (vis[j] == 0) {
     vis[j] = 1;
     j = rs[j] - 1;
    }
   }
  }
 
  if ((sgn&1)==1)
   d = p - d; 
 }
 return d;
}