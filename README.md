<p align="center"><img alt="banner" src="https://github.com/Virag007/Performance-Enhancer/blob/main/media/banner.png" /></p>
<br />

# Performance Enhancer & Tracker (PET)

[![Track](https://img.shields.io/badge/Track-Progress-%23ff4da6)](https://github.com/Virag007/Performance-Enhancer/releases)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-4DFF4D)](https://github.com/Virag007/Performance-Enhancer/issues)
[![Pull Request](https://img.shields.io/badge/PRs-Welcome-ff471a)](hhttps://github.com/Virag007/Performance-Enhancer/pulls)
[![MIT license](https://img.shields.io/badge/Licence-MIT-ff3399)](https://lbesson.mit-license.org/)
![LinesOfCode](https://img.shields.io/badge/Lines%20%20of%20Code%20[LOC]-550%2B-%233390ff)

It is a self-competitive CLI tool that will enhance your performance by keeping track of the threshold you set. You can also add your competitor with whom you want to compete. It will generate daily and monthly leaderboards as well. You can take a challenge of (say 30 days), set your threshold, and start tracking your daily progress. By the end of your resolution, you'll see a better you (mark it).

## Platform Supported

<img align="left" alt="Linux" width="64px" height="64px" src="https://github.com/Virag007/Performance-Enhancer/blob/main/media/linux.png" />
<img align="left" alt="Linux" width="64px" height="64px" src="https://github.com/Virag007/Performance-Enhancer/blob/main/media/windows.png" />

<br />
<br />
<br />
<br />

## Installation

**Step-01:** Clone the github repo and traverse to the mentioned folder.
<br />
```git clone https://github.com/Virag007/Performance-Enhancer.git && cd Performance-Enhancer```
<br /><br />
**Step-02:** Install the required python library to smoothly run the tool.
<br /> 
```pip install -r requirements.txt``` or ```pip3 install -r requirements.txt```
<br /><br />
**Step-03:** View the usage
<br />
```python3 PEtrack.py --help```

```
usage: use "PEtrack.py --help" for more information

Title: Performance Enhancer and Tracker

Author: Parag Thakur (aka Virag)

Twitter Handle: @_virag007

Description: It is a self-competitive CLI tool written in python that will enhance your performance 
by keeping track of the threshold you set. You can also add your competitor with whom you want to 
compete. It will generate weekly and monthly leaderboards as well. You can take a challenge of (say 
30 days), set your threshold, and start tracking your daily progress. By the end of your resolution, 
you'll see a better you (mark it)

optional arguments:
  -h, --help   show this help message and exit
  -f, --flush  Wipe out the previous activities and exit
  --version    Shows the version information and exit

``` 

**Step-04:** ```python3 PEtrack.py```

You have two options given either compete with yourself or with your friend. You need to add attributes name (i.e., your subject for which you want to set limit and track). After adding all the attribute name type **exit** and you'll out from the process.

<br />

## Using Docker

**Step-01:** Clone the github repo and traverse to the mentioned folder.
<br />
```git clone https://github.com/Virag007/Performance-Enhancer.git && cd ./Performance-Enhancer/DockerImage```
<br /><br />
**Step-02:** There are some script file to which you need to give execution permission.
<br/>
```chmod +x buildimage.sh startContainer.sh```
<br /><br />
**Step-03:** Run the buildimage.sh script to build your custom docker image of python3 from the context of DockerFile and create the container. All this will be done automatically by simply running the mentioned script file.
<br />
```./buildimage.sh```
<br /><br />
**Step-04:** Now your container is created and you may need to start the container in attach mode by simply executing the mentioned script.
<br />
```./startContainer.sh```

<br />

## Features

1. Track your daily progress with yourself and with your friend as well.
2. Interactive support to input the daily statistics.
3. Get leaderboard at the end of your resolution.
4. Ability to view the previous day stats interactively.
5. Cross-Platform support (i.e., Windows and Linux).
6. Ability to set the threshold to track everyday stats.
7. At the end of the resolution day get every personalised details separately.

<br />

## Contributions

Your feedback and contributions will be much appreciated. :beers::beers:

<br />

## Connect with me
**Name: Parag (aka Virag)**
<br />

**Social Handles:** &nbsp;
[<img alt="watercaterpillar.blogspot.com" width="22px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/globe.svg" />](https://watercaterpillar.blogspot.com/)
[<img alt="@_virag007 | Twitter" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/twitter.svg" />](https://twitter.com/_virag007)
[<img alt="parag0thakur | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />](https://www.linkedin.com/in/parag0thakur/)
[<img alt="v_ir_ag | Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />](https://www.instagram.com/v_ir_ag/)
[<img alt="parag888 | Facebook" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/facebook.svg" />](https://www.facebook.com/parag888)

<br />
<img src="http://ForTheBadge.com/images/badges/made-with-python.svg" />
