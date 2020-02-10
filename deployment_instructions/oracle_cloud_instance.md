# Oracle Cloud Instances

Oracle Cloud Instances are similar to AWS EC2 instances: basically a complete "computer" that runs in the cloud, and that you interact with via SSH in the terminal.

Oracle seems to be trying to match the services provided by AWS, Google Cloud, and Azure, and is attracting customers by making the free tier of their "instance" service pretty fast/powerful.

## Prerequisites

These instructions assume that you already have a working, production-ready Flask application, where all of the relevant files (including the pickled model) have been pushed up into a single public GitHub repository.

The repository should have a `requirements.txt` in it, which was generated with `pip freeze > requirements.txt`.

## Step 1: Making the Cloud Instance

Go to the [Oracle Cloud Infrastructure website](https://www.oracle.com/cloud/), click on "Try Oracle Cloud Free Tier", click on "Start for Free", and go through the account creation flow.  It will require you to enter credit card information.  Choose "US West (Phoenix)" as your region.

Assuming you chose "US West (Phoenix)" as your region, the home page for managing your cloud services is https://console.us-phoenix-1.oraclecloud.com/.  From there, click on "Create a VM Instance".

The trickiest part here is getting the SSH key connected.  The combination of public and private keys is used _instead of_ a traditional username/password login.  You provide the public key when setting up your instance and provide the private key when logging in.

Assuming you set up GitHub correctly back in Week 1, you should not need to generate a new SSH key.  It should already be located on your computer at `~/.ssh/id_rsa.pub`.  Because the `.ssh` directory starts with a `.`, the Mac OS will not automatically show it to you when you click "Choose Files", so you need to type `Command+Shift+G` (`⇧⌘G`) from the Finder window and then type `~/.ssh` into the textbox and select `id_rsa.pub` from the folder once it's opened.

Ok, once the status of the cloud instance turns green and says RUNNING, you should be able to log into your cloud instance!

## Step 2: Logging in

Your cloud instance is basically like any other Unix-like computer, which can be accessed via the command line.

To connect, first find the public IP address from the "Instance Details" page.  It is under the "Primary VNIC Information" header.  My instance, for example, has the IP address `129.146.133.106`.

In a Terminal window on your local computer, use the SSH command to connect.  The format is:
```
ssh opc@<ip_address> —i <private_key>
```
So, for example, I log in with:
```
ssh opc@129.146.133.106 -i ~/.ssh/id_rsa
```

(You may not actually need the last part starting with `-i` depending on your computer's configuration, but I think it's helpful to be explicit)

Now you should see a command prompt, something like:
```
[opc@instance-XXXXXXXX-XXXX ~]$
```

This is a Bash prompt, which works very similarly to the one on your Mac.  Try some basic commands like `ls` or `pwd`!

You can disconnect by typing `exit` and hitting Enter.

## Step 3: Installing Python, Pip, and Git

Oracle Linux uses the [YUM package manager](http://yum.baseurl.org/), which is roughly similar to Homebrew on a Mac.

To install Python 3 and Pip 3, run:
```
sudo yum install python3
```

If that worked correctly, you should be able to run `which python3` and `which pip3` and it will print out the paths to the executables.

To install Git, run:
```
sudo yum install git
```

Now if you run `git status` from the root directory, you should get an error message saying that it is not a git repository.

## Step 4: Cloning the Flask App and Installing Dependencies

As long as the repository is public on GitHub, this should work the same as cloning any other repository.  Just a typical:
```
git clone <repository_link>
cd <repository_name>
```
So, for example, I ran:
```
git clone https://github.com/hoffm386/capstone-flask-app-template.git
cd capstone-flask-app-template/
```

From the repository, you'll want to install of the Python package dependencies.  I personally did not use `conda` or `virtualenv` because I'm only planning to use this instance to run a single Python project, but you could set it up differently if you wanted to have different versions of various packages available.

To install all packages specified in `requirements.txt`, run:
```
sudo pip3 install -r requirements.txt
```

It will give you a warning message for the reason mentioned above (it's not a best practice to install Pip packages globally rather than using a `conda` or `virtualenv` environment) then proceed to install all of the necessary packages.

To test that your Flask app can run without errors, test out running it:
```
export FLASK_ENV=production
python3 app.py
```

You won't be able to test it in a browser until the network settings are configured, though!

## Step 5: Configuring Network Settings

As far as I can tell, you must use two different interfaces to specify which ports should accept incoming requests.  For these examples, we are assuming that the default port for Flask is used (port 5000).

First, configure from the "console" in the browser where you manage cloud instances.  Do this by navigating to "Networking" --> "Virtual Cloud Networks" in the main menu, selecting your network (should be only one, created by default), selecting "Security Lists" in the bottom left menu, selecting "Default Security List", then clicking the blue "Add Ingress Rules" button.  In that pop-up window, enter `0.0.0.0/0` in the SOURCE CIDR field and 5000 in the DESTINATION PORT RANGE field, then click the blue "Add Ingress Rules" button at the bottom.

Second, configure the firewall on the server itself to accept requests on that port.  Making sure that you are SSH-ed in to your instance (seeing the prompt with `opc@instance`), run the lines:
```
sudo firewall-cmd --zone=public --permanent --add-port=5000/tcp
sudo firewall-cmd --reload
```

Now, if you run the code to start your Flask app again, you should be able to access it in your local browser!  Just type the public IP address followed by the port, e.g. `http://129.146.133.106:5000/`

## Step 6: Using `tmux` to Run Indefinitely

With the current setup, the web server only runs as long as the SSH session is live.  This is fine even for demo-ing at showcase, but if you actually want the website to work whenever someone wants to view it, the web server needs to be detached from the SSH session.

The typical tool used for this is [`tmux`](https://tmuxguide.readthedocs.io/en/latest/tmux/tmux.html)

Just once, you need to install `tmux`:
```
sudo yum install tmux
```

After that, the process for starting your cloud-hosted web server is:
```
tmux
export FLASK_ENV=production
python3 app.py
```

Then press `control-b`, then release both keys, then press `d`, in order to detach from the `tmux` session.

Now your web server will keep running, even if you log out of SSH!

If you want to log in and stop the web server, or inspect the logs, first SSH back in, then run `tmux attach`.
