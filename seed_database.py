# seed/seed_database.py

from app import app, db
from app.models import Crop, Livestock, MarketPrice, FarmingTip, WeatherForecast
from datetime import date

# Create an application context
with app.app_context():
    # Clear existing data
    try:
        MarketPrice.query.delete()
        Crop.query.delete()
        Livestock.query.delete()
        FarmingTip.query.delete()
        WeatherForecast.query.delete()
        db.session.commit()
        print("Existing data cleared.")
    except Exception as e:
        db.session.rollback()
        print(f"Error clearing data: {e}")

    # Sample data
    crops = [
        Crop(name='Maize'),
        Crop(name='Cassava'),
        Crop(name='Yam'),
        Crop(name='Rice'),
        Crop(name='Groundnut'),
        Crop(name='Palm Oil'),
        Crop(name='Sorghum'),
        Crop(name='Millet'),
        Crop(name='Cocoa'),
        Crop(name='Tomato'),
        Crop(name='Pepper'),
        Crop(name='Soybeans'),
        Crop(name='Okra'),
        Crop(name='Plantain'),
        Crop(name='Cucumber'),
        Crop(name='Sweet Potato'),
        Crop(name='Pineapple'),
        Crop(name='Banana'),
        Crop(name='Onion'),
        Crop(name='Sugarcane')
    ]

    livestock = [
        Livestock(name='Goat'),
        Livestock(name='Cattle'),
        Livestock(name='Chicken'),
        Livestock(name='Sheep'),
        Livestock(name='Pig'),
        Livestock(name='Snail'),
        Livestock(name='Fish'),
        Livestock(name='Rabbit'),
        Livestock(name='Turkey'),
        Livestock(name='Duck')
    ]

    # Use the current date for market prices and farming tips
    current_date = date.today()

    # Complete sample market prices
    market_prices = [
        MarketPrice(crop_id=1, price=88000, date=current_date),  # Maize
        MarketPrice(crop_id=2, price=100000, date=current_date),  # Cassava
        MarketPrice(crop_id=3, price=200000, date=current_date),  # Yam
        MarketPrice(crop_id=4, price=100000, date=current_date),  # Rice
        MarketPrice(crop_id=5, price=50000, date=current_date),  # Groundnut
        MarketPrice(crop_id=6, price=70000, date=current_date),  # Palm Oil
        MarketPrice(crop_id=7, price=80000, date=current_date),  # Sorghum
        MarketPrice(crop_id=8, price=70000, date=current_date),  # Millet
        MarketPrice(crop_id=9, price=70000, date=current_date),  # Cocoa
        MarketPrice(crop_id=10, price=150000, date=current_date), # Tomato
        MarketPrice(crop_id=11, price=100000, date=current_date), # Pepper
        MarketPrice(crop_id=12, price=180000, date=current_date), # Soybeans
        MarketPrice(crop_id=13, price=60000, date=current_date),  # Okra
        MarketPrice(crop_id=14, price=250000, date=current_date), # Plantain
        MarketPrice(crop_id=15, price=100000, date=current_date), # Cucumber
        MarketPrice(crop_id=16, price=90000, date=current_date),  # Sweet Potato
        MarketPrice(crop_id=17, price=220000, date=current_date), # Pineapple
        MarketPrice(crop_id=18, price=180000, date=current_date), # Banana
        MarketPrice(crop_id=19, price=80000, date=current_date),  # Onion
        MarketPrice(crop_id=20, price=300000, date=current_date), # Sugarcane

        # Adding market prices for livestock
        MarketPrice(livestock_id=1, price=90000, date=current_date),  # Goat
        MarketPrice(livestock_id=2, price=500000, date=current_date), # Cattle
        MarketPrice(livestock_id=3, price=40000, date=current_date),  # Chicken
        MarketPrice(livestock_id=4, price=40000, date=current_date),  # Sheep
        MarketPrice(livestock_id=5, price=90000, date=current_date),  # Pig
        MarketPrice(livestock_id=6, price=3000, date=current_date),   # Snail
        MarketPrice(livestock_id=7, price=35000, date=current_date),  # Fish
        MarketPrice(livestock_id=8, price=25000, date=current_date),  # Rabbit
        MarketPrice(livestock_id=9, price=50000, date=current_date),  # Turkey
        MarketPrice(livestock_id=10, price=35500, date=current_date)  # Duck
    ]

    # Create sample farming tips
    farming_tips = [
        FarmingTip(title='Timely Weeding', content='Regular weeding is essential to prevent competition for nutrients between crops and weeds.', date=current_date),
        FarmingTip(title='Pest Control', content='Use organic or chemical methods to control pests that can damage crops and reduce yields.', date=current_date),
        FarmingTip(title='Soil Fertility Management', content='Incorporate organic matter such as compost or manure to improve soil fertility.', date=current_date),
        FarmingTip(title='Proper Spacing', content='Ensure adequate spacing between plants to allow for proper growth and reduce competition.', date=current_date),
        FarmingTip(title='Water Management', content='Irrigate crops during dry periods to maintain soil moisture and improve crop yields.', date=current_date),
        FarmingTip(title='Crop Rotation', content='Rotate crops each season to prevent soil nutrient depletion and reduce the risk of pest infestations.', date=current_date),
        FarmingTip(title='Mulching', content='Use mulch to retain soil moisture, suppress weeds, and regulate soil temperature.', date=current_date),
        FarmingTip(title='Harvest Timing', content='Harvest crops at the right time to ensure maximum quality and yield.', date=current_date),
        FarmingTip(title='Seed Selection', content='Choose high-quality, disease-resistant seeds to increase the chances of a successful harvest.', date=current_date),
        FarmingTip(title='Disease Management', content='Monitor crops regularly for signs of disease and take action promptly to prevent spread.', date=current_date),
        FarmingTip(title='Use of Organic Fertilizers', content='Organic fertilizers enhance soil structure and provide essential nutrients to crops.', date=current_date),
        FarmingTip(title='Pruning', content='Regular pruning of plants can promote healthy growth and improve yields, especially for fruit-bearing plants.', date=current_date),
        FarmingTip(title='Climate Monitoring', content='Stay updated with weather forecasts to plan farming activities effectively and avoid losses.', date=current_date),
        FarmingTip(title='Integrated Pest Management', content='Combine biological, cultural, and chemical methods to manage pests sustainably and reduce reliance on pesticides.', date=current_date),
        FarmingTip(title='Conservation Agriculture', content='Practice conservation agriculture techniques such as minimal tillage, cover cropping, and crop diversification.', date=current_date),
        FarmingTip(title='Soil Testing', content='Regular soil testing helps determine nutrient needs and enables precise application of fertilizers.', date=current_date),
        FarmingTip(title='Storage Management', content='Proper storage of harvested crops is essential to prevent spoilage and maintain quality.', date=current_date),
        FarmingTip(title='Efficient Use of Resources', content='Optimize the use of water, fertilizers, and other inputs to reduce costs and improve sustainability.', date=current_date),
        FarmingTip(title='Biodiversity Enhancement', content='Encourage biodiversity on the farm by planting a variety of crops and maintaining natural habitats.', date=current_date),
        FarmingTip(title='Mechanical Weeding', content='Use mechanical weeding tools to reduce manual labor and improve efficiency in weed control.', date=current_date),
        FarmingTip(title='Monitoring Plant Health', content='Regularly inspect plants for signs of stress or disease to take corrective measures early.', date=current_date)
    ]

    # Create sample weather forecasts
    weather_forecasts = [
        WeatherForecast(forecast_date=current_date, temperature=28.5, condition='Rainy'),
        WeatherForecast(forecast_date=current_date, temperature=34.0, condition='Sunny'),
        WeatherForecast(forecast_date=current_date, temperature=26.0, condition='Cloudy'),
        WeatherForecast(forecast_date=current_date, temperature=22.0, condition='Thunderstorms'),
        WeatherForecast(forecast_date=current_date, temperature=30.0, condition='Partly cloudy'),
    ]

    # Add all the sample data to the session
    db.session.add_all(crops + livestock + market_prices + farming_tips + weather_forecasts)

    # Commit the session to save the data to the database
    try:
        db.session.commit()
        print("Database seeded successfully with Nigerian-specific data!")
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        print(f"An error occurred: {e}")
