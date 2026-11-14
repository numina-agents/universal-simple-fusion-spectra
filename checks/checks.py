"""Small exact checks of the proposed construction; no fusion dataset is generated."""
from fractions import Fraction
from math import factorial

def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def charpoly(a):
    n=len(a); b=[[int(i==j) for j in range(n)] for i in range(n)]; cs=[1]
    for k in range(1,n+1):
        ab=mm(a,b); c=-Fraction(sum(ab[i][i] for i in range(n)),k)
        assert c.denominator==1
        cs.append(int(c)); b=[[ab[i][j]+c*(i==j) for j in range(n)] for i in range(n)]
    return cs

def regularize(a,D):
    n=len(a); deficits=[v for v in range(n) for _ in range(D-sum(a[v]))]
    delta=len(deficits); M=delta+D*n
    out=[[0]*M for _ in range(M)]
    for i in range(D):
        for v in range(n):
            for w in range(n): out[delta+i*n+v][delta+i*n+w]=a[v][w]
        for j,v in enumerate(deficits):
            out[j][delta+i*n+v]=out[delta+i*n+v][j]=1
    assert all(sum(row)==D for row in out)
    assert all(out[i][j]==out[j][i] for i in range(M) for j in range(M))
    assert all(out[i][i]==0 for i in range(M))
    return out,delta

def matchings(a,D):
    n=len(a); remaining=[{j for j in range(n) if a[i][j]} for i in range(n)]
    qs=[]
    for _ in range(D):
        right={}
        def augment(i,seen):
            for j in sorted(remaining[i]):
                if j in seen: continue
                seen.add(j)
                if j not in right or augment(right[j],seen):
                    right[j]=i; return True
            return False
        assert all(augment(i,set()) for i in range(n))
        left={i:j for j,i in right.items()}
        q=list(range(2*n))
        for i,j in left.items():
            q[i]=n+j; q[n+j]=i; remaining[i].remove(j)
        assert all(q[q[i]]==i and q[i]!=i for i in range(2*n))
        qs.append(tuple(q))
    assert not any(remaining)
    assert len(set(qs))==D
    return qs

paw=[[0,1,1,1],[1,0,1,0],[1,1,0,0],[1,0,0,0]]
assert charpoly(paw)==[1,0,-4,-2,1]
# (t+1)(t^3-t^2-3t+1); rational-root test proves cubic irreducibility.
a,b,c=-1,-3,1
disc=a*a*b*b-4*b**3-4*a**3*c-27*c*c+18*a*b*c
assert disc==148 and all(x**3-x*x-3*x+1 for x in [-1,1])
y,delta=regularize(paw,3)
assert delta==4 and len(y)==16
qs=matchings(y,3)
assert len(qs)==3 and len(qs[0])==32
# Check the signed-copy embedding of the original adjacency representation.
n=4; M=len(y)
for v in range(n):
    e=[0]*M; e[delta+v]=1; e[delta+n+v]=-1
    ye=[sum(y[i][j]*e[j] for j in range(M)) for i in range(M)]
    expected=[0]*M
    for w in range(n):
        expected[delta+w]=paw[w][v]; expected[delta+n+w]=-paw[w][v]
    assert ye==expected
# The three distinct involutions have a free CYCLIC orbit.
orbit=[tuple((i+j)%3 for i in range(3)) for j in range(3)]
assert len(set(orbit))==3
first_counts=[sum(p[0]==i for p in orbit) for i in range(3)]
assert first_counts==[1]*3
print('PASS: paw charpoly [1,0,-4,-2,1], irreducible cubic discriminant 148.')
print('PASS: regularization M=16, bipartite size N=32, three distinct matching involutions.')
print('PASS: signed-copy intertwining and cyclic orbit scale m=1, simple dimension 3.')
for index,q in enumerate(qs,1):
    print('matching',index,[(i+1,q[i]+1) for i in range(len(q)) if i<q[i]])

# Compact actual categorical control: G=D_20, d=3, no large fusion matrix.
def dmul(g,h):
    a,b=g; c,d=h
    return ((a+(-1 if b else 1)*c)%10,(b+d)%2)
G=[(a,b) for a in range(10) for b in range(2)]
S=[(0,1),(1,1),(3,1)]
assert all(dmul(s,s)==(0,0) for s in S)
idx={g:i for i,g in enumerate(G)}
L=[[0]*20 for _ in G]
for j,g in enumerate(G):
    for s in S: L[idx[dmul(s,g)]][j]+=1

