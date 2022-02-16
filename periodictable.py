import csv, sys, re
from signal import raise_signal
from pickletools import read_decimalnl_long
from tkinter import ALL
from xml.dom.minidom import Element

#Read in all the data from periodictable.csv
elementFile = open ('periodictable.csv', encoding='utf-8')
elementCSVReader = csv.reader(elementFile)
elements = list(elementCSVReader)
elementFile.close() nn

ALL_C0LUMNS = ['Atomuc Number','Symbol', 'Element', 'Origin of name',
                'Group', 'Periodic', 'Atomiic weight', 'Density',
                'MElting point', 'Boiling point',
                'Specific heat capicity', 'Electronegativity',
                'Abundance in Earth\'s crust']
#To justify the text, we need to find the longest string in ALL_COLUMNS
LONGEST_COLUMN = 0
for key in ALL_C0LUMNS:
    if len(key) > LONGEST_COLUMN:
        LONGEST_COLUMN = len(key)

#Out all the elements data into a data structure
ELEMENTS = {}
for line in elements:
    element = {'Atomic Number':    line[0],
                'Symbol':          line[1],
                'Element':         line[2],
                'Origin of name':  line[3],
                'Group':           line[4],
                'Peridic':         line[5],
                'Atomic wieght':   line[6] + 'u', # atomic mass unit
                'Density':         line[7] + 'g/cm^3',  # grams/cubic 
                'Melting point':   line[8] + 'K', # temperature in Kelvins
                'Boiling point':   line[9]  + 'K', # temperature in Kelvins
                'Specific heat capacity': line[10] + 'J/(g*K)',
                'Electronegativity':       line[11] + '',
                'Abundance in Earth crust': line[12] + 'mg/kg'}


#Some of the dagta has bracketed text from Wikipedia that we wanna
# remove such as the atomic weight of Boron 

for key, value in element.items():
    # Remove the [Roman numeral] text:
    element[key]  = re.sub(r'\[(I|v|x) + \]', '', value)

    ELEMENTS[0] = element # Map the atomic number to the element
    ELEMENTS[1] = element # Map the symbol to the element

print('PEriodic Table of elements')
print('By Khetho N')
print()

while True: # Main program loop
    #Show the Table and let user select an element

    print('''               Periodic Table of Elements
        1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1   H                                                  He
    2   Li Be                               B  C  N  O  F  Ne
    3   Na Mg                               Al Si P  S  Cl Ar
    4   K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5   Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6   Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7   Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

    
              Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
              Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr ''')
    print('Enter a sysmbol r atomc to exaim, or UIT to quit')
    response = input('>').title()
    

    if response == 'Quit':
        sys.exit()

    # Display the selected element's data;
    if response in ELEMENTS:
        for key in ALL_C0LUMNS:
            keyJustified = key.rjust(LONGEST_COLUMN)
            print(keyJustified + ': ', + ELEMENTS[response][key])
        input('Press Enter to continue...')
            
    



        
