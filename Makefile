win-pre-expert:
	win-config\python.exe -m pip install gnureadline

win-pre-ez:
	win-config\python.exe common-config\get-pip.py
	win-config\scripts\wheel.exe install gnureadline

win-run: interpreter.py
	 win-config\python.exe interpreter.py

mac-pre-expert:
	python3 -m pip install gnureadline

mac-pre-ez:
	chmod u+x mac-config/brew.sh
	sh brew.sh
	brew install python3
	python3 common-config/get-pip.py
	python3 -m pip install gnureadline

mac-run: interpreter.py
	python3 interpreter.py

win-clean:
	del win-config\Scripts

help:
	echo "\n"
	echo "win-pre-ez: this will automatically install all required packages including Python, pip, etc... on a windows machine \n"
	echo "win-pre-expert: this will only install required PyPI packages on the windows machine \n"
	echo "win-run: this will run the program on a Windows platform \n"
	echo "mac-pre-ez: this will automatically install all required packages including Python, pip, etc... on a macOS machine \n"
	echo "mac-pre-expert: this will only install required PyPI packages on the macOS machine \n"
	echo "mac-run: this will run the program on a macOS platform \n"
