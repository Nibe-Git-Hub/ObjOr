Job Portfolio Project
This repository contains the code for a personal job portfolio website, built using HTML, CSS, and Bootstrap, and designed to be served via a Django application.

Table of Contents
Project Overview

Features

Prerequisites

Installation Guide

1. Clone the Repository

2. Set up a Python Virtual Environment

3. Install Project Dependencies

4. Configure Django Settings

5. Define URL Routes

6. Run the Development Server

Project Structure

Customization

Contributing

License

Project Overview
This project serves as a personal online portfolio to showcase your work, skills, experience, and contact information. It consists of a main landing page and a dedicated "About Me" page. The site is designed with responsiveness in mind, utilizing Bootstrap for a clean and adaptive layout.

Features
Main Page (/main): Introduction, featured projects, and contact information.

About Me Page (/about): Detailed personal information, skills, experience, and education.

Responsive Design: Adapts to various screen sizes (desktop, tablet, mobile) using Bootstrap.

Local Static Assets: All Bootstrap and Popper.js files are served locally, allowing for offline viewing (once the server is running).

Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.x (preferably Python 3.8 or newer)

pip (Python package installer, usually comes with Python)

Git (for cloning the repository)

Installation Guide
Follow these steps to get the project up and running on your local machine.

1. Clone the Repository
Open your terminal or command prompt and run the following command to clone the project:

git clone <repository_url>
cd Abella # Navigate into your project directory (assuming 'Abella' is your project root)

Replace <repository_url> with the actual URL of your Git repository.

2. Set up a Python Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

You should see (.venv) prefixing your terminal prompt, indicating the virtual environment is active.

3. Install Project Dependencies
Install all required Python packages using the requirements.txt file:

pip install -r requirements.txt

4. Configure Django Settings
Django needs to know where to find your HTML templates and static files (CSS, JS, images).

Place your files:

main.html and about.html should go into Abella/templates/.

bootstrap.min.css should go into Abella/static/css/.

bootstrap.min.js and popper.min.js should go into Abella/static/js/.

Any project images (e.g., for portfolio items) can go into Abella/static/img/ (you'll need to create this folder).

Update Abella/settings.py:
Ensure TEMPLATES and STATICFILES_DIRS are configured to point to your templates and static directories at the project root.

import os

# ...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Add this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), # Add this line
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # For production

5. Define URL Routes
You'll need to define the URL patterns for your main and about pages.

Create Abella/views.py:

# Abella/views.py
from django.shortcuts import render

def main_view(request):
    return render(request, 'main.html')

def about_view(request):
    return render(request, 'about.html')

Update Abella/urls.py (Project Level):
Add the routes and ensure static files are served in development.

# Abella/urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main_view, name='main'), # Route for the main page
    path('about/', views.about_view, name='about'), # Route for the about page
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

6. Run the Development Server
From your project root directory (Abella/), with your virtual environment active, run:

python manage.py runserver

This will start the Django development server, usually at http://127.0.0.1:8000/. You can then access your pages at http://127.0.0.1:8000/main and http://127.0.0.1:8000/about.

Project Structure
Abella/
├── .venv/                   # Python Virtual Environment
├── Abella/                  # Django Project Root (contains settings.py, urls.py, wsgi.py, asgi.py, views.py)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py             # New file for your views
│   └── wsgi.py
├── static/                  # Directory for static assets (CSS, JS, images)
│   ├── css/
│   │   └── bootstrap.min.css
│   ├── js/
│   │   ├── bootstrap.min.js
│   │   └── popper.min.js
│   └── img/                 # Optional: for project images
├── templates/               # Directory for HTML templates
│   ├── main.html
│   └── about.html
├── manage.py                # Django management script
├── requirements.txt         # Project dependencies (new file)
└── README.md                # This file

Customization
Content: Replace [Your Name], [Your Professional Tagline], [Your Field], project details, and contact information with your own in main.html and about.html.

Images: Update <img> tags with paths to your actual project screenshots and profile picture. Ensure these images are placed in your static/img/ directory and referenced using Django's static tag (e.g., <img src="{% static 'img/your-profile-image.jpg' %}" ...>).

Styling: Modify the inline <style> blocks in main.html and about.html or create separate CSS files (e.g., static/css/custom.css) for more extensive styling.

Projects: Add or remove .project-item divs in main.html as needed for your portfolio.

Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Make your changes.

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeature).

Open a Pull Request.

License
This project is open-sourced under the MIT License. See the LICENSE file for more details.
