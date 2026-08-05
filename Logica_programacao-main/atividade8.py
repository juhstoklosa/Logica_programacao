times = [
    ["FURIA", "CS2",               "320"],
    ["LOUD",  "Valorant",          "410"],
    ["paiN",  "League of Legends", "280"],
    ["NIP",   "CS2",               "390"]
]
for lin in range(len(times)):
    for col in range(len(times[lin])):
        print(f"• {times[lin][col]}")