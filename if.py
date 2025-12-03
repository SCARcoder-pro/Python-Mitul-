import numpy as np
np.random.seed(42)

puppies = np.array([1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
p=puppies.mean()
print("Mean", p)
print("Standard Deviation", puppies.std())
print("Vlariance", puppies.var())

np.random.choice(puppies, size=(1, 5), replace=True)
np.random.choice(puppies, size=(1, 5), replace=True).mean()

print("\nSampling Sistribution with 5 \n")
twenty_sample_props = []
for i in range(10000):
    sample = np.random.choice(puppies, 5, replace=True)
    twenty_sample_props.append(sample.mean())
twenty_sample_props = np.array(twenty_sample_props)

print("New mean", twenty_sample_props.mean())
print("New Standard Deviation", twenty_sample_props.std())
print("New Variance", twenty_sample_props.var())