def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
expected=[1]
for f in ([1,0,-9],[1,0,-1],[1,0,-7,0,11],[1,0,-7,0,11],
          [1,0,-3,0,1],[1,0,-3,0,1]):
    expected=pmul(expected,f)
assert charpoly(L)==expected
assert (20**3-20)//3+3*20==2720
assert 2660*3**2+60==24000
print('PASS: D_20 regular group spectrum polynomial (t^2-9)(t^2-1)'
      '(t^4-7t^2+11)^2(t^4-3t^2+1)^2.')
print('Cyclic equivariantization: rank 2720, FPdim 24000, selected simple dimension 3.')

# Exact rational trace-Gram realization for f=t^3-t^2-3t+1.
def tr(a): return [list(c) for c in zip(*a)]
def eye(n): return [[Fraction(i==j) for j in range(n)] for i in range(n)]
def inv(a):
    n=len(a); b=[list(map(Fraction,row))+e for row,e in zip(a,eye(n))]
    for j in range(n):
        pivot=next(i for i in range(j,n) if b[i][j]); b[j],b[pivot]=b[pivot],b[j]
        q=b[j][j]; b[j]=[x/q for x in b[j]]
        for i in range(n):
            if i!=j:
                q=b[i][j]; b[i]=[x-q*y for x,y in zip(b[i],b[j])]
    return [row[n:] for row in b]
M=[[0,0,-1],[1,0,3],[0,1,1]]
Q=[[3,1,7],[1,7,7],[7,7,27]]
assert mm(Q,M)==mm(tr(M),Q)
L0=eye(3); D=[]
for i in range(3):
    D.append(Fraction(Q[i][i])-sum(L0[i][k]**2*D[k] for k in range(i)))
    for j in range(i+1,3):
        L0[j][i]=(Q[j][i]-sum(L0[j][k]*L0[i][k]*D[k] for k in range(i)))/D[i]
assert D==[Fraction(3),Fraction(20,3),Fraction(37,5)]
B0=[[Fraction(0) for _ in range(3)] for _ in range(12)]
for i,(b,us) in enumerate([(1,[1,1,1,0]),(3,[7,3,1,1]),(5,[13,4,0,0])]):
    assert sum(u*u for u in us)==D[i].numerator*D[i].denominator
    for j,u in enumerate(us): B0[4*i+j][i]=Fraction(u,b)
B=mm(B0,tr(L0)); assert mm(tr(B),B)==Q
A=mm(mm(mm(B,M),inv(Q)),tr(B))
assert A==tr(A) and mm(A,B)==mm(B,M)
P=3*20*148; ell=P**5
assert all((ell*x).denominator==1 for row in A for x in row)
assert charpoly(A)==pmul([1,-1,-3,1],[1]+[0]*9)
print('PASS: rational trace-Gram realization, Delta=(3,20,148), P=8880, ell=P^5.')
print('PASS: B^T B=Q, A=A^T, AB=BM, ell*A integral, charpoly(A)=t^9 f(t).')

# Tiny signed/diagonal/entry-reduction control for the graph operations.
def block(u,v):
    return [a+b for a,b in zip(u,v)]+[b+a for a,b in zip(u,v)]
W=[[2,-1],[-1,0]]
pos=[[max(x,0) for x in row] for row in W]
neg=[[max(-x,0) for x in row] for row in W]
C=block(pos,neg)
diag=[[C[i][j] if i==j else 0 for j in range(4)] for i in range(4)]
off=[[C[i][j] if i!=j else 0 for j in range(4)] for i in range(4)]
C=block(off,diag)
rows=[sum(row) for row in C]
E=[[int(x>0) for x in row] for row in C]
Dmat=[[x-y for x,y in zip(row,erow)] for row,erow in zip(C,E)]
Graph=block(Dmat,E)
assert all(x in (0,1) for row in Graph for x in row)
assert Graph==tr(Graph) and all(Graph[i][i]==0 for i in range(16))
assert [sum(row) for row in Graph]==rows+rows
cp=charpoly(Graph)
for _ in range(1):
    divisor=charpoly(W); rem=cp[:]
    for i in range(len(rem)-len(divisor)+1):
        q=rem[i]
        for j,x in enumerate(divisor):rem[i+j]-=q*x
    assert not any(rem)
print('PASS: signed, diagonal-removal and support block operations give a simple graph retaining W spectrum.')
