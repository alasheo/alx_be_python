def daily_reminder():
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Process the task based on priority
    match priority:
        case 'high':
            reminder = f"'{task}' is a high priority task"
        case 'medium':
            reminder = f"'{task}' is a medium priority task"
        case 'low':
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an undefined priority level"

    # Modify the reminder if the task is time-bound
    if time_bound == 'yes':
        reminder += " that requires immediate attention today!"

    # Provide a customized reminder
    print(f"Reminder: {reminder}")

if __name__ == "__main__":
    daily_reminder()

