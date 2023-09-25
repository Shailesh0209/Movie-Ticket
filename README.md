# Movie-Ticket
- This project involves building a Vue.js web application for managing venues, and movies.
- The application has two user roles: administrators and users.
- Admin can add, edit, and delete venue details and movies through modals.
- Users can view and book venues and movies.
- Admin and Users can search venue or movie name using search box.


## Steps to run my project
1. Create a virtual environment `python3 -m venv env` and then activate it `venv/scripts/activate` or `venv/bin/activate`.
2. Install requirements.txt file `pip install -r requirements.txt`.
3. run backend `python3 app.py`
4. run frontend `npm run serve` Note: move to exact frontend directory with venv activated
5. run celery workers `celery -A workers.celery worker -l info`
6. run celery beats `celery -A workers.celery beat --max-interval 1 -l info`


[![Presentation video](https://i.ytimg.com/vi/5y0l0qwQ554/maxresdefault.jpg)](https://www.youtube.com/watch?v=5y0l0qwQ554)

## Frameworks used
- Flask for API
- VueJS for UI 
- Jinja2 templates 
- Bootstrap
- SQLite for database 
- Redis for caching
- Redis and Celery for batch jobs
  - Scheduled Job - Daily reminders on Google Chat using webhook or Email
  - Scheduled Job - Monthly Entertainment Report
  - User Triggered Async Job - Export as CSV
- Flask-Caching
  - Added caching wherever required to increase the performance
  - Added cache expiry 
  - API Performance also improved

## Technologies used 
- Vue.js: A JavaScript framework for building user interfaces. It allows for creating dynamic and responsive web applications with its component-based architecture.
- BootstrapVue: A library that integrates Bootstrap components with Vue.js, providing a convenient way to create visually appealing and responsive user interfaces.
- Vuex: A state management pattern and library for Vue.js applications. It centralizes and manages the state of the application, making it easier to share data between components. 
- Vue Router: A routing library for Vue.js applications. It enables navigation between different views and components in a single-page application. 
- Axios: A popular HTTP client for making asynchronous HTTP requests. It's used to communicate with the backend API to fetch and send data. 
- Flask: A lightweight and flexible Python web framework. It's used to build the backend API that handles data storage, retrieval, and manipulation. 
- Flask-RESTful: An extension for Flask that simplifies the creation of RESTful APIs. It helps in defining API resources and their endpoints. 
- Flask-CORS: An extension for handling Cross-Origin Resource Sharing (CORS) in Flask applications. It allows the frontend to make requests to the backend from a different domain. 
- SQLAlchemy: A powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. It's used to interact with the database and manage database operations.
- SQLite: A lightweight, serverless, and self-contained database engine. It's used as the database system to store and manage application data. 
- JWT (JSON Web Tokens): A compact and self-contained way for securely transmitting information between parties as a JSON object. It's used for user authentication and authorization. 
- Python: The programming language used for developing the Flask backend and handling server-side logic.

## ...Connect with me
- [LinkedIn](https://www.linkedin.com/in/shailx876/)
- [Insta](https://www.instagram.com/shailx_kr/)
- [Kaggle](https://www.kaggle.com/shailx)
### if you have any doubts, reach me at shailxiitm@gmail.com


