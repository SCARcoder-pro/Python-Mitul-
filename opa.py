import scipy.stats as stats
prob1 = stats.poisson.pmf(12, 10)
print("Probablity of raining for more than 12 days in next 30 days:", prob1)

prob2 = stats.poisson.pmf(12, 10) + stats.poisson.pmf(13, 10) + + stats.poisson.pmf(14, 10) + stats.poisson.pmf(15, 10) + stats.poisson.pmf(16, 10) + stats.poisson.pmf(17, 10) + stats.poisson.pmf(18, 10) 
print("Probablity of raining for 12-18 days:", prob2)