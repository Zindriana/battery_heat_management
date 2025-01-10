

T_ambient = 25          # Temperature in degrees Celsius
R_int = 0.002           # Resistance in Ohm
T_max = 45              # Maximal battery temperature in degrees Celsius before overheating
Δt = 1                  # Time step in seconds
I_standard = 225        # Amperes in standard operation

# Start temperature
T_battery = T_ambient

for time_step in range(0, 3600, Δt):
    temperature_increase = R_int * I_standard**2 * Δt
    T_battery += temperature_increase
    
    if T_battery > T_max:
        print("Varning: Batteritemperaturen är för hög!")
        print("Batteritemperaturen är: ", T_battery, " vid tiden: ", time_step)
        break





