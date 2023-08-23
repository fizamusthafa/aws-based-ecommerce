# Collection

## Setting Up a Data Firehose Stream for Capturing Server Logs in Amazon Kinesis

This part of the document outlines the process of establishing a Kinesis Data Firehose stream on Amazon Web Services (AWS) to efficiently capture server logs generated from an Amazon EC2 instance. Kinesis Data Firehose facilitates real-time data transfer to AWS for comprehensive analysis.


* **Create a Data Firehose Stream:** I accessed the "Kinesis" service and opted to "Create delivery stream."
* **Specify Data Source and Destination**: I selected "Direct PUT" as the data source option. This ensures direct data input into the Firehose stream. The destination was an Amazon S3 bucket.
* **Provide a Name for the Delivery Stream:** Assign an identifying name to the delivery stream. Furthermore, set up an S3 bucket for data storage, configure buffering and compression, and then finalize the delivery stream creation by reviewing settings and executing the setup.
* **Monitor and Analyze:** Track the creation process of the delivery stream. Upon activation, server logs will be systematically captured and routed to the designated S3 bucket.
By systematically following these steps, a functional Kinesis Data Firehose stream is established to efficiently capture and route server logs to an Amazon S3 bucket. Maintain awareness of the 60-second buffer interval to optimize data capture frequency.

## Setting Up an EC2 Instance to Feed Data into Amazon Kinesis Firehose

This outlines the process of configuring an Amazon Elastic Compute Cloud (EC2) instance for the generation and feeding of data into an Amazon Kinesis Data Firehose stream. This ensures a comprehensive testing of the data capture and transfer process, contributing to operational readiness.

* **Launching an EC2 Instance:** Log in to the AWS Management Console to initiate the setup.
* **Creating a New Instance:** Utilized the "Launch Instances" option to create a new instance with preferred Linux AMI and suitable instance type.
* **Configuring Security Groups:** Authorized SSH access (port 22) for seamless connection to the instance.
* **Launching the Instance:** Reviewed and confirmed instance settings before launching. Generated a new key pair and stored the private key (.pem) file.
* **Connecting to the Instance:** Since I use Windows, I connected to the EC2 instance via PuTTY and the .ppk private key.
* **Installing the Kinesis Agent:** Installed the Kinesis agent using the command:```sudo yum install -y aws-kinesis-agent```
* **Making the Script Executable:** Ensure that the LogGenerator.py script is executable by running the following command: ```chmod a+x LogGenerator.py```
* **Create a log directory:**  Create a directory to accommodate generated log data
* **Configure the Kinesis Agent:** Navigate to the Kinesis agent configuration file
```
cd /etc/aws-kinesis
sudo nano agent.json
```
Configure the agent to direct data to the log directory, and execute the LogGenerator.py script to generate and feed log data to the designated directory
