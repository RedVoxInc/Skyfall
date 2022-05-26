# Skyfall

Check out the [Skyfall Docs](https://redvoxinc.github.io/Skyfall/) for more guidance on how to run the Skyfall code. 

## Description

The Skyfall data is a high-quality dataset that showcases the RedPandas library for processing smartphone data collected 
with the [RedVox Infrasound Recorder app](https://www.redvoxsound.com).

In essence, Skyfall is an event where a smartphone fell from a high altitude and landed on the ground. A balloon hoisted a commercial, off-the-shelf, smartphone to a height of 36 km (around 119,000 feet) and purposely burst
to let the smartphone freefall (hence the name _Skyfall_). As the smartphone fell back to Earth, it recorded its 30 minute 
descent using the app. You can read more about this projects 
in [Skyfall: Signal Fusion from a Smartphone Falling from the Stratosphere](https://www.mdpi.com/2624-6120/3/2/14).

Using the data from this event, RedPandas is able to produce several products.


## Getting started 

### 1. Download the RedVox Skyfall data
To begin, download the Skyfall dataset from [the Redvox website](https://redvox.io/#/reports/3f3f). Next to "Additional Products", you will
find a link to download the data. Click over _API 900 Data Distribution_. A zip file will start to download.

Visit [RedVox](https://www.redvoxsound.com/) for more information on infrasound collection with a smartphone.

### 2. Set up your software environment

#### 2.1. Clone the Skyfall repository
In a Terminal, use the following command:
```shell
git clone git@github.com:RedVoxInc/Skyfall.git
```
For more details, please check: [Instructions on how to clone a GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository).

#### 2.2. Install requirements

To install the necessary requirements:
```shell
pip install -r /path/to/requirements.txt
```

### 3. Run the Skyfall example
#### 3.1. Update the Configuration File
In the newly cloned Skyfall repository, open `skyfall_config_file.py` and update the value of `SKYFALL_DIR` on line 5 to match the directory 
where you downloaded the Skyfall data (the directory will have a folder named "api900").

An example path for Linux/Mac:
```python
SKYFALL_DIR = "/path_to/your/downloaded_data"
```

An example path for Windows:
```python
SKYFALL_DIR = "\\path_to\\your\\downloaded_data"
```
#### 3.2. Run the code
Run the `skyfall_intro.py` file.  This will create some products for you to view.

For more RedPandas products, run the `run_all.py` file in the `lib/` directory.

You may view and run the specific example functions (`skyfall_*.py`) in the `lib/` directory.

## Issues
Please feel free to submit issues and bugs on the GitHub [issue tracker](https://github.com/RedVoxInc/Skyfall/issues).

## Dependecies

You will mainly need the [RedVox SDK](https://github.com/RedVoxInc/redvox-python-sdk#redvox-python-sdk) (redvox >=3.1.7), 
[RedPandas](https://github.com/RedVoxInc/redpandas#redpandas) (redpandas >= 1.3.3),
and [Libquantum](https://github.com/RedVoxInc/libquantum#libquantum) (libquantum >= 1.3.0) libraries.

The SDK should install the required numpy and matplotlib versions.