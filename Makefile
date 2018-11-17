PROJECT_NAME=crawler
ENV=dev

LINUX_PACKAGE_MANAGER=apt-get

REQ_FILE=requirements.txt

freeze_requirements:
	pip freeze > $(REQ_FILE) 

install_requirements:
	pip install -r $(REQ_FILE)

run:
	python crawler.py -u $(url) -t $(format) -o $(output)

test:
	python -m unittest discover unittesting

deps:
    sudo apt install python3.7 python3-pip virtualenv
    virtualenv -p python3.7 .env
    source .env/bin/activate
    pip install -r $(REQ_FILE)