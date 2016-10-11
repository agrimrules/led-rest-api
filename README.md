# led-api

REST Api to write to LED badge
all credit for the LED library goes to this [repository](https://github.com/DirkReiners/LEDBadgeProgrammer) <br>
I just containerized it and made a REST Api around it using the Flask framework <br>

## Getting Started

If you want to run the app locally make sure you do a `pip install -r requirements.txt`<br>
also ensure that you have either `Pillow` or `PIL` installed, as these are dependencies required by the B1248 Led Library<br>
Once you have finished installing dependencies you will need a `settings.conf` file which stores databse credentials in the following format<br>
```
user=''
password=''
databse=''
host=''
```
<br>
Do note that the `settings.conf` is ignored both in `.gitigore` and `.dockerignore` as credentials should not be a part of source code or built container images <br>

### Running natively
Once you have both the `settings.conf` and the dependencies installed. simpy run <br> `python api.py` to start the app.<br>
The request should be a `POST` request at `http://<device-ip>:5000/led` with a payload like below.<br>
```
{
  "message":"<Enter your message>"
}
```

### Running in a container
Convinience scripts `build.sh` and `run.sh` have been provided. <br>
When executing `build.sh` do change the tag after `-t` per your convinience. and while executing `run.sh` make sure the correct port is mounted at `-v`. If you are unsure of where the LED badge is connected. <br>
simply `$sudo apt-get install hwinfo` && `$hwinfo` to get the list of attached devices. <br> The badge will most probably be under `dev/ttyUSB*` and will show as `Prolific PL2303 Serial Port`<br>
Make sure the correct port is mounted as it defaults to `dev/ttyUSB0` in the container.<br>
You might need to `chmod 666 <led-port>` before mounting it as the docker user might not have enough permissions even tough the `--privileged` tag is used<br>
