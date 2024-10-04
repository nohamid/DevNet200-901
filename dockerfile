# Specify Base Image and Author 
    FROM ubuntu:16.0
    MAINTAINER Nomaan Hamid (nohamid@cisco.com)

# Tell Docker what to do: 
    RUN apt-get update && apt-get upgrade -y
    RUN apt-get install nginx -y

# Tell Docker the Port:
    EXPOSE 80 443 

# Create sharepoint to reach files:
    VOLUME /Users/nohamid/Documents/Learning/200-901/Docker/HTML

# Tell Container to run nginx on Launch:
    CMD ["nginx", "-g" "daemon off;"]

    