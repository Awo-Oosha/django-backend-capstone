from django.core.management.base import BaseCommand
from restaurant.models import Menu, Booking
import requests
import pandas as pd

class Command(BaseCommand):
    help = 'Import data from a URL and save it to the Menu model'

    def handle(self, *args, **options):
        url = "https://my.api.mockaroo.com/bookings.json?key=4afbb690"

        # Fetch data from the URL
        response = requests.get(url)
        data = response.json()

        # Convert data to a DataFrame
        df = pd.DataFrame(data)

        # Loop through DataFrame rows and save to the Menu model
        for index, row in df.iterrows():
            Booking.objects.create(
                name=row['name'],
                no_of_guest=row['no_of_guests'],
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
