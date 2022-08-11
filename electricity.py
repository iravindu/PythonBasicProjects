units = float(input("Please enter your electricity units: "))

slab1_rate = 7.85 * (1+2.64)
slab2_rate = 10 * (1+2.11)
slab3_rate = 27.75 * (1+1.25)
slab4_rate = 27.75 * (1+0.89)
slab5_rate = 32
slab6_rate = 45

slab1 = 32 * slab1_rate
slab2 = 32 * slab2_rate
slab3 = 32 * slab3_rate
slab4 = 32 * slab4_rate
slab5 = 64 * slab5_rate

if int(units/32) > 6 :
    bill ="{:,}".format(slab1 + slab2 + slab3 + slab4 + slab5 + (units - 32*6) * slab6_rate)
    print("Your Bill Amount is : " +  str(bill))

if int(units/32) >= 4 and int(units/32) <= 6:
    bill = "{:,}".format(slab1 + slab2 + slab3 + slab4 + (units - 32*4)*slab5_rate)
    print("Your Bill Amount is : " +  str(bill))

if int(units/32) == 3:
    bill = "{:,}".format(slab1 + slab2 + slab3 + (units - 32*3)*slab4_rate)
    print("Your Bill Amount is : " +  str(bill))

if int(units/32) == 2:
    bill = "{:,}".format(slab1 + slab2 + (units - 32*2)*slab3_rate)
    print("Your Bill Amount is : " +  str(bill))

if int(units/32) == 1:
    bill = "{:,}".format(slab1 + (units - 32*1)*slab2_rate)
    print("Your Bill Amount is : " +  str(bill))

if int(units/32) == 0:
    bill = "{:,}".format(slab1_rate * units)
    print("Your Bill Amount is : " +  str(bill))
