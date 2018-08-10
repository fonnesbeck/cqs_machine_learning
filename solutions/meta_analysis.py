r_t_obs = [3, 7, 5, 102, 28, 4, 98, 60, 25, 138, 64, 45, 9, 57, 
           25, 33, 28, 8, 6, 32, 27, 22]
n_t_obs = [38, 114, 69, 1533, 355, 59, 945, 632, 278,1916, 873, 263, 
           291, 858, 154, 207, 251, 151, 174, 209, 391, 680]
r_c_obs = [3, 14, 11, 127, 27, 6, 152, 48, 37, 188, 52, 47, 16, 45, 
           31, 38, 12, 6, 3, 40, 43, 39]
n_c_obs = [39, 116, 93, 1520, 365, 52, 939, 471, 282, 1921, 583, 266, 
           293, 883, 147, 213, 122, 154, 134, 218, 364, 674]
N = len(n_c_obs)

with Model() as meta_analysis:
    
    δ = Normal('δ', 0, sd=10)
    μ = Normal('μ', -1, sd=10)
    
    p_control = invlogit(μ)
    p_treat = invlogit(μ + δ)
    
    control_obs = Binomial('control_obs', n=n_c_obs, p=p_control, observed=r_c_obs)
    treat_obs = Binomial('treat_obs', n=n_t_obs, p=p_treat, observed=r_t_obs)
    
with meta_analysis:
    
    tr = sample(1000, tune=2000, cores=2)
    
from pymc3 import plot_posterior

plot_posterior(tr, varnames=['δ'],  ref_val=0)

from scipy.stats import percentileofscore
pred_data = sample_ppc(tr, samples=500, model=meta_analysis)

pred_control_obs = pred_data['control_obs']
[percentileofscore(pred_control_obs[:, i], r_c_obs[i]) for i in range(N)]