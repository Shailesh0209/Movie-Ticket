from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from pickle import APPEND, APPENDS
import smtplib
from celery import Celery
from app import create_app
from workers import celery  # Make sure this import is correct
# from app import celery
from models import User, Booking
from celery.schedules import crontab
from datetime import datetime as date, timedelta
from models import Venue, Movie, Booking

# Set up Celery app
# celery = Celery('tasks', broker="redis://localhost:6379/1")


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/1'), daily_reminder.s(), name='every 1 minutes')
    # sender.add_periodic_task(crontab(minute=0, hour=0, day_of_month=1), monthly_report.s(), name='At midnight-of-month 1')
    sender.add_periodic_task(crontab(minute='*/1'), monthly_report.s(), name='At midnight-of-month 1')
    sender.add_periodic_task(crontab(minute='*/1'), check_mail.s(), name='every 1 minutes')

def send_mail(message, subject, receiver):
    sender_mail = 'appiitm01@gmail.com'
    sender_pass = 'tnrzkphpwnwivppt'
    
    msg = MIMEMultipart()
    msg['From'] = sender_mail
    msg['To'] = receiver
    msg['Subject'] = subject
    
    body = message
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    try:
        server.login(sender_mail, sender_pass)
        text = msg.as_string()
        server.sendmail(sender_mail, receiver, text)
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email:", str(e))
    finally:
        server.quit()


@celery.task(name='daily_reminder')
def daily_reminder():
    # send_mail("Hey, you have not booked a Movie, please book a movie, thanks", "Book a Movie", "shailxiitm@gmail.com")


    # print("daily_reminder is working")
    data = {}
    current_time = date.now()
    print(current_time)
    time_window = current_time - timedelta(hours=24)

    # bookings = Booking.query.all()
    bookings = Booking.query.filter(Booking.timestamp >= time_window)
    print(bookings) 
    if not bookings:
        send_mail("Hey, you have not booked a Movie, please book a movie, thanks", "Book a Movie", "shailxiitm@gmail.com")
    
    return 'Daily Reminder sent'

@celery.task(name='monthly_report')
def monthly_report():
    data = {}
    current_time = date.now()
    time_window = current_time - timedelta(days=30)
    bookings = Booking.query.filter(Booking.timestamp >= time_window)
    if not bookings:
        send_mail("Hey, you have not booked a Movie, please book a movie, thanks", "Book a Movie", "shailxiitm@gmail.com")
    else:
        subject = "Monthly Report"
        recipient = "shailxiitm@gmail.com"
        # HTML Message
        html_body = f"""
        <html>
        <head>
            <title>{subject}</title>
        </head>
        <body>  
            <h1>{subject}</h1>
            <p>{bookings}</p>
            <p>This is a monthly report</p>
        </body>
        </html>
        """
        send_mail(html_body, subject, recipient)
    return 'Monthly Report sent'

from models import Venue, Movie, Booking

@celery.task(name='export_theatre_csv')
def export_theatre_csv(theatre_id):
    theatre = Venue.query.get(theatre_id)
    if not theatre:
        return 'Theatre not found'

    # Get theatre details
    num_shows = len(theatre.movies)
    total_bookings = sum(len(movie.bookings) for movie in theatre.movies)
    avg_rating = sum(movie.avg_rating for movie in theatre.movies) / len(theatre.movies)
    total_revenue = sum(booking.total_price for movie in theatre.movies for booking in movie.bookings)
    contact_email = theatre.contact_email
    contact_phone = theatre.contact_phone

    # Create CSV content
    csv_content = f"Theatre Name,Location,Number of Shows,Total Bookings,Average Rating,Total Revenue,Contact Email,Contact Phone\n"
    csv_content += f"{theatre.name},{theatre.address},{num_shows},{total_bookings},{avg_rating},{total_revenue},{contact_email},{contact_phone}\n"

    csv_file_path = f"/path/to/csv/files/theatre_{theatre_id}.csv"
    with open(csv_file_path, 'w') as csv_file:
        csv_file.write(csv_content)

    # Send email notification to user
    subject = f"Theatre Export CSV - {theatre.name}"
    message = f"The CSV file for {theatre.name} has been generated and is attached."
    send_mail(subject, message, "shailxiitm@gmail.com", attachments=[csv_file_path])

    return f'Export CSV for {theatre.name} completed!'

