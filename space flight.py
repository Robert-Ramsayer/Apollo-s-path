import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# function that returns dy/dt
def model(z,t):
    mu = .01214

    r1 = np.sqrt((z[0] + mu) ** 2 + z[2] ** 2)
    r2 = np.sqrt((z[0] + mu - 1) ** 2 + z[2] ** 2)
    xder=[[],[],[],[]]
    xder[0] = z[1]
    xder[1] = 2 * z[3] + z[0] - ((1 - mu) * (z[0] + mu)) / (r1 ** 3) - (mu * (z[0] - 1 + mu)) / (r2 ** 3)
    xder[2] = z[3]
    xder[3] = -2 * z[1] + z[2] - ((1 - mu) * z[2]) / (r1 ** 3) - (mu * z[2]) / (r2 ** 3)
    return xder

# initial condition
x0=1.2
dx0=0.0
y0=0.0
dy0=-1.04935751

IC = [x0, dx0, y0, dy0]
T=6.19216933
# time points
step=10000
t = np.linspace(0,1*T,step)

# solve ODE
z = odeint(model,IC,t,rtol=1e-6)
x=z[:,0]
y=z[:,2]



#animation
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'orange', animated=True,label='Neil Armstrong')

def init():
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    return ln,
def update(frame):
    xdata.append(x[frame])
    ydata.append(y[frame])
    ln.set_data(xdata, ydata)
    return ln,
stepper=np.arange(0,step,20)
ani = FuncAnimation(fig, update, frames=stepper,interval=1,
                    save_count=50, init_func=init, blit=True)

#add the moon and earth
plt.scatter(0,0,c='green',marker='*',label='earth')
plt.scatter(1,0,c='grey',marker='o',label='moon')
plt.scatter(.1,.2,c='brown',marker='+',label='Space Monkey')

# plot results
#plt.plot(x,y,c='orange',label='shuttle')
plt.xlabel('horz')
plt.ylabel('vert')
plt.legend()
plt.show()

ani.save("movie.htm")
