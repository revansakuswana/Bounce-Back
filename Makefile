build:
	docker build . -t hldtux/pygame

xhost:
	xhost +	

run-linux:	xhost
	docker run --privileged -it --rm \
	--cap-add=SYS_PTRACE \
	-u 1000:1000 \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e DISPLAY \
	-v /run/dbus:/run/dbus \
	-v /dev/shm:/dev/shm \
	--device /dev/snd \
	--device /dev/dri \
	-e PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native \
	-v ${XDG_RUNTIME_DIR}/pulse/native:${XDG_RUNTIME_DIR}/pulse/native \
	-v /run/user/1000/pulse:/run/user/1000/pulse \
	-v /var/run/dbus:/var/run/dbus \
	-v ~/Downloads:/home/docker \
	hldtux/pygame

open-socat:
	socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"

run-mac:	xhost
	IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
	docker run --privileged -it --rm -u 1000:1000 \
	--cap-add=SYS_PTRACE \
	-v /tmp/.X11-unix:/tmp/.X11-unix \
	-e DISPLAY=$IP:0 \
	-v ~/.config/pulse:/run/user/1000/pulse \
	hldtux/pygame

run-windows:
	docker run --privileged -it --rm --cap-add=SYS_PTRACE -u 1000:1000 -e DISPLAY=127.0.0.1:0.0 -v %userprofile%\Downloads:/home/docker hldtux/pygame
