0x0D. Web stack debugging #0
============================

Concepts
--------

*For this project, students are expected to look at these concepts:*

-   [Network basics](https://alx-intranet.hbtn.io/concepts/33)
-   [Docker](https://alx-intranet.hbtn.io/concepts/65)
-   [Web stack debugging](https://alx-intranet.hbtn.io/concepts/68)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/265/uWLzjc8.jpg)

Background Context
------------------

The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that's the "fun" part of the job!).

Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.

In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.

Let's start with a very simple example. My server must:

-   have a copy of the `/etc/passwd` file in `/tmp`
-   have a file named `/tmp/isworking` containing the string `OK`

