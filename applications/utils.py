from scipy.spatial import distance_matrix
import numpy as np
from ripser import Rips
from sklearn.neighbors import KDTree
from sklearn.decomposition import PCA
import warnings
from kneed import KneeLocator
warnings.filterwarnings("ignore")

####################
# Geometric anomalies
####################

def local_neighborhood(data, scale):
    D = distance_matrix(data, data)
    n = scale[1]-scale[0]
    local_neigh = np.ndarray(shape=(len(D),n), dtype=int, order='F')
    radius = np.ndarray(shape=(len(D),2), dtype=float, order='F')
    for i in range(len(D)):
        local_neigh[i] = np.argsort(D[i])[scale[0]:scale[1]]
    D.sort()
    for i in range(len(D)):
        radius[i] = [D[i][scale[0]], D[i][scale[1]]]
    return local_neigh, radius
    
def compute_local_persistence(data, scale):
    k1 = scale[0]
    k2 = scale[1]
    
    local_neigh, radius = local_neighborhood(data, [k1, k2])
    
    rips = Rips()
    mask = []
    for i in range(len(data)):
        dgm = rips.fit_transform(data[local_neigh[i]])
        
        # here we only focus on betti 1

        lifetime = dgm[1][:,1]-dgm[1][:,0]

        r1 = radius[i][0]
        r2 = radius[i][1]
            
        N = np.where(lifetime>r2-r1)[0]

        if len(N)==0:
            mask.append(0) #boundary
        elif len(N)==1:
            mask.append(1) #regular point
        else:
            mask.append(2) # singular point

    return np.array(mask)


#################
# Local dimension
#################

def local_pointclouds(k, pointcloud):
    '''
    Constructs local pointclouds of size k
    '''
    kd_tree = KDTree(pointcloud, leaf_size=2)

    def neighbors_k(idx, k):
        return kd_tree.query(np.array([pointcloud[idx]]), k = k)

    def local_pointcloud(idx, k):
        dist, ind = neighbors_k(idx, k)
        return pointcloud[ind[0]]

    return np.array([local_pointcloud(i,k) for i in range(len(pointcloud))])


def local_pca(k, pointcloud, max_components = 6) :
    '''
    Applies PCA to local pointclouds and recover local dimension finding elbows in the function od recovered variances
    '''
    
    elbows = []
    recovered_variances = []

    lp = local_pointclouds(k, pointcloud)

    max_components = min(max_components, len(pointcloud[0]))
    
    for i in range(len(pointcloud)) :
        local = lp[i]
    
        pca = PCA(n_components=max_components)
        local_dimred = pca.fit_transform(local)
    
        vs = pca.explained_variance_ratio_
        
        kneedle = KneeLocator(range(max_components), vs, S=1, curve='convex', direction='decreasing')
        elbow = kneedle.elbow
        elbows.append(elbow)
        recovered_variances.append(np.sum(vs[:2]))
                
    recovered_variances = np.array(recovered_variances)
    elbows = np.array(elbows)
    
    return (elbows, recovered_variances)