# Dockerized-RabbitMQ

This project provides code to run RabbitMQ, a message broker software, in a Docker container. Using Docker makes it easy to deploy and manage RabbitMQ without worrying about infrastructure. It's a great starting point for developers looking to add message queuing functionality to their projects.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Conclusion](#conclusion)

### Prerequisites

**1) Docker**

- [A Docker](https://hub.docker.com/)

**2) RabbitMQ**

All codes require a **RabbitMQ node running on localhost** with stock (default) settings.

To understand how to install RabbitMQ in different ways, check the RabbitMQ documentation. It has all the details about the installation process and the available options:

- [Windows](https://www.rabbitmq.com/install-windows.html) installer
- [MacOS](https://www.rabbitmq.com/install-homebrew.html) installer

**3) Pika**

Pika is a Python implementation of the AMQP 0-9-1 protocol for RabbitMQ.
To run this code you need to install the **pika** package version **1.0.0** or later. To install it, run

<!-- Add a code block with a copy button -->
<pre>
<code class="language-javascript">python -m pip install pika</code><button class="btn" data-clipboard-target="#code-block"></button>
</pre>

### Installation

To use the components in this repository, you will need to have Python 3 installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Once you have installed Python, you can download the repository by cloning it from GitHub:

<!-- Add a code block with a copy button -->
<pre>
<code class="language-javascript">git clone https://github.com/arrahim75/Dockerized-RabbitMQ</code><button class="btn" data-clipboard-target="#code-block"></button>
</pre>

### Usage

***Setting up the RabbitMQ container***

Before running the services in Docker, you will need to set up a RabbitMQ container.

1. Open a terminal window and run the following command to pull the RabbitMQ Docker image:

<!-- Add a code block with a copy button -->
<pre>
<code class="language-javascript">docker pull rabbitmq</code><button class="btn" data-clipboard-target="#code-block"></button>
</pre>

2. Run the following command to start the RabbitMQ container:

<!-- Add a code block with a copy button -->
<pre>
<code class="language-javascript">docker run -d --hostname rabbitmq-host --name rabbitmq-container -p 15672:15672 -p 5672:5672 rabbitmq:3-management
</code><button class="btn" data-clipboard-target="#code-block"></button>
</pre>

3. Open a web browser and navigate to http://localhost:15672. You should see the RabbitMQ management interface. Log in with the default credentials (guest/guest).

***Running the services in Docker***

To run the services in Docker, you will need to build Docker images for the Producer and Consumer services, and then run Docker containers for each service.

1. Open a terminal window and navigate to the root directory of the repository.

2. Build the Docker images for the Producer and Consumer services by running the following commands:

<!-- Add a code block with a copy button -->
<pre>
<code class="language-javascript">docker-compose up</code><button class="btn" data-clipboard-target="#code-block"></button>
</pre>

3. Navigate to Docker dashboard to view the results.

## Conclusion

That's it! You should now be able to use the components in this repository to implement a multi-container service. If you have any questions or issues, please feel free to open an issue on the GitHub repository.
