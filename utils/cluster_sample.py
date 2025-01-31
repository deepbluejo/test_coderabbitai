from sklearn.mixture import GaussianMixture
import numpy as np

class RandCluster:
    def __init__(self, n_components):
        self.n_components = n_components

    def rand_means(self,factor_means):
        self.means = np.random.random(size = n_samples)
        self.weights = np.random.random(self.n_components)
        self.weights = self.weights/self.weights.sum()
        self.covariances = np.eye(self.n_components).reshape(1,self.n_components, self.n_components)

    def gmm_sampling_idont_know_name(self,):
        gmm = GaussianMixture(n_components= self.n_components)
        gmm.means_ = self.means
        gmm.weights_ = self.weights
        gmm.covariances_ = self.covariances
        self.gmm_sampling = gmm

    def sample_again(self, n_samples):
        self.gmm_sampling_idont_know_name()
        sample = self.gmm_sampling.sample(n_samples)
        return sample

c = RandCluster(5)
sample = c.sample_again(100)
print(sample.mean(0))

