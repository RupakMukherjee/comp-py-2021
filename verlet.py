#!/usr/bin/ python
import numpy as np
import math
import random
import time

def main():
    #========== Input Parameters ===========

    Lx      = 10.0   # System length in X
    Ly      = 10.0   # System length in Y
    Lz      = 10.0   # System length in Z

    N       = 100    # Number of particles

    tmax    = 2.0   # Final time
    dt      = 0.01   # time step size
    Nt      = round(tmax/dt)  #number of time steps

    Vxmax   = 1.0    # Maximum velocity in X
    Vymax   = 1.0    # Maximum velocity in Y
    Vzmax   = 1.0    # Maximum velocity in Z

    #========= Initialize ========
    random.seed(99999999)
    x  = np.empty(N, dtype=float)
    y  = np.empty(N, dtype=float)
    z  = np.empty(N, dtype=float)
    vx = np.empty(N, dtype=float)
    vy = np.empty(N, dtype=float)
    vz = np.empty(N, dtype=float)
    ux = np.empty(N, dtype=float)
    uy = np.empty(N, dtype=float)
    uz = np.empty(N, dtype=float)
    ax = np.empty(N, dtype=float)
    ay = np.empty(N, dtype=float)
    az = np.empty(N, dtype=float)

    svx  = 0.0  # velocity sum correction term in X
    svy  = 0.0  # velocity sum correction term in Y
    svz  = 0.0  # velocity sum correction term in Z

    ###### Initialize time array and data dump array ######
    time  = np.linspace(0,tmax,Nt)

    for i in range(N):
        x[i] = (random.random())*2.0*Lx - Lx
        y[i] = (random.random())*2.0*Ly - Ly
        z[i] = (random.random())*2.0*Lz - Lz
        vx[i] = (random.random())*Vxmax - Vxmax/2.0
        vy[i] = (random.random())*Vymax - Vymax/2.0
        vz[i] = (random.random())*Vzmax - Vzmax/2.0
        svx = svx + vx[i]
        svy = svy + vy[i]
        svz = svz + vz[i]

    for i in range(N):
        vx[i] = vx[i] - svx/N
        vy[i] = vy[i] - svy/N
        vz[i] = vz[i] - svz/N


    for i in range(N):
        ax[i] = 0.0
        ay[i] = 0.0
        az[i] = 0.0
        for j in range(N):
            if (i != j):
                xdiff = ( x[i]-x[j] ) - round((x[i]-x[j])/(2.0*Lx)) * 2.0*Lx
                ydiff = ( y[i]-y[j] ) - round((y[i]-y[j])/(2.0*Ly)) * 2.0*Ly
                zdiff = ( z[i]-z[j] ) - round((z[i]-z[j])/(2.0*Lz)) * 2.0*Lz
                r = math.sqrt(xdiff*xdiff + ydiff*ydiff + zdiff*zdiff)
                fx = xdiff/(r*r*r)
                fy = ydiff/(r*r*r)
                fz = zdiff/(r*r*r)
                ax[i] = ax[i] + fx
                ay[i] = ay[i] + fy
                az[i] = az[i] + fz

    #========= Time Loop =========

    for t in range(len(time)):
        for i in range(N):
            ux[i] = vx[i] + ax[i] * dt/2.0
            uy[i] = vy[i] + ay[i] * dt/2.0
            uz[i] = vz[i] + az[i] * dt/2.0
            x[i] = x[i] + ux[i] * dt
            y[i] = y[i] + uy[i] * dt
            z[i] = z[i] + uz[i] * dt
            x[i] = x[i] - (int(x[i]/Lx)) * 2.0 * Lx      # Periodic Boundary Condition
            y[i] = y[i] - (int(y[i]/Ly)) * 2.0 * Ly      # Periodic Boundary Condition
            z[i] = z[i] - (int(z[i]/Lz)) * 2.0 * Lz      # Periodic Boundary Condition

        for i in range(N):
            ax[i] = 0.0
            ay[i] = 0.0
            az[i] = 0.0
            for j in range(N):
                if (i != j):
                    xdiff = ( x[i]-x[j] ) - round((x[i]-x[j])/(2.0*Lx)) * 2.0*Lx
                    ydiff = ( y[i]-y[j] ) - round((y[i]-y[j])/(2.0*Ly)) * 2.0*Ly
                    zdiff = ( z[i]-z[j] ) - round((z[i]-z[j])/(2.0*Lz)) * 2.0*Lz
                    r = math.sqrt(xdiff*xdiff + ydiff*ydiff + zdiff*zdiff)
                    fx = xdiff/(r*r*r)
                    fy = ydiff/(r*r*r)
                    fz = zdiff/(r*r*r)
                    ax[i] += fx
                    ay[i] += fy
                    az[i] += fz

        for i in range(N):
            vx[i] = ux[i] + ax[i] * dt / 2.0
            vy[i] = uy[i] + ay[i] * dt / 2.0
            vz[i] = uz[i] + az[i] * dt / 2.0

        np.savetxt('data/time%04d'%t+'.txt', np.column_stack([x,y,z]))
        print("Timestep = %d"%t)

    #========== End of Time Loop ======

    return 0

if __name__== "__main__":
	start = time.time()
	main()
	end = time.time()
	print("Elapsed (after compilation) = %s"%(end - start)+" seconds")
