# IDS706-Project1-Yutong

### Usage
##### To run in docker
`docker build -t <image_name> .`
`docker run -d --name <docker_process_name> -p 80:80 <image_name>`
##### To kill the deamon process in docker
`docker ps // check current process`
`docker kill <image_name>`
`docker ps`