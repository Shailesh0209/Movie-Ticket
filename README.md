# Movie-Ticket-Project
This project involves building a Vue.js web application for managing venues, and movies.
The application has two user roles: administrators and users. Admin can add, edit, and
delete venue details and movies through modals. Users can view and book venues and
movies.

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


## Steps to run my project
1. Create a virtual environment `python3 -m venv env` and then activate it `venv/scripts/activate` or `venv/bin/activate`.
2. Install requirements.txt file `pip install -r requirements.txt`.
3. run backend `python3 app.py`
4. run frontend `npm run serve` Note: move to exact frontend directory with venv activated
5. run celery workers `celery -A workers.celery worker -l info`
6. run celery beats `celery -A workers.celery beat --max-interval 1 -l info`

### if you have any doubts, reach me at shailxiitm@gmail.com


