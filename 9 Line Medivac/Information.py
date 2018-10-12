"""
This is the 9-line medivac for the U.S Armed forces.
Developed by Kevin Lee

Line 1: Location of pick-up site.

Line 2; Radio frequency, call sign, and suffix

Line 3: Number of patients by procedence

Line 4: Special equipment required

Line 5. Number of patients

Line 6: Security pick-up site

Line 7: Method of marking pick-up site:

Line 8: Patient nationality and status

Line 9: NBC Contamination


Further ideas;

Dial up internet- track the ip address to find the geo location 

"""

import datetime
import _socket


# s = socket.socket(socket.AF_INET, socket.sock_DGRAM)
# s.connect("8.8.8.8",80)
IP = _socket.gethostbyname(_socket.gethostname())

class medivac():
    def __init__(self):
        self.date= datetime.datetime.now()
        self.ip_address =IP

    def __repr__(self):
        raise NotImplementedError


class ninelines(medivac):
    """
            This initializes the 9 lines of medivac
            :param line_1: Location of the pick-up site.
            :param line_2: Radio frequency, call sign, and suffix.
            :param line_3: Number of patients by precedence
                A – Urgent
                B – Urgent Surgical
                C – Priority
                D – Routine
                E – Convenience
            :param line_4: Special equipment required
                A – None
                B – Hoist
                C – Extraction equipment
                D – Ventilator
            :param line_5: Number of patients
                A – Litter
                B – Ambulatory
            :param line_6: Security at pick-up site
                N – No enemy troops in area
                P – Possible enemy troops in area (approach with caution)
                E – Enemy troops in area (approach with caution)
                X – Enemy troops in area (armed escort required)
                * In peacetime – number and types of wounds, injuries, and illnesses
            :param line_7: Method of marking pick-up site
                A – Panels
                B – Pyrotechnic signal
                C – Smoke signal
                D – None
                E – Other
            :param line_8: Patient nationality and status
                A – US Military
                B – US Civilian
                C – Non-US Military
                D – Non-US Civilian
                E – EPW
            :param line_9: NBC Contamination
                N – Nuclear
                B – Biological
                C – Chemical
                * In peacetime – terrain description of pick-up site
            :return: .txt file with all the information

            """
    def __int__(self, line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9):

        self.date = datetime.datetime.now()
        self.ip_address = IP
        self.location = line_1
        self.frequency = line_2
        self.urgentness = line_3
        self.special_equipment = line_4
        self.casualties = line_5
        self.pick_up_site = line_6
        self.method_of_pick_up = line_7
        self.nationality = line_8
        self.NBC_contamination = line_9

    def output(self):
        f =open("Output.txt", "w")
        general_info = [f"Date: {self.date}\n",
                        f"IP address: {self.ip_address}\n,"
                        f"Location: {str(self.location)},\n"
                        f""]
        f.write(f"Date: {self.date}\n")
        f.close()



import sys
import os
sys.path.append(os.path.abspath("/USERS/klee17/desktop/9-line Medivac"))
from Information import *


def main():

    userLine_1=  input("Enter Line 1: ")
    userLine_2 = input("Enter Line 2: ")
    userLine_3 = input("Enter Line 3: ")
    userLine_4 = input("Enter Line 4: ")
    userLine_5 = input("Enter Line 5: ")
    userLine_6 = input("Enter Line 6: ")
    userLine_7 = input("Enter Line 7: ")
    userLine_8 = input("Enter Line 8: ")
    userLine_9 = input("Enter Line 9: ")
    driver = ninelines()

    driver.output()


if __name__ == "__main__":
    main()
