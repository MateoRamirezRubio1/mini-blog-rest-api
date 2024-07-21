This project is a Django-based mini blog application designed to illustrate the implementation of the Services and Repositories design pattern. It features a clear separation of concerns, making the codebase easier to maintain and extend.

**You can follow the step by step of the making of the app on my blog: [My blog](https://mateoramirezr.hashnode.dev/django-services-and-repositories-design-pattern-with-rest-api).**

## Features
- **Posts and Comments:** Users can create, update, and delete blog posts and comments.
- **RESTful API:** Provides endpoints for interacting with the application programmatically.
- **Web Interface:** Offers a basic user-friendly interface for managing posts and comments.
- **Service Layer:** Contains business logic and orchestrates interactions between views and repositories.
- **Repository Layer:** Encapsulates data access logic, providing a clean API for the service layer.
- **Django Admin:** Allows administrative management of posts and comments.

## Project Structure
The project follows a modular structure, with each app having its own models, views, serializers, services, and repositories.

my_project_blog/ <br>
├── apps/ <br>
│   ├── comments/ <br>
│   │   ├── models.py <br>
│   │   ├── repositories/ <br>
│   │   ├── services/ <br>
│   │   ├── templates/ <br>
│   │   ├── views/ <br>
│   ├── posts/ <br>
│   │   ├── models.py <br>
│   │   ├── repositories/ <br>
│   │   ├── services/ <br>
│   │   ├── templates/ <br>
│   │   ├── urls/ <br>
│   │   ├── views/ <br>
├── my_project_blog/ <br>
│   ├── settings.py <br>
│   ├── urls.py <br>
│   ├── wsgi.py <br>
├── manage.py <br>

## Architectural pattern
![PatronArquitectura](https://github.com/MateoRamirezRubio1/mini-blog-rest-api/assets/100296963/c7df2c24-06a5-404c-8349-c635a82bfc93)

## Getting Started
To get started with this project, follow these steps:

1. **Clone the repository:**
```
git clone https://github.com/MateoRamirezRubio1/mini-blog-rest-api.git
cd my_project_blog
```

2. **Set up a virtual environment:**
```
python -m venv venv
source `venv\Scripts\activate` # This is for windows

```

3. **Install dependencies:**
```
pip install -r requirements.txt
```

4. **Apply migrations:**
```
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser:**
```
python manage.py createsuperuser
```

6. **Run the development server:**
```
python manage.py runserver
```

7. **Access the application:** <br>
Open your web browser and go to `http://127.0.0.1:8000/api/posts/` to start creating posts.
