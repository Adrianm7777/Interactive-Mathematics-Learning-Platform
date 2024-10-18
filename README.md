# Interactive-Mathematics-Learning-Platform

Description
An interactive platform for learning mathematics, where users can solve math problems at varying difficulty levels. The system evaluates users' answers and adjusts the difficulty level based on their performance. The application features a backend built using Django REST Framework and a frontend using Next.js and Tailwind.

Features
User registration and login.
Solving math problems (various difficulty levels).
Evaluating users' answers.
Tracking user progress.
REST API for managing problems and answers.
Requirements
To run the project, you need:

Python 3.8+
Node.js (with Next.js installed)
Yarn or npm
Django 4.0+
Django REST Framework
djangorestframework-simplejwt (optional, for JWT)
Installation
Backend (Django REST Framework)
Clone the repository:

bash
git clone https://github.com/your-repo/math_learning_platform.git
cd math_learning_platform
Install dependencies:

bash
pip install django djangorestframework djangorestframework-simplejwt
Create the database and run migrations:

bash
python manage.py makemigrations
python manage.py migrate
Create a superuser for the Django admin panel:

bash
python manage.py createsuperuser
Run the development server:

bash
python manage.py runserver
Visit the admin panel:

Open http://127.0.0.1:8000/admin/ in your browser.

Frontend (Next.js)
Navigate to the frontend folder and install dependencies:

If you don’t have a frontend yet, create a Next.js project:

bash
npx create-next-app@latest math-learning-frontend
cd math-learning-frontend
yarn add axios tailwindcss
Configure Tailwind CSS:

Install Tailwind CSS:

bash
yarn add -D tailwindcss postcss autoprefixer
npx tailwindcss init
Run the frontend application:

bash
yarn dev
The application will be available at http://localhost:3000.

API Endpoints
POST /api/register/ – User registration.
POST /api/login/ – User login (with optional JWT).
GET /api/problems/ – Fetch all math problems.
POST /api/submit-answer/ – Submit an answer for a problem.
GET /api/progress/ – Fetch user progress.
Future Features
Task recommendation system – Based on user performance, the app will suggest suitable tasks.
Leaderboard – A global scoreboard featuring top users.
Task creation – Teachers will be able to create custom tasks for their students.
Technologies
Backend: Django, Django REST Framework
Frontend: Next.js, TypeScript, Tailwind CSS
Database: SQLite (default, can be switched to PostgreSQL or others)
AI: Planned future enhancements (e.g., user level classification).

License
This project is licensed under the MIT License.
