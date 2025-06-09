how do you pass build arguments to docker file

FROM busybox
USER ${username:-some_user}
ARG username
USER $username


docker build --build-arg username=what_user .