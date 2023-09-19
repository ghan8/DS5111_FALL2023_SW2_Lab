# DS5111_FALL2023_SW2_Lab

What did you have to do to get make to work?
I had a multiple pre-work / update steps getting make to work. sudo apt update implemented some security updates. Somewhere along the way I think I lost VIM, so I had to reinstall that as well. While creating the venv I I need to install python-venv for python3.10. I also had to clean the venv from the directory at one point because somewhere along the way I created the venv while working through the required code for the make file. Also including the commands on one line was a point of troubleshooting. At one point the AWS instance required a reboot. 

Similarly for python3 -m venv env, what did you have to do? (How likely are you to have guessed that without their clear error message?)
For the virtual environment port I needed to install python-venv for 3.10, I would not have guessed that without googling it. Additionally, a AWS reboot was required at one point which I also would not have guessed. 

Both the pip install on the requirements.txt, and the call to run bin/clockdeco_param.py should be activating the virtual environment first. In other words, there are two bash commands separated by a ;, the first of which activates. Why can't we just do that on a separate line? 
In other words, why do we have to do that in one line and separate the commands with a ;?  Because we want to execute within the activated environment. If we did not implement on the same line the command desired to be executed within the venv would be executed in standard bash. The semicolon essentially enables sequentially chained execution.

As it is, both the env and tests jobs run differently in that only one runs if the directory exists. This is as intended and all is well. What do you think about the job run? What would happen if you accidentaly had a file called run in your directory? What can we do to fix this? 
I think the run would error out, but I would need to do some more experimenting to be certain. We can add an if run exist conditional to prevent running when without the presence of run. 

The code provided to you for the test file starts with two lines, seemingly to append something to sys.path. What is the purpose of these lines?
