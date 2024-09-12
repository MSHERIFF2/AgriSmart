from app  import db

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    market_price = db.relationship("MarketPrice", backref='crop', lazy=True)

    def __repr__(self):
       return f'<Crop {self.name}>'

class Livestock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    market_price = db.relationship('MarketPrice', backref='livestock', lazy=True)

    def __repr__(self):
        return f'<Livestock {self.name}>'

class MarketPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_id = db.Column(db.Integer, db.ForeignKey('crop.id'))
    livestock_id = db.Column(db.Integer, db.ForeignKey('livestock.id'))
    price = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<MarketPrice {self.price} on {self.date}>'

class FarmingTip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<FarmingTip {self.title}>'

class WeatherForecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forecast_date = db.Column(db.Date, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    condition = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<WeatherForecast {self.forecast_date} - {self.condition}>'

