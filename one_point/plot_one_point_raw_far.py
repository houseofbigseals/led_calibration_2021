import pandas as pd
import numpy as np
import pylab as pl
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import cm
from scipy import interpolate

def main():
    # A1 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='A1')
    # A2 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='A2')
    # A3 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='A3')
    # A4 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='A4')
    # A5 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='A5')
    # B1 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='B1')
    # B2 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='B2')
    # B3 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='B3')
    # B4 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='B4')
    # B5 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='B5')
    # C1 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='C1')
    # C2 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='C2')
    # C3 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='C3')
    # C4 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='C4')
    # C5 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='C5')

    names = ["IR", "IW", "FAR"]

    A1 = pd.read_csv('autoadjust_A1.csv', header=None, names=names)
    A2 = pd.read_csv('autoadjust_A2.csv', header=None, names=names)
    A3 = pd.read_csv('autoadjust_A3.csv', header=None, names=names)
    A4 = pd.read_csv('autoadjust_A4.csv', header=None, names=names)
    A5 = pd.read_csv('autoadjust_A5.csv', header=None, names=names)
    B1 = pd.read_csv('autoadjust_B1.csv', header=None, names=names)
    B2 = pd.read_csv('autoadjust_B2.csv', header=None, names=names)
    B3 = pd.read_csv('autoadjust_B3.csv', header=None, names=names)
    B4 = pd.read_csv('autoadjust_B4.csv', header=None, names=names)
    B5 = pd.read_csv('autoadjust_B5.csv', header=None, names=names)
    C1 = pd.read_csv('autoadjust_C1.csv', header=None, names=names)
    C2 = pd.read_csv('autoadjust_C2.csv', header=None, names=names)
    C3 = pd.read_csv('autoadjust_C3.csv', header=None, names=names)
    C4 = pd.read_csv('autoadjust_C4.csv', header=None, names=names)
    C5 = pd.read_csv('autoadjust_C5.csv', header=None, names=names)

    far_mean = (A1['FAR'] + A2['FAR'] + A3['FAR'] + A4['FAR'] + A5['FAR']
               + B1['FAR'] + B2['FAR'] + B3['FAR'] + B4['FAR'] + B5['FAR']
               + C1['FAR'] + C2['FAR'] + C3['FAR'] + C4['FAR'] + C5['FAR'])/15

    far = np.array(far_mean)
    red = np.array(A1['IR'])
    white = np.array(A1['IW'])
    # a1 = np.array((A1['FAR'] + A2["FAR"])/2)
    print(np.shape(far))
    f = np.reshape(far, [7, 7])
    r = np.reshape(red, [7, 7])
    w = np.reshape(white, [7, 7])
    print(f[0][:])

    # # 1
    # # just raw data visualization FAR (I_red, I_white)
    # fig = pl.figure()
    # ax = p3.Axes3D(fig)
    # cs = ax.plot_surface(r, w, f, rstride=1, cstride=1, color='g', cmap=cm.coolwarm)
    # pl.clabel(cs, fmt='%.1f', colors="black")
    # fig.colorbar(cs, shrink=0.5, aspect=5)
    # ax.set_ylabel('R, mA')
    # ax.set_xlabel('W, mA')
    # ax.set_zlabel('FAR, mkmoles')
    # ax.set_title('Hehe')
    # pl.grid()
    # # pl.savefig("gradient_metaopt_5678676787656765456765.png")
    # pl.show()


    # 2
    # interpolation
    # real points (measured current values)
    xr_old = [10, 50, 75, 100, 150, 200, 250]
    yw_old = xr_old
    f1 = interpolate.interp2d(xr_old, yw_old, f.T, kind='cubic')
    # points for interpolate
    xr = np.arange(10, 250, 1)
    yw = np.arange(10, 250, 1)
    xx_new, yy_new = np.meshgrid(xr, yw, indexing='ij')
    interp = f1(xr, yw)

    fig = pl.figure()
    ax = p3.Axes3D(fig)
    cs = ax.plot_surface(xx_new, yy_new, interp, cmap=cm.coolwarm)
        # ,
        #                  rstride=1, cstride=1, color='g', cmap=cm.coolwarm)
    pl.clabel(cs, fmt='%.1f')#, colors="black")
    fig.colorbar(cs, shrink=0.5, aspect=5)
    ax.set_ylabel('Red, mA')
    ax.set_xlabel('White, mA')
    ax.set_zlabel('FAR, mkmoles')
    ax.set_title('Interpolated total lite intensity by currents \n on red and white leds')
    # pl.grid()
    # pl.savefig("gradient_metaopt_5678676787656765456765.png")
    pl.show()

    # 3
    # surface on (i1, i2) by all points
    ir = 200
    iw = 200
    # 200 200  -  on the row 41
    addr = 41
    # fake x and y - extended
    x_fake = np.array([0, 4, 12, 20, 24])  # cm
    y_fake = np.array([0, 4, 10, 20, 30, 40, 44])  # cm
    mx_fake, my_fake = np.meshgrid(x_fake, y_fake, indexing='ij')

    # _ 0 1 2 3 4 5 6
    # A
    #
    # B
    #
    # C

    # edge_coefficient
    ef = 130
    a1 = A1['FAR'][addr]
    a2 = A2['FAR'][addr]
    a3 = A3['FAR'][addr]
    a4 = A4['FAR'][addr]
    a5 = A5['FAR'][addr]
    b1 = B1['FAR'][addr]
    b2 = B2['FAR'][addr]
    b3 = B3['FAR'][addr]
    b4 = B4['FAR'][addr]
    b5 = B5['FAR'][addr]
    c1 = B1['FAR'][addr]
    c2 = B2['FAR'][addr]
    c3 = B3['FAR'][addr]
    c4 = B4['FAR'][addr]
    c5 = B5['FAR'][addr]

    ext_array = np.array([
        [ef, a1, a2, a3, a4, a5, ef],
        [ef, (a1+b1)/2, (a2+b2)/2, (a3+b3)/2, (a4+b4)/2, (a5+b5)/2, ef],
        [ef, b1, b2, b3, b4, b5, ef],
        [ef, (c1+b1)/2, (c2+b2)/2, (c3+b3)/2, (c4+b4)/2, (c5+b5)/2, ef],
        [ef, c1, c2, c3, c4, c5, ef]
    ])

    # create interpolation
    print(np.shape(x_fake))
    print(np.shape(y_fake))
    print(np.shape(ext_array))
    f1 = interpolate.interp2d(x_fake, y_fake, ext_array.T, kind='cubic')

    # points for interpolate
    xr = np.arange(0, 24, 0.3)
    yw = np.arange(0, 44, 0.3)
    xx_new, yy_new = np.meshgrid(xr, yw, indexing='ij')
    interp = f1(xr, yw)
    print(np.shape(xx_new))
    print(np.shape(yy_new))
    print(np.shape(interp))

    fig = pl.figure()
    ax = p3.Axes3D(fig)
    cs = ax.plot_surface(xx_new, yy_new, interp.T, cmap=cm.coolwarm)
    pl.clabel(cs, fmt='%.1f')
    # fig.colorbar(cs, shrink=0.5, aspect=5)
    ax.set_ylabel('x, cm')
    ax.set_xlabel('y, cm')
    ax.set_zlabel('FAR, mkmoles')
    ax.set_title('Interpolated total lite intensity by currents \n on Ir = 200 and Iw = 200')
    # pl.grid()
    # pl.savefig("gradient_metaopt_5678676787656765456765.png")
    pl.show()


if __name__ == "__main__":
    main()