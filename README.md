# Disc Jockey

## Introduction

This is an example program that users the Spirit of Korth's Software Development Wrapper for Active Worlds to interact with the [Active Worlds](https://www.activeworlds.com). This project or its contributors are not affiliated with Active Worlds. This program was inspired by the [Disc Jockey](http://wiki.activeworlds.com/index.php?title=SDK_Sample_Program_2) written in C using the original Active Worlds SDK. The Active Worlds SDK is provided in aw64.dll. By using the active worlds SDK, you are agreeing to the terms of the [Active Worlds SDK License Agreement](https://www.activeworlds.com/sdk/download.htm).

## Usage

This program can both be used locally and through the use of the provided Docker image.

To use this program locally, you will need to have Python 3 installed. Then you can run the program with the following commands:
```bash
pip install -r requirements.txt
python ./disc_jockey
```

You can also run the program with the following command provided you have Docker installed:
```bash
docker build -t dj .
docker run -it dj
```


## Configuration

Configuration is an aggregation of multiple configuration sources. The configuration sources in order of precedence are:

- The json configuration file
- The user's input

X coordinates are west/east where west is positive and east is negative.
Y coordinates represent height where up is positive and down is negative and ground is 0.
Z coordinates are north/south where north is positive and south is negative.

| Variable | Description |
|---------|-------------|
| `BOT_NAME` | The name of the bot. |
| `CITIZEN_NUMBER` | The owner of the bot. |
| `PASSWORD` | The password of the bot. |
| `PLUGIN_PATH` | The directory to load plugins from. |
| `WORLD_NAME` | The name of the world to connect to. |
| `WORLD_X` | The x coordinate of the world to connect to. |
| `WORLD_Y` | The y coordinate of the world to connect to. |
| `WORLD_Z` | The z coordinate of the world to connect to. |

### Json Configuration File

The json configuration file is a json file that contains the configuration for the bot. The json file must be called `configuration.json`. IF the json file is not found, no errors occur and the configuration is not used.

Configuration example:
```json
{
    "bot_name": "Plugin Bot",
    "world_name": "Test World",
    "world_coordinates": {
        "x": 0,
        "y": 0,
        "z": 0
    },
    "plugin_path": "plugins",
    "citizen_number": 123456,
    "password": "password"
}
```

### User Input

The user input is a series of prompts that are displayed to the user. The user input is used to gather the configuration for the bot when no other configuration is available.

## License

This project is licensed under the MIT license.

## Contribution

This project is open source. Feel free to contribute to the project by opening an issue, creating a pull request, or by contacting [Johnny Irvin](mailto:irvinjohnathan@gmail.com). I appreciate any feedback or contributions. This project is not affiliated with Active Worlds, Inc. The creator of this project is not affiliated with Active Worlds, Inc.