# Section 3 - System Design

This section of the repository contains the resources and explaination for the system design of a image upload web application.

# System Design Architecture Diagram

![System Design Architecture Diagram](section-3-system-design-diagram.png?raw=true "System Design Architecture Diagram")

# Assumptions

1. The company's software engineers have written code to process images that can be run in a serverless environment like AWS Lambda.
2. The company's engineers are familiar with managing Kafka streams on AWS.
3. The company's analysts are familiar with using Amazon Redshift for analytical computations.
4. Compliance and privacy requirements dictate that images and metadata should be stored for 7 days only.
5. AWS as cloud provider


# Solution

The architecture diagram shows the end-to-end flow of the data pipeline in the cloud environment. The components in the architecture diagram are explained in detail below:

* Web Application: The web application allows users to upload images to the cloud using an API. The web application will be hosted in an Amazon EC2 Auto Scaling Group. This helps to ensure that the correct number of Amazon EC2 Instances are always available to handle the load for the web application. We can set the minimum and maximum number of instance in EC2 Auto Scaling, which allows it to launch or terminate instances as demand on the web application increases or decreases. The Web Application will also use AWS Elastic Load Balancing, which is a load balancer on AWS. This ensures that the incoming application traffic across all the EC2 instances are distributed well. It manages requests by optimally routing traffic so that none of the EC2 Instances will be overwhelmed.

* Kafka Stream: There is a separate web application which hosts a self managed Kafka Application which is managed by the company employees. A topic created will be created for this application which will hold all the events sent from the web application. The messages will later be processed downstream, and if they are not processed, it will stay on the topic. Topic Partitions are also used to distribute the load. SASL/SCRAM authentication is also set up for accessing these brokers over the internet, which is managed by the AWS Secret Manager.

* Amazon S3 Bucket: In this system design, users are allowed to upload images onto our Amazon S3 Bucket. The bucket is split into two, one containing the raw user image uploads, another containing the processed images after being processed downstream. They are refered to 'User Images Upload' and 'Processed Images' in the diagram. As the requirement is to store the images for seven days, we will set up the lifecycle policy to seven days for these buckets, which after seven days the image will be automatically purged. As a best practice, AWS S3 Versioning is also used here to ensure we can recover data if needed. Finally, we will also use bucket policy to control access to the images.

* AWS Lambda: The code that was written by the company's engineers will be hosted on AWS lambda, which is a serverless compute service on AWS. There will be 2 lambda triggers in this system design: an apache kafka trigger and a Amazon S3 trigger to trigger our processing. The Amazon S3 trigger uses the invoke function on AWS S3 to automatically trigger the AWS Lambda function. The Apache Kafka trigger is built on AWS Lambda, where the lambda service internally polls for new records or messages from the source, and invokes the lambda function. The lambda function then processes these images and stores them in the 'Processed Images' AWS S3 bucket. Lambda is recommended for specific and small focused computations. We assume the image process is a small task so we have used it, otherwise, we will have to use compute-intensive resources. It will leverage the VPC across the whole setup for security. It is recommended to use logging and monitoring to keep an eye on the running lambda. 

* Dynamo DB: A Dynamo DB is used to store the metadata of the processed images. Dynamo DB will give us quicker return time on querying for business analytical purposes. If analyst require image metadata, it can be quickly obtained from here instead of a object storage like Amazon S3. It can be used to look at the snapshot of the system at any point in time as well. We will enable Time to live for the image metadata to purge the records after 7 days. Enabling TTL on your DynamoDB table allows us to specify a timestamp attribute for the table and set a time-to-live value in seconds. Once the timestamp attribute expires, the corresponding item is automatically deleted from the table.

* Amazon Redshift: Redshift is used as a BI resource in this system design which allows the company's business analysts to perform analytical computations on the process data. Dynamo DB metadata will be replicated into the redshift as well as “Processes images” bucket will be replicated to the redshift spectrum which will be used to query the data into the bucket direction from the redshift. Having both metadata and image data will allow the analyst to join both and generate analytics. 

* Tableau: Tableau can further be used to visualize any data and generate automated reports from Redshift, if needed.

# Extra Consideration

* Duplication/Overwrites of images from Kafka stream and web application: 

	1. Unique Identifiers when uploading images to ensure each image has a distinct id.
	2. Amazon S3 Versioning to track changes to objects over time.
	3. Configuring Permissions on S3 Bucket to restrict access and prevent deletion and overwrites
	4. Monitoring and alerting systems to detect and notify if there are any issues with image storages
