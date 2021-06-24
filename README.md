# Jellyfin Insert Script


Python3 script based on [this reddit post](https://www.reddit.com/r/jellyfin/comments/mkudb0/tutorial_how_to_insert_a_custom_link_into/)

## Features
- Insert links into Jellyfin by injecting stuff into 'main.*.bundle.js'
- Creates a local backup for future restore
- Quick and easy restore process

## Requirements
Script only requires [python3](https://www.python.org/downloads/) to run.

Installing  dependencies on ubuntu/debian os:

```sh
sudo apt install python3
```



## Usage
Script needs to be set up first before running.

To setup:
- Edit additional_text.txt accordingly to your liking
- Make sure additional_text.txt is right beside the python script

To insert changes:
```sh
sudo python3 insertScript.py -i /usr/share/jellyfin/web/main.*.bundle.js
```

To revert changes:
```sh
sudo python3 insertScript.py -i /usr/share/jellyfin/web/main.*.bundle.js_backup
```
