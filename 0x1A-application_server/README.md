0x1A. Application server
------------------------
**DevOps SysAdmin**
Concepts
========
For this project, we expect you to look at these concepts:
* [Web Server](https://intranet.alxswe.com/concepts/17 "Web Server")
* [Server](https://intranet.alxswe.com/concepts/67 "Server")
* [Web stack debugging](https://intranet.alxswe.com/concepts/68 "Web stack debugging")
Background Context
------------------
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240611%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240611T162213Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=23a5883428c645efd40aabd8d8f563fba727c8a957066a95f624db27509cf2f2)
Your web infrastructure is already serving web pages via `Nginx` that you installed in your first [web stack project](https://intranet.alxswe.com/projects/266 "web stack project"). While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your `Nginx` and make is serve your Airbnb clone project.
Resources
---------
**Read or watch:**
* [Application server vs web server](https://www.f5.com/glossary "Application server vs web server")
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04 "How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04") (As mentioned in the video, do not install Gunicorn using `virtualenv`, just install everything globally)
* [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html "Running Gunicorn")
* [Be careful with the way Flask manages slash](https://werkzeug.palletsprojects.com/en/3.0.x/ "Be careful with the way Flask manages slash") in [route](https://flask.palletsprojects.com/en/3.0.x/api/#flask.Blueprint.route "route") - `strict_slashes`
* [Upstart documentation](https://doc.ubuntu-fr.org/upstart "Upstart documentation")
Requirements
------------
General
=======
* A `README.md` file, at the root of the folder of the project, is mandatory
* Everything Python-related must be done using python3
* All config files must have comments
Bash Scripts
============
* All your files will be interpreted on `Ubuntu 16.04 LTS`
* All your files should end with a new line
* All your Bash script files must be executable
* Your Bash script must pass `Shellcheck` (`version 0.3.7-5~ubuntu16.04.1 via apt-get`) without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing
