def print_jobs(rows):
    print("\nJob Applications:")
    print("-" * 40)
    for company, role, status in rows:
        print(f"{company:15} | {role:20} | {status}")
