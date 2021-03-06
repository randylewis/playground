# beginning.py   randy.lewis@yorku.ca
from collections import defaultdict
from dwave.system import DWaveSampler, EmbeddingComposite
lam = 0.0
y = 0.0
Q = defaultdict(float)
Q[(0,0)] = -lam
Q[(0,1)] = 8*y
Q[(0,2)] = 0.0 
Q[(1,1)] = 3.0 - lam
Q[(1,2)] = 2*y
Q[(2,2)] = 3.0 - lam
sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(Q,num_reads=10)
print(sampleset)
