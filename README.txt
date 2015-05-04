Readme file for Project 2 of the Udacity Full Stack Web Developer Nanodegree, Version 1.0 April 29 2014.


For Project 2, a Python module uses the PostgreSQL database to keep track of players and matches in a game tournament.


The game tournament uses the Swiss system for pairing up players in each round: players are not eliminated, and each player is be paired with another player with the same number of wins, or as close as possible.
  

A virtual machine (VM) is used to run a database server and a web app that uses it. The VM is a Linux server system that runs on 
top of your own computer.  You can share files easily between your computer and the VM.


The Vagrant software is used to configure and manage the VM. 


The following outlines the tools you'll need to install to get the VM running:

1) Git:

If you don't already have Git installed, download Git from git-scm.com. Install the version for your operating system.

On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash).
(On Mac or Linux systems you can use the regular terminal program.)

You will need Git to install the configuration for the VM. If you'd like to learn more about Git, take a look at our course about Git and Github.


2) VirtualBox:

VirtualBox is the software that actually runs the VM. 

You can download it from virtualbox.org, at the following link: https://www.virtualbox.org/wiki/Downloads 

Install the platform package for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

Ubuntu 14.04 Note: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.


3) Vagrant:

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  
You can download it from https://www.vagrantup.com/downloads. Install the version for your operating system.

Windows Note: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.
Use Git to fetch the VM configuration

Windows: Use the Git Bash program (installed with Git) to get a Unix-style terminal.
Other systems: Use your favorite terminal program.

From the terminal, run:

         git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack

This will give you a directory named fullstack.


4) Run the virtual machine:

Using the terminal, change directory to fullstack/vagrant (cd fullstack/vagrant), 
then type "vagrant up" to launch your virtual machine.
Once it is up and running, type "vagrant ssh" to log into it. 

This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt. 

The Vagrant VM provided in the fullstack repo already has PostgreSQL server installed, as well as the psqul command line interface(CLI).

When you want to log out, type "exit" at the shell prompt.  To turn the virtual machine off (without deleting anything), type "vagrant halt". If you do this, you'll need to run "vagrant up" again before you can log into it.


5) For project 2, in order to run the files a database named tournament was created:

The files are located in the "tournament" subdirectory of your VM’s /vagrant directory inside the virtual machine.  
Using the terminal, change directory to "tournament" by typing in: "cd /vagrant/tournament".

To create the database, the create database command in psql was used. The database was named "tournament".

psql  was used to connect to the new database by typing in "psql tournament", then the tables in the database were created 
from the SQL statements written in tournament.sql. 

This was done by using the command "\i tournament.sql" to import the whole file into psql.  Then "\q" to exit.



6) The files and commands to be used: 

The files are located in the "tournament" subdirectory of your VM’s /vagrant directory inside the virtual machine.  
Using the terminal, change directory to "tournament" by typing in: "cd /vagrant/tournament".


At the command line, type "python tournament_test.py" to test the code.


The contents of the files are described below:

The database being used is named "tournament".
There are three files associated with this project: tournament.sql, tournament.py, and tournament_test.py.

The file "tournament.sql' provides the database schema, in the form of SQL create table commands.  These identify the tables created. 

The file "tournament.py" is the code for the tournament module that identifies several functions(listed below) for the swiss pairing tournament that are called by the "tournament_test.py" file.

The file tournament_test.py was provided by Udacity.  This file contains unit tests that test the functions written in tournament.py. 


 


The functions within the "tournament.py" file are as follows:


1)registerPlayer(name)
Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

2)countPlayers()
Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

3)deletePlayers()
Clear out all the player records from the database.

4)reportMatch(winner, loser)
Stores the outcome of a single match between two players in the database.

5)deleteMatches()
Clear out all the match records from the database.

6)playerStandings()
Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

7)swissPairings()
Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.

