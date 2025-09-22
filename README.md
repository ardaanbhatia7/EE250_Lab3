# Lab 3

## Team Members
 - Kyna Rochlani -> rochlani@usc.edu -> kynarochlani2006
 - Ardaan Bhatia -> ardaanbh@usc.edu -> ardaanbhatia7
## Lab Question Answers

Question 1: Why are RESTful APIs scalable?
 - They are scalable because they are stateless. Each request has all the information needed, so the server doesn\u2019t need to track sessions. This makes it easier to add servers, balance load, and use caching to handle more requests.


Question 2: According to the definition of "resources" provided in the AWS article above, What are the resources the mail server is providing to clients?
 - The resources include emails (individual messages), folders like inbox or sent, attachments inside emails, and user accounts with their settings. Each of these can be treated as a resource that the client can request or update.

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?
 - One method not used is PUT. We could add it so a user can update an existing draft by sending new content to the same endpoint, replacing the old version.

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!
 - API keys are used to identify the client or application making a request. They help control access by allowing only approved clients to use the API. They also enforce limits on how many requests can be made, which prevents abuse. In addition, API keys make it possible to track usage and monitor how different clients are using the service.

