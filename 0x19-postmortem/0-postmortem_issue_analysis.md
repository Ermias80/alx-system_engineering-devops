# Postmortem

![IMG](https://github.com/Ermias80/alx-system_engineering-devops/blob/master/0x19-postmortem/0-postmortem_issue.webp)

# Issue Summary

On 09-06-2024, our newly launched tour and travel agency website experienced a critical issue shortly after deploying a new feature. Within 10 minutes of the update, users began reporting issues with booking tours and travel services. Approximately 45% of our user base was affected. Upon investigation, it was discovered that a misconfigured database connection pool was the root cause, preventing the application from establishing stable connections to the database. This resulted in disrupted user authentication and booking processes.

The incident began at 6:20 PM GMT+3 and persisted until 1:10 AM GMT+3 when the database connection pool configuration was corrected.

# Timeline

* 6:20 PM GMT+3: The issue begins; user reports indicate an inability to complete bookings.
* 6:20 PM GMT+3: Mahari, our senior backend developer, encounters the same issue.
* 6:30 PM GMT+3: The engineering team begins investigating the issue, focusing on database logs, query performance, and network connectivity.
* 6:40 PM GMT+3: The database connection failure is identified; the team starts troubleshooting the database server.
* 6:45 PM GMT+3: The team mistakenly believes the external API for availability verification is experiencing an outage.
* 6:50 PM GMT+3: The incident is escalated to the DevOps team.
* 7:00 PM GMT+3: The database server is restarted, resolving the connection issue.
* 7:10 PM GMT+3: Functionality is verified, and the incident is declared resolved.

# Root Cause and Resolution
The outage was caused by a misconfiguration in the database connection pool, which hindered the web application's ability to connect to the database. The issue was identified by the engineering team through monitoring alerts and resolved by restarting the database server.

# Corrective and Preventative Measures 
To prevent similar incidents in the future, the following measures will be implemented:
+ [x] 1. Investigate the Database Server Failure: A detailed review of server logs and diagnostics will be conducted to understand the cause of the failure.
