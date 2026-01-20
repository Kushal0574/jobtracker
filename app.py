from db import init_db, get_connection
from models import Job
from utils import print_jobs

def add_job(company, role, status):
    conn = get_connection()
    job = Job(company, role, status)
    conn.execute(
        "INSERT INTO jobs (company, role, status) VALUES (?, ?, ?)",
        (job.company, job.role, job.status)
    )
    conn.commit()
    conn.close()

def list_jobs():
    conn = get_connection()
    rows = conn.execute("SELECT company, role, status FROM jobs").fetchall()
    conn.close()
    print_jobs(rows)

if __name__ == "__main__":
    init_db()
    add_job("Google", "Software Engineer", "Applied")
    add_job("Amazon", "Backend Engineer", "Interview")
    list_jobs()
