![1DAit5zwR1BFDW9JuKbPchCesq23qS9ZLp](https://raw.github.com/Joshka-Randora/wallet_tutorial_series/master/assets/images/1DAit5zwR1BFDW9JuKbPchCesq23qS9ZLp.png?raw=true)

*1DAit5zwR1BFDW9JuKbPchCesq23qS9ZLp*

This EBook Tutorial Series is released on a "Pay What You Want" model.

--------------------------------------------------------------------------------

# [Tutorial 02: *Read settings from bitcoin.conf*](./tutorial_02/) 2014-03-06

Here we start separating components into their own modules. 
Then we focus on the Configuration modual to read from ~/.bitcoin/bitcoin.conf to read rpc connection information. 
This makes it possible to run the wallet without hardcoding username and password info into the source code.

--------------------------------------------------------------------------------

## Platform information

**Tested OS** *Ubuntu 13.10*

**Tested Language** *Python 2.7*

--------------------------------------------------------------------------------

## Preface

This tutorial demonstrates how to read the *~/.bitcoin/bitcoin.conf* file so 
this information doesn't have to be hard coded into the source code.

This improves security and makes the code distributable to multiple users.

You will also notice the modules have been broken up into multiple files. 
This is in preparation of separation of form and function. 
More on this in a future tutorial.

We are mostly going to be concerned with the **Configuration()** modual *./configuration.py* 
for the sake of this tutorial. 

Demonstrated technologies include:

* **SafeConfigParser** *The library which will read and parse ~/.bitcoin/bitcoin.conf*

--------------------------------------------------------------------------------

## Step 1

### Clone this project

clone this code to your machine

    $ mkdir ~/git

    $ cd ~/git

    $ git clone https://github.com/Joshka-Randora/wallet_tutorial_series.git

## Step 2

### Run the Bitcoin Daemon

    $ bitcoind -server

#### Make sure RPC is working

    $ bitcoind getinfo

## Step 3

### Execute this tutorial's code

    $ python ./wallet_tutorial_series/tutorial_02/main.py

Hopefully, you'll see a user interface pop up with the same info as in **Step 2**.
This should be identical to *tutorial_01*

--------------------------------------------------------------------------------

# Explanation of Cod

## configuration.py

This file is the focus of this tutorial. 
Compare it with **tutorial_01**'s **main.py** - **Configuration()** class to understand 
better what is going on here. 

### New Parameter: *altcoin*

First, you'll notice **Configuration()** accepts a *string* called **altcoin** as 
a parameter.
This is for modularity, in the future this can be used to get "litecoin's" 
configuration file as well as bitcoin's

### New Member Function: *read()*

Next, you'll notice a new member function **read(self)**.
This will look for **altcoin**'s configuration file. It will read it and turn 
it into a datastructure we can use.

### What is: *class Fake_Head()*?

The Bitcoin configuration doesn't comply with the standards expected from 
**ConfigParser**, so this is an attempt to fake it by first attaching a fake header 
then parsing it normally.

## command.py

The only other thing we need to worry about is changing **command.py**'s 
**self.configuration = Configuration("bitcoin")** to reflect the change in 
**configuration.py**

## Success

If everything went as planned, executing the script should provide the same result 
as in **tutorial_01**, except the configuration file is being dynamically read as 
opposed to having the information hard coded into our app.
