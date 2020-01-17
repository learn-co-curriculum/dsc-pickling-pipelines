# Cloud Services

<img src="https://nerds.net/wp-content/uploads/2018/02/cloud-computer-reality-750x646.jpg" width="400px">

## Students Will Be Able To
 - [ ] Explain the general concept of "the cloud"
 - [ ] Understand the cases where _hardware acceleration_ is useful
 - [ ] Understand the cases where _cloud storage_ is useful
 - [ ] Explain the difference between a "cloud database" and a "storage bucket"

## Hardware Acceleration

As much as software libraries like NumPy or Spark can improve the efficiency of code, there is a limit to how much of a difference they can make, depending on the actual hardware of your computer.

As a general concept, [hardware acceleration](https://www.omnisci.com/learn/resources/technical-glossary/hardware-acceleration) means using purpose-built hardware rather than general-purpose hardware.

In the case of machine learning, this typically means running your code on a GPU, rather than a CPU.  A CPU _can_ do everything that a GPU can do, but it is not optimized for it, so it will likely take more time.  [This blog](https://towardsdatascience.com/maximize-your-gpu-dollars-a9133f4e546a) argues that a CPU is to a GPU as a horse and buggy is to a car.

Sometimes you want to use cloud computing just for the GPU!

### Cloud Services with Hardware Acceleration

There is a lot of overlap between these services and the services listed on the Deployment page, but you may need to configure them specifically to indicate you want to use a GPU:

 - [AWS EC2](https://aws.amazon.com/blogs/machine-learning/train-deep-learning-models-on-gpus-using-amazon-ec2-spot-instances/)
 - [Google Cloud Platform](https://cloud.google.com/ml-engine/docs/using-gpus)
 - [IBM Watson Studio](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml_dlaas_gpus.html)
 - [AWS Sagemaker](https://aws.amazon.com/machine-learning/accelerate-machine-learning-P3/)
 - [Azure VM](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/sizes-gpu)

There are also some cloud IDEs with GPUs, where you can run Jupyter Notebook code:

 - [Databricks Community Edition](https://community.cloud.databricks.com/)
 - [Google Colab](https://towardsdatascience.com/getting-started-with-google-colab-f2fff97f594c)
 - [Kaggle kernels](https://www.kaggle.com/dansbecker/running-kaggle-kernels-with-a-gpu)

## Cloud Storage

It's annoying to have huge data files taking up space on your laptop, and if you want to train your model in the cloud, your data also needs to be in the cloud.  But for reasons related to hardware acceleration, it can get pretty expensive to store large datasets in general-purpose cloud services like an EC2 instance or a cloud VM.  That's when cloud storage services become useful.

### Cloud Storage Buckets

The major providers of storage "buckets" are:

 - [AWS S3](https://aws.amazon.com/s3/getting-started/)
 - [Google Cloud Storage](https://cloud.google.com/storage/)
 - [Azure Storage](https://docs.microsoft.com/en-us/azure/storage/common/storage-introduction)

These tools are designed for uploads of raw files, e.g. folders full of images, CSVs, or JSONs.

They each cost about 2-5 cents per GB per month.  AWS S3 is the oldest and tends to have the most integration support with other platforms, although you may need to use Google storage if you're using other Google products or Azure storage if you're using other Azure products.

### Cloud Databases

If you want to deploy a website where new information gets saved (what kinds of queries users perform, user ratings of the quality of predictions, etc.) then you need a cloud database.  These work roughly the same as a database running on your computer.

Using a cloud database is mainly an opportunity to practice using tooling that you are likely to use on the job, because they assist with collaboration.

Some popular providers are:

 - [Heroku Postgres](https://www.heroku.com/postgres)
 - [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
 - [AWS Aurora](https://aws.amazon.com/rds/aurora/)
 - [AWS RDS](https://aws.amazon.com/rds/)

Most of these tools have a free tier, which permits a limited number of records to be stored.

## Links to Other Resources

 - [Introduction to AWS for Data Scientists](https://www.dataquest.io/blog/introduction-to-aws-for-data-scientists/)