# Imagely
### An example web application created with Django for learning purposes.

### Author: Kino Rose


# How To Run

1. Clone the repository `git clone https://github.com/KinoAR/imagely.git`
2. Install Django `pip install django=2.1.3`
3. Install Pillows `pip install Pillow`



# Django Notes

## Migrations
Migrations are how Django storage changes to your models (database schema). Migrations allow you to update your database schema live due to the flexibility of being able to synchronize changes made to your models.

## SQL Migrations
`python manage.py sqlmigrate imagestorage 0001`

Prints the SQL code that Django thinks is required for your migrations.

# Django API Shell
`python manage.py shell`

Allows you to interactively play around with the Django API; this shell sets the environment variables to match the Django project.