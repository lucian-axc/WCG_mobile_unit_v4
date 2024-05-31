from app import app, db
from models import User, Device, Analysis, Spectrum, Chemical, Intensity, Shift

# USER
user = User(first_name = "Marcus", last_name = "Aurelius")
db.session.add(user)

# DEVICE
device = Device(name = "Light Novo MiniRaman spectrometer")
db.session.add(device)
    # device_2 = Device(name = "next spectro")
    # db.session.add(device_2)

# ANALYSIS
analysis_1 = Analysis(
    Device.query.get(1),
    "First analysis",
    "June 17 2024",
    "This analysis detected high amounts of PFAS compounds"
)

analysis_2 = Analysis(
    Device.query.get(1),
    "Second analysis",
    "June 21 2024",
    "This analysis detected low amounts of PFAS compounds"
)

db.session.add(analysis_1)
db.session.add(analysis_2)


# SPECTRUM
spectrum_1 = Spectrum(
    Analysis.query.get(1),
    Intensity.query.get(1),
    Shift.query.get(1)
)
spectrum_2 = Spectrum(
    Analysis.query.get(2),
    Intensity.query.get(2),
    Shift.query.get(2)
)

# CHEMICAL
chemical_1 = Chemical(
    Analysis.query.get(1),
    "PFAS compound X",
    "Concentration 0.01 ug/l"
)

# INTENSITY
intensities = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

for intensity in intensities:
    new_intensity = Intensity(intensity)
    db.session.add(new_intensity)

# SHIFT
shifts = [300, 350, 400, 450, 500]

for shift in shifts:
    new_shift = Shift(shift)
    db.session.add(new_shift)


# Delete all data in a table model
def delete_table_data(table):

    for device in table.query.all():
        db.session.delete(device)


# delete_table_data(Device)

db.session.commit()