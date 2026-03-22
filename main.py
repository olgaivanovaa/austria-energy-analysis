from energy_analysis import load_data, total_consumption, renewable_share, plot_energy_mix

print("=" * 50)
print("       Austria Energy Analysis")
print("=" * 50)

df = load_data("data/austria_energy.csv")
print("Data loaded successfully! Years covered: 2004-2024")

print("\n--- Total Energy Consumption ---")
print(f"2020: {total_consumption(df, 2020)} TWh")
print(f"2022: {total_consumption(df, 2022)} TWh")
print(f"2023: {total_consumption(df, 2023)} TWh")

print("\n--- Renewable Energy Share ---")
print(f"2020: {renewable_share(df, 2020) * 100:.1f}%")
print(f"2022: {renewable_share(df, 2022) * 100:.1f}%")
print(f"2023: {renewable_share(df, 2023) * 100:.1f}%")

print("\n--- Energy Mix Chart ---")
print("Showing chart for 2023...")
plot_energy_mix(df, 2023)