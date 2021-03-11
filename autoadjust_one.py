import pandas as pd
import numpy as np
from led_uart_wrapper import UartWrapper
from time import sleep
import csv

def set_current(wrapper, red, white):
    print(wrapper.STOP()[1])
    print(wrapper.START_CONFIGURE()[1])
    print(wrapper.SET_CURRENT(0, red)[1])
    print(wrapper.SET_CURRENT(1, white)[1])
    print(wrapper.FINISH_CONFIGURE_WITH_SAVING()[1])
    print(wrapper.START()[1])

def read_loop():
    #A1 = pd.read_excel('Stend_autoadjust.xlsx', sheet_name='A3')
    #red = np.array(A1['IR'])
    #white = np.array(A1['IW'])

    # red = np.array([10, 10, 10, 10, 10, 10, 10, 50, 50, 50, 50, 50, 50, 50,
    #                 75, 75, 75, 75, 75, 75, 75, 100, 100, 100, 100, 100, 100, 100,
    #                  150, 150, 150, 150, 150, 150, 150,
    #                  200, 200, 200, 200, 200, 200, 200,
    #                  250, 250, 250, 250, 250, 250, 250
    #                 ])
    # white = np.array([
    #     10, 50, 75, 100, 150, 200, 250, 10, 50, 75, 100, 150, 200, 250,
    #     10, 50, 75, 100, 150, 200, 250, 10, 50, 75, 100, 150, 200, 250,
    #     10, 50, 75, 100, 150, 200, 250, 10, 50, 75, 100, 150, 200, 250,
    #     10, 50, 75, 100, 150, 200, 250
    # ])

    wrapper = UartWrapper(
    )

    print("A1 A2 A3 A4 A5\n"
        "B1	B2 B3 B4 B5\n"
        "C1	C2 C3 C4 C5\n"
    )
    name = input("Enter a position as {A, B, C} and number {1-5}: ")
    red = [int(input("Enter red current: "))]
    white = [int(input("Enter white current: "))]
    datafile = "autoadjust_{}.csv".format(name)

    for i in range(len(red)):

        red_ = int(red[i])
        white_ = int(white[i])

        set_current(wrapper, red_, white_)

        print("current red {} white {}".format(red_, white_))

        far_done = False
        while not far_done:
            try:
                far = float(input("Print far: "))
                far_done = True
            except Exception as e:
                print("error : {}, try input far again again")

        data = {
            "Ired": red_,
            "Iwhite": white_,
            "Far": far
        }

        fieldnames = ["Ired", "Iwhite", "Far"]

        with open(datafile, "a", newline='') as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
            writer.writerow(data)

if __name__ == "__main__":
    read_loop()