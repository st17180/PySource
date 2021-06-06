# READ. ME.
check the issues tab, the wiki tab and the commits tab. evidence of testing, feedback, documentation and continuous improvement from them are ALL THERE. 
Implications are at the BOTTOM on this file. and the use of a project manager IS this file as well as the rest of this repository.

# PySource
A system independent resource monitor written in python with psutil.

## Installation

### windows
make sure an up to date version of python is installed
use PIP to install the "psutil" package
download and extract the ZIP under the green "code" button
run the cli.py! (i recomend against running it in a windows terminal as it apparently can get visually buggy, the best use case ive seen is in something like VS code)

to update you will need to redownload the ZIP (git is available for windows but is outside the scope of this wiki)

### UNIX
make sure up to date versions of python pip and git are installed
in shell run `pip instal psutil --user` (the user flag may not be needed feel free to adjust as aproprate for your system/use case) `git clone https://github.com/st17180/PySource.git` `cd PySource` 
to run just give python the path to `cli.py` so if your in the PySource directory just `python cli.py`.

to update you can just go back to `PySource` directory and `git pull`

## The Idea
A program to view system information like cpu/memory/disk usage. the user will be able to save a copy of the currently displayed info, adjust how the info is shown etc. through a CLI for users, or to use the main as they want in their own code

## Rescrictions
depend on as few external librarys as resonable, just one! psutil 👍

### Windows users read me
depending on how python was installed to the system, it may need to be run with administrator privilages. understandably seen as a security flaw this is nothing i can fix and is the result of mismatched installations from the windows store to the python.org installer as well as 3rd party solutions 

### unix users read me
depending on the permission of your "wheel" group, the user running the CLI may need more privilages. (running this as root has never caused me issues but could easily be a security flaw and as such I cant recomend it)

## milestones 
- [X] the base functions on which the following milestones will be built to use
- [X] a CLI tester for the functions ( tester is no longer in source, see [v2 testing](https://github.com/st17180/PySource/issues/3#issuecomment-851698651)
- [X] a CLI for people to use
- [X] saving output to a file

## current plan 
- [X] create functions to update and format results into a format to be used by later sections like the GUI or CLI
  - [X] cpu usage as list of values related to the cpu core number if above 1 to list of all available cores
    - [X] add switch to change results from per core usage to total cpu usage
  - [X] mem usage as usage of total available in GB
    - [X] add switch to change results between GB and MB
  - [X] disk usage as useage of total available in GB
    - [X] add switch to change results between GB and MB
- [X] create CLI to interact with the base functions directly
  - [X] a human readable mode
    - [X] small menu to call each function with help option
  - [X] a system useable mode
    - [X] documented expected formatting for each function
  - [X] add ability to save out to a file

## testing see [Closed + Testing flags](https://github.com/st17180/PySource/issues?q=label%3ATesting+is%3Aclosed) feedback is addressed under the issues tab take a look !
- [X] base functions
  - [X] cpu
    - [X] per_cpu/total toggle
  - [X] memory
    - [X] mb/gb toggle
  - [X] disk
    - [X] mb/gb toggle
- [X] CLI
  - [X] flag to change between human readable, and system useable
  - [X] huamn readable menu to call each function
  - [X] system useable formatting for each function
  - [X] output save option

## relavent implications
functionality Does the outcome work as intended and why it matters, useability does the outcome give the user freedom does it have error prevention and recoverey and is it consistent in this, accessability, sustainability and future proofing will the outcome remain up to date and relevant.
#### how they'll be addressed in this program
for functionality each release of the program was tested to atleast have some level of the end goal in functionality, each commit pushing the program further in that direction, weather or not the program functions correctly matters because if a nonfunctional version was released and users update to it, it could break any of their projects that depend on it or their own personal use of the program may lead them to getting missinformation

for useability the program was broken up into multiple layers, firstly weather or not it was going to be used by a human or another program in the "readability" varaiable the "Monitor" class asks for, as well as the many different function specific flags such as mb or gb in disk and memory functions. the user has complete freedom over what results they get so even though the default is made for human readable formatting they could just as easily make it use the systems format, as well as error prevention and recovery, if a function is configured it will just return a string saying as such, if the CLI getts a innapropreate responce it will correct the user both error prevention, and error recovery

for accessability the program was made in a way in which it can be adapted to fit many specific needs of the end user, be it through documenting the main and allowing the end user to create their own interface easily, or having it run as plain text the programs accessability should adapt to the users system as such, think increasing font size in their terminals etc. as well as that the CLI included is documented within the program, its help message gives about all the information you could need from it( this is also apart of useability generally) and the SAVE option formats the text in a way thats easily readable in the users program of choice. being text addressing accessability directly is fairly simple where i wanted to make this program stand out was making sure it can be made to work with many different existing systems that the impaired use already

for sustainability and future proofing each outcome was planned out ( and later even rewriten) for readable code, code that depended on as little 3rd party librarys as possible ( this was taken down to just psutil ) as well as minimal lines of code and work arounds, the less the program depends on other programs the lower the chance it breaks because of them, the less moving parts in a program then lower the points of failure. and making sure this is all written in a reliably readable way ensures the program will continue to be easily adpated to any changes that might be needed in the future making it alot more sustainable

