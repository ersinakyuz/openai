#!/bin/bash
if python3 --version ;
then
	pip3 install openai
	pip3 install requests

else
	echo "No Python3 executable is found. Please install Python3 first"
fi