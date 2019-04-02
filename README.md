# Python office hours coding challenge

This is an optional coding challenge for participants in the Python Office Hours. If you're stuck, you can look at this repository for example code.

# The challenge

## The dataset

We're scraping the city's database of employee salaries. You can find the JSON at `https://opendata.arcgis.com/datasets/54e0445a54c144cda3ce09596f50a134_0.geojson`

## The database

You must create a [Peewee](http://docs.peewee-orm.com/en/latest/) model to store employee data and use it to populate the database.

## The queries

You must use Peewee to query:

1. The number of employees whose last name is Lyles
2. The number of employees whose job title is Mayor
3. The largest salary paid to any city employee
4. The name and job title of the person who is paid the largest salary.
