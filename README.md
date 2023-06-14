# Neuron - Mental Health Care Website

Neuron is a Django-based mental health care website that provides various features to support mental well-being. Users can take quizzes, view analytics on graphs, engage in music therapy, play games, and connect with doctors in critical situations. The website also includes a section called "Warrior's Story" where users can read inspiring stories of individuals who have overcome challenging situations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributors](#contributors)
- [License](#license)

## Installation

To run the Neuron project, follow these steps:

1. Ensure that you have Django installed. If not, run the following command to install it:

```shell
pip install django
```

2. Clone the Neuron repository:
```shell
git clone https://github.com/kevalhingu/neuron.git
cd neuron
```
3. Apply the database migrations:
```shell
python manage.py migrate
```
4. Create a superuser to access the admin panel:
```shell
python manage.py createsuperuser
```
#usage

To start the Neuron server, run the following command:
```shell
python manage.py runserver
```
Once the server is running, you can access the website by navigating to http://localhost:8000 in your web browser.

#features

Neuron offers the following key features:

Quiz functionality with analytics displayed on graphs
Music therapy for relaxation and mental well-being
Interactive games for mental stimulation
Contact information for doctors in nearby metro cities during critical situations
Inspiring stories of individuals who have overcome challenging situations






