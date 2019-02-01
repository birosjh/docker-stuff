# Docker Example

This is my example configuration for data science projects.  I'll likely add to it as I go, but if anyone looking at it sees any gapping erros and wants to leave an issue or something, I ain't got no problems with that.

### Things that weren't initally clear to me about Docker files

- Ports are written in the <LOCAL_PORT>:<PORT_INSIDE_CONTAINER> format
- The host in the ponyorm settings should be "db".  I had tried to put an IP address in at first and it wasn't working at all.
- If you are using port 3306 locally (like for a local SQL database), then you need to give it a different port (in my case 33061).
- Volumes are also written <LOCAL_FOLDER_NAME>:<FOLDER_INSIDE_CONTAINER>
- Be careful with the COPY command in the Dockerfile.  If you are copying the entire folder, it could mess up the volumes that you create.
-  I don't really completely understand it but the tty setting being set to true will keep your web container alive when your db container gets built.  If you don't have it, your web container will exit each time.