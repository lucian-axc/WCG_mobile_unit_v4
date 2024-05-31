import random

user_s = {
    "id": 1,
    "first_name": "Marcus",
    "last_name": "Aurelius"
}

device_s = {
    "id": 1,
    "user_id": user_s["id"],
    "name": "Light Novo MiniRaman spectrometer",
}

intensities_s = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
shifts = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]

spectrum_s_analysis_1 = [ (random.choice(intensities_s), shift) for shift in shifts ]
spectrum_s_analysis_2 = [ (random.choice(intensities_s), shift) for shift in shifts ]

chemical_s_1 = {
    "id": 1,
    "substance": "perfluorinated carboxylic acid",
    "concentration": "0.01 ug/l"
}

chemical_s_2 = {
    "id": 2,
    "substance": "sulfonic acid",
    "concentration": "0.00005 ug/l"
}

analysis_s_1 = {
    "id": 1,
    "device_id": device_s["id"],
    "name": "First analysis",
    "date": "June 17 2024",
    "comment": "This analysis detected high amounts of PFAS compounds",
    "spectra": spectrum_s_analysis_1,
    "chemicals": chemical_s_1
}

analysis_s_2 = {
    "id": 2,
    "device_id": device_s["id"],
    "name": "Second analysis",
    "date": "June 21 2024",
    "comment": "This analysis detected low amounts of PFAS compounds",
    "spectra": spectrum_s_analysis_2,
    "chemicals": chemical_s_2
}
