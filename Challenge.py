# written in Python 3.9.1
#
# Copyright (c) 2021 Christoph Schwalbe
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#
# Task is to solve a challenge with two logistical storage transporter.
#
#
# Transporter1 = Driver1 + Cargo
# Transporter2 = Driver2 + Cargo
# Cargo is a fixed table with elements
# Each Transporter can only transport 1100 kg or 1100000 g including driver + cargo
#
import sys
#
# global vars
CARGO_LIMIT = 1100000
DRIVER1 = 72400 # in g = 72,4 kg
DRIVER2 = 85700 # in g = 85,7 kg
TRANSPORT1 = CARGO_LIMIT - DRIVER1
TRANSPORT2 = CARGO_LIMIT - DRIVER2
CURRENT_CARGOSPACE_LEFT = 0

# Main Task:
# Was ist die optimale Beladung (Summe der Nutzwerte),
# wenn die beiden Transporter jeweils einmal fahren können?
# Erstelle einen Algorithmus,
# der die bestmögliche Ladeliste für jeden der beiden Transporter ermittelt.


# dictionary
data = { '1': ["Notebook indoor 13", 205, 2451, 40],
         '2': ["Notebook indoor 14", 420, 2978, 35],
         '3': ["Notebook outdoor", 450, 3625, 80],
         '4': ["Mobile P. indoor", 60, 717, 30],
         '5': ["Mobile P. outdoor", 157, 988, 60],
         '6': ["Mobile P. heavy duty", 220, 1220, 65],
         '7': ["Tablet indoor little", 620, 1220, 40],
         '8': ["Tablet indoor big", 250, 1405, 40],
         '9': ["Tablet outdoor little", 540, 1690, 45],
        '10': ["Tablet outdoor big", 370, 1980, 68]
    }

#
#
#
def myerror(text):
    print(text)
    sys.exit(1)

def showTable(d):
    print("{:<4} {:<22} {:<12} {:<6} {:<6}".format('Key', 'Hardware','Req. Units','Weight', 'Priority'))
    for k, v in d.items():
        label, units, weight, prio = v
        print("{:<4} {:<22} {:<12} {:<6} {:<6}".format(k, label, units, weight, prio))

def checkfreespace(units, weight, free_cargospace):
    check_weight = units * weight
    if check_weight <= free_cargospace:
        # nice, take complete cargo
        #print("here units {} weight {} and cargo {}".format(units, weight, units*weight))
        return True
    elif check_weight > free_cargospace:
        # split cargo
        return False

def iterativ_consumer(units, weight, free_cargospace):
    consume = { 'units': 0, 'status': "none"}
    if free_cargospace == 0:
        consume['status'] = "full"
        return consume
    if checkfreespace(units, weight, free_cargospace) == False:
            # handle split
            #print("[-] split cargo")
            consume['units'] = int(free_cargospace / weight)
            consume['status'] = "split"
    elif checkfreespace(units, weight, free_cargospace) == True:
            # consume freespace 
            # and set units in original data source to 0
            # and append dict with data to delivery dict
            #print("[+] fetch all units")
            consume['units'] = units
            consume['status'] = "all"
    else:
            myerror("Program has received invalid data")
    return consume

def calcWeight(units, weight, free_cargospace):
    if units > 0:
      cargo = units * weight
      free_cargospace = free_cargospace - cargo
    return free_cargospace

def isCargoEmpty(d):
    all_units_zero = True
    for k, v in d.items():
        label, units, weight, prio = v
        if units != 0:
            all_units_zero = False
    return all_units_zero
#
# dummy
#
def checkStatus(status, data):
    cargosetup = {}
    if status == "full":
        # Transporter is full or has near 0 space left
        pass
    elif status == "split":
        # add splited cargo to cargosetup
        # and set units in original data source to units
        # and append dict with data to delivery dict
        pass
    elif status == "all":
        # add all cargo to cargosetup
        # and set units in original data source to 0
        # and append dict with data to delivery dict
        pass
    else:
        myerror("This status is currently not supported.")
#
# dummy
#

# this function goes through all data and consume units
def packageCargo(d, c):
    """
    d := data dictionary
    c := CURRENT_CARGOSPACE_LEFT
    """
    cargosetup = { }
    if c < 0:
        myerror("no free CURRENT_CARGOSPACE_LEFT")

    for elem, data in d.items():
        #print(data)
        takenUnits = iterativ_consumer(data[1],data[2], c)
        c = calcWeight(takenUnits['units'], data[2], c)
        
        if takenUnits['status'] == "all":
            # add all cargo to cargosetup
            # and set units in original data source to 0
            # and append dict with data to delivery dict
            data[1] = 0
            mydict = { elem: data }            
            cargosetup.update(mydict)
            
        elif takenUnits['status'] == "split":
            # add splited cargo to cargosetup
            # and set units in original data source to units
            # and append dict with data to delivery dict
            data[1] = data[1] - takenUnits['units']
            mydict = { elem: [data[0], takenUnits['units'] , data[2], data[3]]}
            cargosetup.update(mydict)
    #showTable(cargosetup)
    #print("\nCargo left:")
    #showTable(d)

    # writeback
    sorted_data = d

    return cargosetup

#
if __name__ == "__main__":
        
    print("Unsorted:")
    showTable(data)
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1][3], reverse=True))
    print("\nSorted:")
    showTable(sorted_data)
    print("Capacity1: {}".format(TRANSPORT1))
    print("Capacity2: {}".format(TRANSPORT2))

    car1 = packageCargo(sorted_data, TRANSPORT1)
    car2 = packageCargo(sorted_data, TRANSPORT2)


    print("\nCargosetup1:")
    showTable(car1)
    print("\nCargosetup2:")
    showTable(car2)

    print("\nCargo left:")
    showTable(sorted_data)

    print("\n\n=== Challenge Ends now ===\n\nBonus")


    #408.925 - (370*1980) --> execced
    #408.925 / 1980 = 206

#
#  Bonus
#
    extra_drives = 0
    i = 0
    while isCargoEmpty(sorted_data) == False:
      if i % 2 == 1:
          packageCargo(sorted_data, 1027600)
          #showTable( packageCargo(sorted_data, 1027600) )
          extra_drives = extra_drives + 1
      elif i % 2 == 0:
          packageCargo(sorted_data, 1014300)
          #showTable( packageCargo(sorted_data, 1014300) )
          extra_drives = extra_drives + 1
      i = i + 1
    print("\nEmpty cargo")
    showTable(sorted_data)
    print("Extra rounds needed to transport everything: {}".format(extra_drives))
          
    
# TODO: drivers have to make sport and eat healthy and please don't become fat
#       make modular software
#       add logging
#       add pandas and DB support
#       seperate datamodell in one class
#       seperate data reader in one class
#       outsource helper functions
#       seperate view/main in one class/file
