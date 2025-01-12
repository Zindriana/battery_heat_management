# This program simulates a continuosly rising of the temperature of a battery during charging

# Battery: Tesla Model S/X Module - 5.3kWh / 232Ah / 22.8V
#T_battery(t) = T_ambient + R_int ⋅ I²(t) ⋅ Δt

T_ambient = 25  # Temperature in degrees Celsius
R_int = 0.005   # Resistance in Ohm
T_max = 45      # Maximal battery temperature in degrees Celsius before overheating
#Δt = 1          # Time step in seconds
I = 1.625       # Amperes in standard operation


def main():
    for time in range(0, 14400): # 4 hour charging simulation (the time it takes to charge the battery)
        T_battery = T_ambient + R_int * I**2 * time

        if time % 60 == 0:
            print("Battery temperature: {:.2f} at time: {} minutes".format(T_battery, time/60))
            
        if T_battery > T_max:
            print()
            print("Warning: Critical temperature reached! Charging stopped.")
            print("Battery temperature: {:.2f} at time: {} minutes".format(T_battery, time/60))
            print()
            break

if __name__ == "__main__":
    main()