y = temps_2010.values
X = np.arange(len(y)).reshape(-1, 1)

from sklearn.gaussian_process.kernels import 

kernel = (1.0 * RBF(length_scale=100.0, length_scale_bounds=(1e-2, 1e3)) 
    + WhiteKernel(noise_level=1, noise_level_bounds=(1e-10, 1e+2)))
    
gp = gaussian_process.GaussianProcessRegressor(kernel=kernel)
gp.fit(X, y)

gp.kernel_

x_pred = np.linspace(0, len(y)).reshape(-1,1)
y_pred, sigma = gp.predict(x_pred, return_std=True)