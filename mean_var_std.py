import numpy as np

def calculate(lista):

    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")

    calculations = {}
    r,c = 3,3
    arr = np.array(lista)
    m = arr.reshape(r,c)
    calculations['mean']=[np.mean(m,0).tolist(),np.mean(m,1).tolist(),np.mean(m)]
    calculations['variance']=[np.var(m,0).tolist(),np.var(m,1).tolist(),np.var(m)]
    calculations['standard deviation']=[np.std(m,0).tolist(),np.std(m,1).tolist(),np.std(m)]
    calculations['max']=[np.max(m,0).tolist(),np.max(m,1).tolist(),np.max(m)]
    calculations['min']=[np.min(m,0).tolist(),np.min(m,1).tolist(),np.min(m)]
    calculations['sum']=[np.sum(m,0).tolist(),np.sum(m,1).tolist(),np.sum(m)]
    return calculations
