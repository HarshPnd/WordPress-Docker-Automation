# WordPress-Docker-Automation

# About the Project -

This project automates the deployment of a Dockerized WordPress application with Python scripting and persistent database storage. It's designed for DevOps professionals, developers, and anyone seeking a convenient and efficient way to set up a WordPress website in a Docker environment. By running a simple script, users can quickly establish a WordPress site with all dependencies, making it an ideal solution for those who want to streamline the deployment process and focus on web development rather than system configuration.

Simplify your WordPress deployment and get started with ease.



# What is WordPress ?

WordPress (WP, WordPress.org) is a free and open-source content management system (CMS) written in PHP and paired with a MySQL or MariaDB database. Features include a plugin architecture and a template system, referred to within WordPress as Themes. WordPress was originally created as a blog-publishing system but has evolved to support other types of web content including more traditional mailing lists and forums, media galleries, membership sites, learning management systems (LMS) and online stores. WordPress is used by more than 60 million websites, including 33.6% of the top 10 million websites as of April 2019, WordPress is one of the most popular content management system solutions in use. WordPress has also been used for other application domains such as pervasive display systems (PDS).


# What is MySQL Database ?

MySQL is an open-source relational database management system (RDBMS) known for its performance, reliability, and scalability. It provides a structured and efficient way to store, manage, and retrieve data for web applications like WordPress. MySQL is essential for maintaining content, user data, and website functionality.

# What is Docker ?

Docker is a comprehensive platform designed for simplifying application development, deployment, and management. It utilizes containerization technology, allowing you to package applications and their dependencies in isolated containers. Containers ensure consistent performance across different environments, making it easier to develop, test, and deploy software. Docker provides a standardized way to package and run applications, making it a popular choice for DevOps and developers.

# What is HTTPD (Apache HTTP Server) ?

HTTPD refers to the Apache HTTP Server, a widely used open-source web server software. It's responsible for serving web content and handling HTTP requests. Apache provides a robust and customizable platform for hosting websites, delivering web pages, and executing server-side scripts. It's a fundamental component for running web applications.

# What is Git ?

Git is a distributed version control system used in software development. It enables multiple team members to collaborate on code by tracking changes, managing versions, and facilitating efficient code-sharing. Git's decentralized architecture ensures data redundancy and enhances code management, making it a vital tool for software developers and project teams.

# What is Docker Compose ?

Docker Compose is a powerful tool for defining and running multi-container Docker applications. It simplifies the management of complex, interconnected services by using a YAML configuration file. With Docker Compose, you can specify containers, networks, and volumes, making it easy to set up and orchestrate multi-service applications. It streamlines the deployment of complex systems by specifying the relationships between different components, facilitating a more efficient development and deployment process.

# What are Docker Volumes ?

Docker volumes are a fundamental feature for managing data in containerized environments. They provide data persistence, enabling information to survive the lifecycle of containers. Volumes are isolated from container file systems and come in various types, including named volumes and host-mounted volumes. They facilitate data sharing, backup, and migration, making them crucial for preserving and sharing data in containerized applications while ensuring security and performance.

---

# Automated Setup

Follow these steps to quickly automate the setup of your Dockerized WordPress application on an EC2 instance:

## Step 1: Configure and Launch EC2 Instance

- Configure and launch an EC2 instance using any RPM-based Linux distribution of your choice.
- Set up inbound rules in the EC2 security group to allow connections to your WordPress website. Common ports to open include 80 (HTTP) and 22 (SSH) for initial setup.

## Step 2: Connect to Your EC2 Instance

- Connect to your EC2 instance via SSH by using the public IP or DNS provided by AWS.

## Step 3: Switch to Root User

- Switch to the root user with the following command:
  
       sudo su -

## Step 4: Get the Automation Script

