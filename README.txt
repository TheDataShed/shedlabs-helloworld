Welcome to the DataShed Apache Spark Labs 'Hello-World' docker program.

Here's what you need to do to get started...

Please ensure HyperV/VMWare is not running on your laptop.

Windows & OS X

	1) Download Docker here: https://docs.docker.com/windows/step_one/
	   I had some issues connecting to the Virtual Box VM via the Dcoker Quickstart Terminal.
           If you do too you may need to uninstall Virtual Box and re install the latest version (5.0.16) which 
           you can find here: https://www.virtualbox.org/wiki/Downloads

	2) Sign up for a Docker Hub account here: https://hub.docker.com/

	2) If you do not have Git for Windows download it here: https://git-scm.com/download/win

	3) Clone this repository

	4) Open the Docker Quickstart Terminal and navigate to the cloned repository

	5) Enter this command from the root of the project:
		
		docker-compose-up

	That should be it. You now need to find the ip docker machine is running on and go to port 8000 in a browser i.e 192.168.99.100:8000.
	You can find it at the top of the terminal under the image of the Docker whale. OR you can run
	'docker-machine ip'.

	See Other Docker Commands below incase you are interested in learning more/having issues.

Linux (Ubuntu)

	1) Download Docker here: https://docs.docker.com/engine/installation/linux/ubuntulinux/

	2) Sign up for a Docker Hub account here: https://hub.docker.com/

	3) Install Git 'apt-get install git' (if not running Ubuntu find install command here: https://git-scm.com/download/linux)

	4) Clone the Datashed Labs repo with this URL https://the-datashed.visualstudio.com/DefaultCollection/_git/DataShed%20Labs

	5) Enter these commands from the root of the project:

		docker build -t datashed/web_demo . (don't forget the full stop!)
		
		docker-compose-up

	That should be it. You now need to find the ip docker machine is running on and go to port 8000 in a browser i.e 192.168.99.100:8000.
	You can find it at the top of the terminal under the image of the Docker whale. OR you can run
	'docker-machine ip'.

Other Docker Commands

	docker ps - see running containers

	docker images - see all your docker images

	docker rm $(docker ps -a -q) - delete all containers

	docker rmi $(docker images -q) - delete all docker images

	docker run -ti {image name} /bin/bash - start bash prompt on a new container

	docker exec -ti {container name} /bin/bash - start bash prompt on existing container



		