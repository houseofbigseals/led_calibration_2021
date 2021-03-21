import pandas as pd
import numpy as np
import pylab as pl


def calculate_and_plot(path, name):
    names = ["IR", "IW", "FAR"]

    A1 = pd.read_csv(path + 'autoadjust_A1.csv', header=None, names=names)
    A2 = pd.read_csv(path + 'autoadjust_A2.csv', header=None, names=names)
    A3 = pd.read_csv(path + 'autoadjust_A3.csv', header=None, names=names)
    A4 = pd.read_csv(path + 'autoadjust_A4.csv', header=None, names=names)
    A5 = pd.read_csv(path + 'autoadjust_A5.csv', header=None, names=names)
    B1 = pd.read_csv(path + 'autoadjust_B1.csv', header=None, names=names)
    B2 = pd.read_csv(path + 'autoadjust_B2.csv', header=None, names=names)
    B3 = pd.read_csv(path + 'autoadjust_B3.csv', header=None, names=names)
    B4 = pd.read_csv(path + 'autoadjust_B4.csv', header=None, names=names)
    B5 = pd.read_csv(path + 'autoadjust_B5.csv', header=None, names=names)
    C1 = pd.read_csv(path + 'autoadjust_C1.csv', header=None, names=names)
    C2 = pd.read_csv(path + 'autoadjust_C2.csv', header=None, names=names)
    C3 = pd.read_csv(path + 'autoadjust_C3.csv', header=None, names=names)
    C4 = pd.read_csv(path + 'autoadjust_C4.csv', header=None, names=names)
    C5 = pd.read_csv(path + 'autoadjust_C5.csv', header=None, names=names)

    far_mean = ((A1['FAR'] + A2['FAR'] + A3['FAR'] + A4['FAR'] + A5['FAR']
                 + B1['FAR'] + B2['FAR'] + B3['FAR'] + B4['FAR'] + B5['FAR']
                 + C1['FAR'] + C2['FAR'] + C3['FAR'] + C4['FAR'] + C5['FAR'])) / 15

    far = np.array(far_mean)
    red = np.array(A1['IR'])
    white = np.array(A1['IW'])
    # a1 = np.array((A1['FAR'] + A2["FAR"])/2)
    print(np.shape(far))
    f = np.reshape(far, [7, 7])
    r = np.reshape(red, [7, 7])
    w = np.reshape(white, [7, 7])
    print(f[0][:])

    # 0
    # create new coordinates from old
    print("zero/2: ", far[0] / 2)
    zero = far[0]
    far_red = []
    far_white = []
    for i in range(0, len(red)):
        if red[i] == 10:
            far_white.append(far[i] - zero / 2)
        if white[i] == 10:
            far_red.append(far[i] - zero / 2)
    f_r = np.array(far_red)
    f_w = np.array(far_white)
    I = np.array([10, 50, 75, 100, 150, 200, 250])

    # numpy. numpy.polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)
    p_r = np.polyfit(x=I, y=f_r, deg=1)
    p_w = np.polyfit(x=I, y=f_w, deg=1)
    print("red = {}*Ired + {}".format(*p_r))
    print("white = {}*Iwhite + {}".format(*p_w))
    # print(p_w)

    rfit = np.polyval(p_r, I)
    wfit = np.polyval(p_w, I)

    # 2D plot of f_r and f_w by I with error
    fig = pl.figure()
    pl.plot(I, f_r, 'vr', label="Red FAR data")
    pl.plot(I, f_w, 'ob', label="White FAR data")

    pl.plot(I, rfit, '-r', label="Red lite intensity approximation")
    pl.plot(I, wfit, '-b', label="White lite intensity approximation")

    # pl.plot(I, rfit - f_r, '.g', label='Red approx error')
    # pl.plot(I, wfit - f_w, '.y', label='White approx error')
    print("red data{}".format(f_r))
    print("white data {}".format(f_w))
    print("red err {}".format(rfit - f_r))
    print("white err {}".format(wfit - f_w))

    pl.ylabel('FAR, mkmoles')
    pl.xlabel('I, mA')
    pl.title(name+"\nRed and white lite intensity by currents, and approximations")
    pl.legend(loc='upper left')
    pl.grid()
    pl.savefig("./reports/"+name)
    pl.show()


if __name__ == "__main__":
    calculate_and_plot(path="./data/exp_25cm/", name="2021_exp_25cm")
    calculate_and_plot(path="./data/exp_15cm/", name="2021_exp_15cm")
    calculate_and_plot(path="./data/control_25cm/", name="2021_control_25cm")
