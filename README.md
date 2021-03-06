# About
This is my attempt to gain insights from [<strong>`Stackoverflow Developer Survey in 2020`</strong>](https://insights.stackoverflow.com/survey/2020). They have been doing it since 2011, but currently I'm focusing on 2020 first. In fact, I'm trying to compare the trends in Indonesia with what's happening to the rest of the world. The data for each year can be obtained [<strong>`here`</strong>](https://insights.stackoverflow.com/survey).

# Clone
In any case you're interested to play around on your machine, just do the following inside the terminal:

```bash
cd ~
git clone https://github.com/ledwindra/stackoverflow-survey.git
cd stackoverflow-survey
```

# Virtual environment and install requirements
You may need a virtual environment in case you don't want to mess up with the existing modules inside your machine because here we need external modules such as [<strong>`pandas`</strong>](https://github.com/pandas-dev/pandas), [<strong>`matplotlib`</strong>](https://github.com/matplotlib/matplotlib), and [<strong>`seaborn`</strong>](https://github.com/mwaskom/seaborn). Just do the following inside the terminal:

```bash
python -m venv .venv # .venv can be changed to whatever it is as you like
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt # you're all set
```

Just type and press `deactivate` when you want to exit from the virtual environment. You can just install the requirements if you don't care with virtual environment at all :smile:

# Let's get it on
Now we're ready to explore the data. There are two main components here. First, it's the Python script that will be used in the notebook. It's located inside [<strong>`src/stackoverflow.py`</strong>](https://github.com/ledwindra/stackoverflow-survey/blob/master/src/stackoverflow.py). Its task is to manipulate the DataFrame and create visualization methods. The main purpose is to make the notebook looks cleaner. The notebook itself is located inside [<strong>`index.ipynb`</strong>](https://github.com/ledwindra/stackoverflow-survey/blob/master/index.ipynb).

# Contribute or complain
You can contribute to the analysis by editing this repo inside your branch and making a pull request. Moreover, you can also file [<strong>`issues`</strong>](https://github.com/ledwindra/stackoverflow-survey/issues) in case you have any questions or find bugs.

# Enjoy
I hope you enjoy this repository and cheers! :beers:
