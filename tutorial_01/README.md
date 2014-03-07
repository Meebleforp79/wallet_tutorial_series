![1DAit5zwR1BFDW9JuKbPchCesq23qS9ZLp](https://raw.github.com/Joshka-Randora/wallet_tutorial_series/master/assets/images/1DAit5zwR1BFDW9JuKbPchCesq23qS9ZLp.png?raw=true)

*1DAit5zwR1BFDW9JuKbPchCesq23qS9ZLp*

This EBook Tutorial Series is released on a "Pay What You Want" model.

--------------------------------------------------------------------------------

# [Tutorial 01: *Proof of concept*](./tutorial_01/) 2014-03-03

Using Python 2.7, bitcoin-rpc, and PyQT to poll bitcoind and insert the results of getinfo into a GUI.

--------------------------------------------------------------------------------

## Platform information

**Tested OS** *Ubuntu 13.10*

**Tested Language** *Python 2.7*

--------------------------------------------------------------------------------

## Preface

This tutorial demonstrates the minimum requirements to make a bitcoin wallet.

This tutorial doesn't acutally do anything it is only a proof of concept showing that the technologies work.

We can build upon these concepts to add modules in future tutorials

Demonstrated technologies include:

* **bitcoind** *The daemon our wallet will communicate with in order to get info about the bitcoin environment*

* **Python 2.7** *Our language of choice for this project*

* **bitcoin-rpc** *The protocol our wallet uses to speak with bitcoind*

* **PyQt** *The library of choice for building our wallet's user interface*

--------------------------------------------------------------------------------

## Step 1

### Clone this project

clone this code to your machine

    $ mkdir ~/git

    $ cd ~/git

    $ git clone https://github.com/Joshka-Randora/wallet_tutorial_series.git

## Step 2

### Install Dependencies

#### python-bitcoinrpc

    $ git clone https://github.com/jgarzik/python-bitcoinrpc.git

Follow instructions here: https://github.com/jgarzik/python-bitcoinrpc 

#### python-qt4

    $ sudo apt-get install python-qt4

## Step 3

#### Make the following changes to this code:

    self.username	= "rpc_username" #change to match your username in ~/.bitcoin/bitcoin.conf
    self.password	= "rpc_password" #change to match your password in ~/.bitcoin/bitcoin.conf

## Step 4

### Run the Bitcoin Daemon

    $ bitcoind -server

#### Make sure RPC is working

    $ bitcoind get info

## Step 5

### Run this tutorial'ss code

    $ python ./wallet_tutorial_series/tutorial_01/main.py

Hopefully, you'll see a user interface pop up with the same info as in **Step 3**

--------------------------------------------------------------------------------

# Explanation of Code

## main.py

This is the only file in this tutorial. It has 4 parts to it: **Main()**, **Command()**, **Configuration()**, and **UI()**

Since this is a bitcoin wallet tutorial and not a Python, or PyQt tutorial.
I will spend most of my time explaining the aspects pertaining to bitcoin.

### class Command

This class is what communicates with **bitcoind**.

Initialize the configuration...

    self.conf = Configuration()

and Create a connection to **bitcoind**...

    self.access = AuthServiceProxy(self.conf.get_uri())

We can use *self.access* to pass arguments to **bitcoind**

    self.info = self.access.getinfo()

Now self.info has the same information you would have by executing **$ bitcoind getinfo** from the command line.
The only difference is, it's now in useable form, which we will see in **UI()**.

### class Configuration()

This class provides our **BitcoinRPC** with the needed user/server information to connect.

It's usually not a good idea to hardcode authentication variables into the source, but this is only a proof of concept.
We will fix this problem in the next tutorial.

### class UI()

This isn't a tutorial about using PyQt, so we aren't going to spend a great deal of time explaining the aspects of PyQT here.
What we are going to do is show how to use the data from **Configuration()** and display it.

#### Fetch Info from bitcoind

    command = Command()
    info = command.get_info()

It's pretty simple. The rest of the code in **UI()** just reads info and dynamically creates grids and interface widgets to put that info.

#### Get other information from the server

Notice in **Command()** there is also a *list_accounts(self)* method.

Change:

    info = command.get_info()

to:

    info = command.list_accounts()

and see what happens

--------------------------------------------------------------------------------

This isn't a wallet just, yet. But now we have the pieces in place to make one.

