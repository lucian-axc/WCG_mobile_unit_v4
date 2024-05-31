# from app import app, db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     first_name = db.Column(db.String(30), index = True)
#     last_name = db.Column(db.String(50), index = True)

# class Device(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     name = db.Column(db.String(100))
#     analyses = db.relationship('Analysis', backref = 'device',
#                                 lazy = 'dynamic', cascade = "all, delete, delete-orphan")

# class Analysis(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
#     name = db.Column(db.String(100), index = True)
#     date = db.Column(db.String(100), index = True)
#     comment = db.Column(db.String(100))
#     spectra = db.relationship('Spectrum', backref='analysis',
#                                 lazy = 'dynamic', cascade = "all, delete, delete-orphan")
#     chemicals = db.relationship('Chemical', backref='analysis',
#                                 lazy = 'dynamic', cascade = "all, delete, delete-orphan")

# class Spectrum(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     analysis_id = db.Column(db.Integer, db.ForeignKey('analysis.id'))
#     intensity = db.Column(db.Float, db.ForeignKey('intensity.value'))
#     shift = db.Column(db.Integer, db.ForeignKey('shift.value'))

# class Chemical(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     analysis_id = db.Column(db.Integer, db.ForeignKey('analysis.id'))
#     substance = db.Column(db.String(200), index = True)
#     concentration = db.Column(db.String(200), index = True)

# class Intensity(db.Model):
#     value = db.Column(db.Float, primary_key = True)
#     spectra = db.relationship('Spectrum', backref='spectrum_intensity',
#                                 lazy = 'dynamic', cascade = "all, delete, delete-orphan")

# class Shift(db.Model):
#     value = db.Column(db.Integer, primary_key = True)
#     spectra = db.relationship('Spectrum', backref='spectrum_shift',
#                                 lazy = 'dynamic', cascade = "all, delete, delete-orphan")



# app.app_context().push()
# db.create_all()