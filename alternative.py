# This program simulates a charging of a battery with the risk of something goes wrong with the charging

import random

# Battery: Tesla Model S/X Module - 5.3kWh / 232Ah / 22.8V
# T_battery(t) = T_ambient + R_int ⋅ I²(t) ⋅ Δt

T_ambient = 25  # Temperature in degrees Celsius
R_int = 0.05    # Resistance in Ohm
T_max = 45      # Maximal battery temperature in degrees Celsius before overheating
#Δt = 1          # Time step in seconds
I = 1.625       # Amperes in standard operation

# Battery temperature before charging starts
T_battery = T_ambient

# a randomiser function to simulate a failure in the battery
def I_failure():
        if random.randint(1, 50) == 1:
            return 1
        else:
            return 0


def charging_with_failrisk():
    print()
    for time in range(0, 14400): # 4 hour charging simulation (the time it takes to charge the battery)
        I_current = I + I_failure()
        T_battery = T_ambient + R_int * I_current**2 * time
        if time % 60 == 0:
            print("Battery temperature: {:.2f} at time: {} minutes".format(T_battery, time/60))
        
        if T_battery > T_max:
            print()
            print("Warning: Critical temperature reached! Charging stopped.")
            print("Battery temperature: {:.2f} at time: {} minutes".format(T_battery, time/60))
            print()
            break

charging_with_failrisk()