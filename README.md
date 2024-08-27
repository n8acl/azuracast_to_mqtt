# Azuracast to MQTT

Sends the currently playing information from Azuracast to MQTT Broker.

If you are using Azuracast to run an Internet Radio Station, this script could be for you. It will take the currently playing track information for all of the stations on your Azuracast instance and send that information to an MQTT Broker to allow you to use it in other ways as needed. For example, this data could be sent to Home Assistant for display or for automations to be run when something changes.

My wife and I play Farming Simulator alot and the game has an in-game radio system that allows you to listen to music like if you were listening to a stereo in your car. It has some functionality to allow you to add Icecast radio streams from the internet to the "channel" list. I setup an Azuracast instance to allow us to add some stations of our own music to the game to listen to. It works great. I also setup some Discord bots around that to allow us to listen to the music streams as well.

I wanted a central dashboard to be able to see what all was playing on each station, so I put this together to let me add the information to Home Assistant. But the data can be used for any other application by connecting to the MQTT Broker and pulling the data from the topics.

This script is lightweight enough to be run on a Raspberry Pi (which is how I run it)

---

## How it works

The script will read your Azuracast nowplaying API endpoint and pull the now playing information for each station. It then uses the shortcode of your station to build an MQTT topic simliar to `azuracast/<station shortcode>/nowplaying`. This is where you would find the track information in MQTT.

---

## Installation

This can be run 2 ways. Either running the script directly or in Docker (recommended).

in either case, you will need to clone the repository first and enter the new directory:

```bash
git clone https://github.com/n8acl/azuracast_to_mqtt.git
cd azuracast-to-mqtt
```

Then you need to enter some information into the `config.json` file. Edit the file in your favorite editor and change the following:

- `azuracast_status_url` : this will be the url for your now playing API. It should be something along the lines of "http://ip or FQDN of azuracast/api/nowplaying"
- `mqtt_broker` : this will be the IP or FQDN of your MQTT Broker.
- `mqtt_port` : _Optional_ change this if your MQTT Broker is not on the default Port.
- `mqtt_topic_prefix` : _Optional_ change this if you want to publish to a different topic schema instead.

### Docker (Recommended)

You can either build the image locally or use the image on Docker Hub to run this in Docker.

#### Docker Hub

To use the image on Docker Hub, you can still clone the repository to get the `config.json` file and get it setup correctly.

Then edit the `docker-compose.yaml` file to set the path for the `config.json` file.

Then run the following commands:

```bash
docker-compose pull
docker-compose up -d
```

#### Building Locally

After cloning the repo and setting up the `config.json` file, you will need to build the container. There is an example docker-compose.yaml file in the repository that you can use to build the container with.

Edit the docker-compose file and add the path to the repo directory.

Then comment out this line:

```yaml
image: n8acl/azuracast_to_mqtt:latest
```

and uncomment this line:

```yaml
# build: .
```

then run the following commands.

```bash
docker-compose build
docker-compose up -d
```

Regardless of how you got the container, once it is up, check your MQTT Broker. You should have track information streaming in.

### Run the script directly

You can also run the script directly outside of Docker if you want.

Once you have the repo cloned and setup the `config.json` file, run the following commands:

```bash
sudo apt-get install screen python3 python3-pip

pip3 install -r requirements.txt --break-system-packages

screen -R azuracast_to_mqtt

python3 azuracast-mqtt.py
```

Once the script is running, you can then hit `CTRL` + `A` + `D` to exit the screen session and let it run. Then you should have data streaming to your MQTT Broker.

---

## Contact

If you have questions, please feel free to reach out to me. You can reach me in one of the following ways:

- Discord: Ravendos
- Mastodon: @n8acl@mastodon.radio
- E-mail: n8acl@qsl.net

Or open an issue on Github. I will respond to it, and of course you, when I can. Remember, this is a hobby and there are other daily distractors that come first, like work, school and family.

If you reach out to me and have an error, please include what error you are getting and what you were doing. I may also ask you to send me certain files to look at. Otherwise just reach out to me :).

---

## Change Log

- 08/26/2024: Initial Release
