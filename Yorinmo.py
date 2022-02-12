import numpy as np
import matplotlib.pyplot as plt
import imageio

data = np.loadtxt("burger.dat")


n_times=np.shape(data)[0]
n_space=int(np.sqrt(np.shape(data)[1]))
x=np.linspace(0.0,2.0, n_space**2)
y=np.linspace(0.0,2.0, n_space**2)
dx=2.0/n_space
for i in range(n_space):
    for j in range(n_space):
        x[n_space*i+j]=i*dx
        y[n_space*i+j]=j*dx
        
t=np.linspace(0.0,0.05, n_times)

u=np.zeros((n_space, n_space))

for i in range(n_times):
    filename="snap_{}.png".format(i)
    fig=plt.figure(figsize=(3,3))
    plt.scatter(x,y, c=data[i,:], s=20, marker="s")
    plt.title("Tiempo {:.3f} segundos".format(t[i]))
    plt.xlabel("Posición [metros]")
    plt.ylabel("Posición [metros]")
    plt.ylim(0.0,2.0)
    plt.xlim(0.0,2.0)
    plt.grid()
    plt.savefig(filename,bbox_inches="tight")
    plt.close(fig)
    
    
with imageio.get_writer('burgers.gif', mode='I') as writer:
    for i in range(n_times):
        filename = "snap_{}.png".format(i)
        image = imageio.imread(filename)
        writer.append_data(image)
