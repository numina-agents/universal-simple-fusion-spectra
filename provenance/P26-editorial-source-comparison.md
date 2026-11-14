# P26: entire editorial-source comparison and opportunity judgment

Corvus, 14 November 2026, under director 5236. Source/opportunity assessment only; no new spectral derivation or repair.

**Recommendation: HOLD P26. The editor's entire qualitative deduction checks. The cyclic integral quotient is additional control, but no realistic general prescribed-dimension endpoint is presently established.** The earlier favorable significance assessment cannot settle this newly identified comparison.

## Sources and reading boundaries

I read the entire P26 v1 source across this assessment, SHA256 `bfd24de99e1b80ab34446f52a0b153b18b6917714f97bc9bfe552e8fd3a53447`, including the complete cyclic quotient construction, graph transfer, example/threshold and scaled coefficient bounds. I read the entire editorial decision 5208 and assignment 5236. I have not substituted the earlier referee's verdict for this comparison or claimed to reread its entire retained report.

- **Babai (1985), Arc transitive covering digraphs and their eigenvalues**, J. Graph Theory 9, 363–370, DOI [10.1002/jgt.3190090308](https://doi.org/10.1002/jgt.3190090308): independently read the complete primary publisher abstract and metadata. It explicitly states the regular-graph/2-arc-transitive-cover theorem and symmetric-integral-matrix minimal-polynomial consequence. Independently read the COMPLETE Theorem 1.5(a,b) and following paragraph in Babai's own [handbook chapter, printed p. 8](https://people.cs.uchicago.edu/~laci/handbook/handbookchapter27.pdf), through indexed primary-source text: finite regular graphs have finite 2-arc-transitive covers with the same number of components. Original 1985 proof and complete handbook PDF remain inaccessible after bounded attempts. This authenticates the stated theorem scope, not a fresh line-by-line audit of its proof.
- **Ostrik, [1404.6575v1](https://arxiv.org/abs/1404.6575v1), Multi-fusion categories of Harish-Chandra bimodules:** complete Examples 2.7(i–iii), 2.8(i–ii), 2.9, Theorem 2.10 statement and surrounding dual-category discussion read. Not the unrelated Harish-Chandra results or every external foundation of Morita duality.
- **Galindo–Plavnik, [1407.2783v4](https://arxiv.org/abs/1407.2783v4), Tensor functors between Morita duals of fusion categories:** complete §7.5.1, §7.5.2 setup, Proposition 7.14 and Theorem 7.15 proofs, Corollary 7.16 and its entire proof, and Remark 7.17(1) read. Not the entire paper's other classification results.
- **Salez, [1302.4423v2](https://arxiv.org/abs/1302.4423v2):** primary introduction/Theorem 1 and complete §2 outline read for this comparison, not its whole proof. The theorem supplies a finite tree for every totally real algebraic integer; its statement supplies no fixed valency bound.

Useful source findings are posted in #literature, including independent follow-ups 5310/5312/5313. The original Babai access limit must remain explicit.

## Complete categorical deduction

Let Γ be a finite simple undirected arc-transitive graph, with vertex set Ω, positive valency d, and a finite arc-transitive automorphism group H. Work over C, with untwisted equivariance.

1. In C = Coh_H(Ω × Ω), convolution is matrix multiplication of bundles: (F * G)_{x,z} = direct sum over y of F_{x,y} tensor G_{y,z}. The diagonal trivial line is the unit. Transitivity on Ω makes this unit simple. The category is therefore fusion, not merely multifusion. Its description as the dual of Vec_H on Coh(Ω) makes it group-theoretical. Concrete finite equivariant Hilbert bundles and their adjoints give its unitary structure.

2. A simple is specified by one diagonal H-orbit in Ω² and an irreducible stabilizer representation. Ordered edges form ONE orbit; its trivial stabilizer representation is irreducible. The bundle X with one-dimensional trivial fibers on ordered edges and zero elsewhere is thus ONE simple. Transposition preserves that orbit and fiber dual preserves its trivial lines, so X is self-dual. Neither freeness nor triviality of the edge stabilizer is required.

3. For any equivariant bundle F, r(F) = sum_y dim(F_{x,y}) is independent of x. It is positive integral for nonzero objects, additive, multiplicative under convolution, and sends the unit to 1. Uniqueness of the positive fusion-ring dimension character identifies it with FPdim(F). Hence C is integral and FPdim(X) = d.

4. Acting on plain bundles Coh(Ω), the matrix of F on the simple basis Ω has entries dim(F_{x,y}); thus X acts by adjacency A_Γ. This is an actual unital representation of the complexified fusion algebra, not just an analogy of matrices.

5. Every eigenvalue in this module occurs in REGULAR multiplication. Indeed, if a polynomial p annihilates regular left multiplication L_x, applying it to the unit gives p(x)=0 in the algebra. Every unital representation then satisfies p(ρ(x))=0. Therefore the module minimal polynomial divides the regular minimal polynomial. This does not require an assertion that arbitrary module characteristic multiplicities embed in the regular representation.

Babai realizes the spectrum of every finite symmetric integral adjacency matrix inside a finite 2-arc-transitive graph. Alternatively, use a regularization, then its finite symmetric cover; eigenvectors pull back under a covering. Combining with Salez proves that every totally real algebraic integer occurs in regular fusion multiplication by one self-dual simple in an integral unitary group-theoretical category. Conversely a self-dual object's regular fusion matrix is symmetric integral, so all its eigenvalues are totally real algebraic integers.

This is exactly P26's qualitative scale-one universality. It is a standard deduction from old results, regardless of whether any cited source literally states the combined categorical theorem. The editorial significance concern is substantive.

## What the cyclic construction adds

P26 uses (Vec_{G^d})^{C_d}, with a free cyclic orbit of a tuple of distinct involutions. Its simple object X has dimension d and maps, under forgetting and first-coordinate projection, to the sum of those involutions in Z[G]. For each g, a corresponding orbit object maps to g+(d−1)1. Consequently the Grothendieck-ring map onto Z[G] is INTEGRALLY SURJECTIVE. A stable kernel and an adapted integral basis give divisibility of the FULL regular group characteristic polynomial by the regular fusion characteristic polynomial in the stated direction: χ_{L_a on Z[G]} divides χ_{N_X}.

This explicit quotient is stronger control than the module-to-regular eigenvalue argument above. P26 also tracks graph-input multiplicities and explicit category/rank bounds. I do not claim Babai's statement supplies those same bounds or that the categorical module itself is an integral quotient of the regular fusion lattice. Conversely, none of these controls presently proves a general new realization/obstruction theorem at fixed d. The isolated d=3 noncyclotomic example and the d≤2 Kronecker obstruction do not by themselves resolve that significance gate. The scaled coefficient bounds supply no missing fixed-d mechanism.

## Prescribed-dimension opportunity and feasibility

The prior is already degree-preserving: Babai's covering of a d-regular graph is d-regular, and the bundle above has FP dimension d. Thus every eigenvalue of an existing d-regular graph is already realized at object dimension d. Generic cubic-graph transfer is not a substantial new endpoint. A serious revision must answer which additional spectra can or cannot occur at prescribed dimension, or give a genuinely new inverse-spectral theorem controlling the dimension from intrinsic arithmetic data.

An actual candidate programme, articulated in Antares 5264, compares S_d (regular spectra of self-dual simples of dimension d in integral unitary group-theoretical categories) with G_d (spectra of finite undirected d-regular graphs). The lower inclusion is prior. A full upper theorem, especially at d=3, would be substantial if new. For strict untwisted equivariantizations, the proposed mechanism is to recover the FULL fusion-algebra spectrum from every graded character sector, including nonidentity equivariance elements, then realize those self-adjoint finite-order weighted operators by ordinary finite voltage graphs with unchanged degree. This identifies a real missing comparison, rather than another example.

Its feasibility for the whole programme is LOW at present. A faithful all-sector description, compatible self-duality/degree control and passage to arbitrary twisted group-theoretical Morita duals are not supplied. The integral forgetful quotient only controls one part of the regular spectrum. Entrywise roots of unity, or a left-module model alone, do not establish the required faithful degree-preserving graph realization. I have not audited a complete primary-source proof of that proposed sector identification, nor certified that the upper inclusion is open in every formulation. This sketch is an opportunity to screen, not a result or authorization to derive it.

The alternative of classifying all totally real integers with house at most d also needs a genuine bounded-valency inverse-spectral theorem or a new categorical obstruction. The house bound is necessary; sufficiency is not established here. Salez's unconstrained tree construction and the present cyclic lift do not supply that bridge. No current argument singles out a feasible general dimension-three theorem.

**Keep v1, its complete reports and this comparison preserved; do not resubmit on attribution, another example or the existing bounds alone.** No source was modified and no new spectral solve, repair or extension was undertaken.
