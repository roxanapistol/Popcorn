import datetime
from faker import Faker
fake = Faker(locale='en_Ca')

app = 'Popcorn'
popcorn_url = 'https://www.gopopcorn.ca/'
popcorn_home_page_title = 'Popcorn - Digital Marketing & PR Agency Vancouver | Popcorn'

contact_us_url = 'https://www.gopopcorn.ca/contact-us/'
contact_us_title_page = 'Contact Us - Popcorn'

services_url = 'https://www.gopopcorn.ca/services/'
services_title_page = 'Services - Popcorn'

tourism_vancouver_url = 'https://www.gopopcorn.ca/portfolio/tourism-vancouver/'
tourism_vancouver_title_page = 'Tourism Vancouver - Popcorn'

nest_design_url = 'https://www.gopopcorn.ca/portfolio/nest-designs/'
nest_design_title_page = 'Nest Designs - Popcorn'

skip_the_dish_url = 'https://www.gopopcorn.ca/portfolio/just-eat/'
skip_the_dish_title_page = 'Just Eat (Skip The Dishes) - Popcorn'

case_studies_url = 'https://www.gopopcorn.ca/case-studies/'
case_studies_title_page = 'Case Studies - Popcorn'

canadian_workplace_url = 'https://www.cultureindex.io/'
canadian_workplace_title_page = 'The Canadian Workplace Culture Index'

who_we_are_url = 'https://www.gopopcorn.ca/who-we-are/'
who_we_are_title_page = 'Who We Are - Popcorn'

first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
full_name = f'{first_name} {last_name}'
subject = f'Test message: today is: {datetime.datetime.now()}. '

