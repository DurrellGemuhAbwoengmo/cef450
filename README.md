# cef450
setting up environment 
  
  Step 1: Updating all your software
    $ sudo apt-get update
  
  Setup your Python environment — Python 3
    $ cd ~
    $ wget https://bootstrap.pypa.io/get-pip.py
    $ sudo python get-pip.py
    $ sudo pip install virtualenv virtualenvwrapper
    $ sudo rm -rf ~/get-pip.py ~/.cache/pip
    
  Once we have virtualenv and virtualenvwrapper installed, we need to
update our ~/.bashrc file to include the following lines at the bottom of
the file:
    $ nano ~/.bashrc (then in the file that opens, go to the bottom and paste the following)
        # virtualenv and virtualenvwrapper
        export WORKON_HOME=$HOME/.virtualenvs
        source /usr/local/bin/virtualenvwrapper.sh
        
   After editing our ~/.bashrc file, we need to reload the changes:
      $ source ~/.bashrc
      
   Creating your Python virtual environment
use this command to create a Python 3 virtual environment:
      $ mkvirtualenv ws -p python3
      $ workon ws
      
      install pandas and cherrypy
      These libraries can be installed using the pip command:
        >> pip install pandas
        >> pip install CherryPy
        
        
     run with
      >> python app.py
