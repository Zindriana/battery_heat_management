import random

# This program simulates a continuosly rising of the temperature of a battery during charging

# Battery: Tesla Model S/X Module - 5.3kWh / 232Ah / 22.8V
#T_battery(t) = T_ambient + R_int ⋅ I²(t) ⋅ Δt

T_ambient = 25  # Temperature in degrees Celsius
R_int = 0.03   # Resistance in Ohm
T_max = 45      # Maximal battery temperature in degrees Celsius before overheating
Δt = 1          # Time step in seconds
I = 1.625       # Amperes in standard operation

# Battery temperature before charging starts
T_battery = T_ambient

for time in range(0, 14400): # 4 hour charging simulation (the time it takes to charge the battery)
    T_battery += R_int * I**2 * Δt

    if time % 60 == 0:
        print("Battery temperature: ", T_battery, " at time: ", time)
        
    if T_battery > T_max:
        print("Warning: Critical temperature reached! Charging stopped.")
        print("Battery temperature: ", T_battery, " at time: ", time)
        break