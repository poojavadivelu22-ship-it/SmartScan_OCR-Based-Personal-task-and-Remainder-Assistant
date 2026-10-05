from datetime import datetime


def check_reminder(task_date, task_time):

    current_time = datetime.now()

    task_datetime = datetime.strptime(
        f"{task_date} {task_time}",
        "%Y-%m-%d %H:%M:%S"
    )

    if current_time >= task_datetime:

        return True

    return False