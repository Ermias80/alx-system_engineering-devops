# Postmortem

![IMG](https://github.com/Ermias80/alx-system_engineering-devops/blob/master/0x19-postmortem/0-postmortem_issue.webp)

# Issue Summary

On 09-06-2024, our newly launched tour and travel agency website experienced a critical issue shortly after deploying a new feature. Within 10 minutes of the update, users began reporting issues with booking tours and travel services. Approximately 45% of our user base was affected. Upon investigation, it was discovered that a misconfigured database connection pool was the root cause, preventing the application from establishing stable connections to the database. This resulted in disrupted user authentication and booking processes.

