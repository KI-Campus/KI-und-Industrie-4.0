def mae(x, x_pred):
    n = x.shape[1]
    diff = x - x_pred
    return np.sum(np.abs(diff), axis=1)/n 