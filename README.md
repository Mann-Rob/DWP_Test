# DWP Test
Flask Api for DWP Test

This Program is written in Python 3.6 with a few other libraries added on to perform specialist tasks
The only user requirements are for the installation of virtualbox and vagrant, on the users machine. 

The included playbooks and scripts will handle the installation of additional dependencies but it should 
be noted that these dependencies are installed onto the virtual machine therefore no changes other than those 
specified should occur to the users PC. 

In a production environment these tasks would not be required and deployment and builds and tests can be 
automated via jenkins. 

#Requirements
####Virtualbox [6.0.14]
[Virtualbox 6.0.14]: https://download.virtualbox.org/virtualbox/6.0.14/VirtualBox-6.0.14-133895-Win.exe

####Vagrant [2.2.6]
[Vagrant 2.2.6]: https://releases.hashicorp.com/vagrant/2.2.6/vagrant_2.2.6_x86_64.msi

#Set Up Guide
To Set up the app you need to clone the code from the [git repository]: https://github.com/Mann-Rob/DWP_Test

Using the command line in windows/terminal window in ubuntu navigate to the directory you cloned the project too
ie. cd /d "D:\Projects\Python Projects\DWP_Test"

Type the following command into the command line/Terminal 
```
vagrant up 
```

This will download and automatically configure an ubuntu 18.10 virtual machine and create a link between the app directory
and the virtual machine so local code changes will automatically by applied to the virtual environment. 

Type the following command into the command line/Terminal 
```
vagrant ssh
``` 
(If prompted for a password the default is "vagrant", in a production environment this would be secured using 
ssh keys.) 

once you have connected to the vagrant box you need to navigate to the DWP_Api directory using the following command
```
cd opt/dev/DWP_Test
```
This will leave you in the apps route directory to start the API you need to type the following command
```
make run_dwp_api
```
This will start the app and it will be available on the address http://127.0.0.1:5000/

#Unit Tests
The Code comes with its own set of built in unit tests which run of a seperate command 
** Note it is not possible to run the unit tests on the same command line/terminal window that the app is 
currently running as it locks the command window it is however possible to run the tests while the app is 
running by opening a new terminal and following the steps highlighted above with the following change. 

instead of 
```
make run_dwp_api
```
Use 
```
make run_dwp_api_unit_tests
```

#Breakdown of endpoints 
The API provides the following three end points for use: 

###http://127.0.0.1:5000/
The Landing Page this will return the users currently within 50 miles of London (Lat: 51.30, Long: 0.5)
and those users who live around london. 

###http://127.0.0.1:5000/health_check
Returns a status 200 response when called (Used by unit tests to confirm that the API is available)

###http://127.0.0.1:5000/get_in_radius/\<radius>
Replace \<radius> with the desired value to return users for different radii around london.   
