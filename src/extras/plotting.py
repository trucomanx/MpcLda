#!/usr/bin/python

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def plot_points_frame(  x1, x2,mu1,mu2,Vecs,Vals,
                        fig, ax, t=0, 
                        elev=30, azim=-60):
    ax.view_init(elev=elev, azim=azim+t)#, roll=roll)
    #print('ax.elev {}'.format(ax.elev))
    #print('ax.azim {}'.format(ax.azim))
    #print('ax.elev {}'.format(ax.roll))

    scat=ax.scatter3D(x1[0,:], x1[1,:], x1[2,:], c="r");
    scat=ax.scatter3D(x2[0,:], x2[1,:], x2[2,:], c="b");

    ax.set_xlabel('$X_1$')
    ax.set_ylabel('$X_2$')
    ax.set_zlabel('$X_3$')
    #plt.gca().set_aspect('equal')

    return scat;
  

def create_frame2(  x1,x2,mu1,mu2,Vecs,Vals,
                    fig,ax,t=0,
                    elev=30, azim=-60):
    ax.view_init(elev=elev, azim=azim+t)

    scat=ax.scatter3D(x1[0,:], x1[1,:], x1[2,:], c="r");

    scat=ax.scatter3D(x2[0,:], x2[1,:], x2[2,:], c="b");

    mu=(mu1+mu2)/2.0;
    suma=np.sum(np.abs(Vals));
    V=2*Vecs[0,:]*np.diag(Vals)/suma;
    scat=ax.quiver( mu[0,0]*np.ones((3,)),
                  mu[1,0]*np.ones((3,)),
                  mu[2,0]*np.ones((3,)),
                  8*V[0,:],
                  8*V[1,:],
                  8*V[2,:],
                  length=0.5, normalize=False,color='black')

    ax.set_xlabel('$X_1$')
    ax.set_ylabel('$X_2$')
    ax.set_zlabel('$X_3$')
    #plt.gca().set_aspect('equal')

    return scat;

################################################################################

import matplotlib.animation as animation
from matplotlib import rc
rc('animation', html='jshtml')#'html5'

from tqdm.notebook import tqdm
import numpy as np

def func_animate(x1,x2,mu1,mu2,Vecs,Vals,function_plot,Ntot):
    pbar=tqdm(total=2*Ntot+1, position=0, leave=True)
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    
    def animate(t):
      pbar.update();
      return function_plot(x1,x2,mu1,mu2,Vecs,Vals,fig,ax,t=3*t),

    ani = animation.FuncAnimation(fig, animate,
                                  frames=np.linspace(-Ntot,Ntot,2*Ntot+1),
                                  repeat=True,
                                  interval=50);
    return ani
