import pandas as pd
# 1. Base Farmer Registry (12 farmers across 3 zones)

farmer_detail = pd.DataFrame({
    "farmer_name": ["mathew warutere", "Simon Kamau", "Purity Wangeshi", "Marion Mugechi", "Harrison Njoroge", "Phoeb Mugure", "James Mbugua", "Timothy Kariuki", "Christopher Mwathi", "Paphael Nanjala", "Emaniel Karimi", "Joyce Mumbi"],
    "zone": ["Bahati", "Njoro", "Bahati", "Molo", "Njoro", "Bahati", "Molo", "Bahati", "Njoro", "Molo", "Bahati", "Molo"],
    "rate_per_ltr": [45, 47, 45, 60, 47, 45, 60, 45, 47, 60, 45, 60]
})

# 2. Assign specific manual monthly litres to each farmer in order
farmer_detail["supplied_litres"] = [450.4, 367.7, 400.2, 670.8, 232.1, 120.7, 900.3, 640.5, 234.6, 98.8, 240.3, 365.6]

# 3.Process Financials
farmer_detail["payout"] = farmer_detail["supplied_litres"] * farmer_detail["rate_per_ltr"]

# 4. Generate Zone Aggregations
zone_totals = farmer_detail.groupby("zone").agg(
    total_litres=("supplied_litres", "sum"),
    total_payout=("payout", "sum")
).reset_index()

# 5. Extracting Top Farmer per Zone based on provided figures
sorted = farmer_detail.sort_values(by=["supplied_litres", "farmer_name"], ascending=[False, True])
top_farmer = sorted.groupby("zone").first().reset_index()[["zone", "farmer_name"]]
top_farmer.rename(columns={"farmer_name": "top_farmer"}, inplace=True)

# 6. Combining Elements & Format Presentation View
summary_table = pd.merge(zone_totals, top_farmer, on="zone")
summary_table["total_litres"] = summary_table["total_litres"].map("{:,.1f} L".format)
summary_table["total_payout"] = summary_table["total_payout"].map("KES{:,.2f}".format)

summary_table.columns = ["zone", "total litres", "total_payout", "top_farmer"]
summary_table.set_index("zone", inplace=True)

print("\n===============FINAL END MONTH SUMMARY===============")
print(summary_table.to_string())
print("======================================================\n")