- Retrieve the Dockerized WordPress automation script from the GitHub repository.  
You can do this in one of two ways:  

  - Clone the GitHub repository to your instance using the following command:  

        git clone https://github.com/HarshPnd/WordPress-Docker-Automation.git

  - Alternatively, manually copy and paste the contents of the __dockerizedWordPressAutomationScript.py__ file to your EC2 instance.

    **dockerizedWordpressAutomationScript.py**

        import subprocess
        import os

        # Check if the script is being run as the root user
        current_user = subprocess.check_output("whoami", shell=True, text=True).strip()
        if current_user != "root":
          print("Please switch to the root user by running 'sudo su -' before executing this script.")
          exit(1)

        # Define a list of commands for the first set of actions
        commands_set1 = [
          "yum install httpd -y",
          "yum install docker -y",
          "yum install git -y",
          "sudo systemctl start httpd",
          "sudo systemctl start docker",
          "curl -SL https://github.com/docker/compose/releases/download/v2.23.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose",
          "chmod +x /usr/local/bin/docker-compose",
          "git clone https://gist.github.com/21f213a4d02ee6ab219ee4c2c645b01d.git"
        ]

        # Get the current working directory using the `pwd` command
        current_directory = subprocess.check_output("pwd", shell=True, text=True).strip()

        # Construct the new directory path
        new_directory = os.path.join(current_directory, "21f213a4d02ee6ab219ee4c2c645b01d")

        # Execute the first set of commands with exception handling
        for cmd in commands_set1:
          try:
            subprocess.run(cmd, shell=True, check=True)
          except subprocess.CalledProcessError as e:
            print(f"Command failed: {cmd}")
            print(f"Error message: {e}")
            break
          except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
        else:
          print("First set of commands executed successfully.")
    
        # Change the current working directory to the new directory
        os.chdir(new_directory)

        try:
          subprocess.run("docker-compose up -d", shell=True, check=True)
          result = subprocess.run("curl -4 -s icanhazip.com", shell=True, check=True, capture_output=True, text=True)
          output = "Copy & Paste the following Ip address in a new tab:  " + result.stdout.strip() + ":8080"
          print(output)
        except subprocess.CalledProcessError as e:
          print(f"Command failed: {cmd}")
          print(f"Error message: {e}")
        except Exception as e:
          print(f"An unexpected error occurred: {e}")

        # Change the working directory back to the original directory
        os.chdir(current_directory)


## Step 5: Run the Automation Script

 - Execute the automation script with the following command:  

       python dockerizedWordPressAutomationScript.py

## Step 6: Access Your Dockerized Microservices

- The script will provide you with an IP address and port. Copy and paste this IP address, along with the specified port, into a new web browser tab.

- Voila!💥 Your WordPress website and associated services are up and running as Dockerized microservices on your EC2 instance.  

___

# Manual Setup

If you prefer to set up the project manually, without automation or Docker Compose, follow these steps:

## Step 1: Configure and Launch EC2 Instance

- Configure and launch an EC2 instance using any RPM-based Linux distribution of your choice.
- Set up inbound rules in the EC2 security group to allow connections to your WordPress website. Common ports to open include 80 (HTTP) and 22 (SSH) for initial setup.

## Step 2: Connect to Your EC2 Instance

- Connect to your EC2 instance via SSH by using the public IP or DNS provided by AWS.

## Step 3: Switch to Root User

- Switch to the root user with the following command:
  
      sudo su -

## Step 4: Install Apache HTTP Server  

    yum install httpd -y

 ![](/dockerized_wordpress_images/install_httpd.png)

 ## Step 5: Install Docker  

    yum install docker -y
  
 ![](/dockerized_wordpress_images/install_docker.png)


## Step 6: Start HTTPD (Apache)  
  
    systemctl start httpd


## Step 7: Start Docker Service  
  
    systemctl start docker


## Step 8: Create MySQL Container (dbos)  
  
    docker run -d -it -e MYSQL_ROOT_PASSWORD=rootpass -e MYSQL_USER=vimal -e MYSQL_PASSWORD=redhat -e MYSQL_DATABASE=mydb -v mysql_storage:/var/lib/mysql --name dbos mysql:5.7
 
 ![](/dockerized_wordpress_images/launch_dbos.png)

## Step 9: Create WordPress Container (wpos)  

    docker run -dit -e WORDPRESS_DB_HOST=dbos -e WORDPRESS_DB_USER=vimal -e WORDPRESS_DB_PASSWORD=redhat -e WORDPRESS_DB_NAME=mydb -v wp_storage:/var/www/html --name wpos -p 8080:80 --link dbos wordpress:5.1.1-php7.3-apache
 
 ![](/dockerized_wordpress_images/launch_wpos.png)


## Step 10: Get External IP Address  

    curl -4 -s icanhazip.com
 
 ![](/dockerized_wordpress_images/get_ip.png)
 
## Step 11: Access Your Dockerized Microservices  

- The last command will provide you with an IP address. Copy and paste this IP address, along with the specified port **:8080**, into a new web browser tab.
 
 ![](/dockerized_wordpress_images/wp_admin.png)
 

- Voila!💥 Your WordPress website and associated services are up and running as Dockerized microservices.
 
 ![](/dockerized_wordpress_images/wp_website.png)  



 
 P.S. - Any suggestions and improvements are warmly welcome.
