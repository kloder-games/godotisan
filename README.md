# WORK IN PROGRESS... UNFINISHED

# godotisan

A command line interface for templates compilation and modules management.

## Purpose

Create a workflow about Godot template compilation and management.

This tool intend to simplified the templates compilation with Godot Engine.

## Install

Install using *pip*

    $ pip install godotisan

Not yet published :(

## Usage

```bash
godotisan create project-name
cd project-name
godotisan module add admob
godotisan module install admob
godotisan build android --cores=8
```

### Create

Create the project and clone the Godot repo on it, checkout the latest stable tag.

```bash
godotisan create project-name
```

### Compile Android Templates

Compile the debug and release andoird templates.

```bash
godotisan build android
```

By default it use 4 cores for scons we can change to 8 (for example) with the *--cores* option

```bash
godotisan build android --cores=8
```

And we can select witch target build

```bash
godotisan build android --cores=8 --only-debug
godotisan build android --cores=8 --only-release
```

### Modules

#### Add

Add the module to the modules folder (Not install into Godot)

```bash
godotisan module add admob
```

#### Remove

Remove the module from the modules folder and from the config file

```bash
godotisan module remove admob
```

#### install

Install the module on Godot modules folder and take the next actions indicated on the config file

```bash
godotisan module install admob
```

#### uninstall

Remove the module from Godot modules folder

```bash
godotisan module uninstall admob
```

## Firebase

If you are using firebase you must turn firebase to *true* (on godotisan.json) and put your *google-services.json* on the root of the build project

```bash
{
    ...
    "firebase": true
    ...
}
```

## Modules list

- **admob** https://github.com/jlopezcur/GodotAdmob.git (tag: v1.1)
- **adcolony** https://github.com/jlopezcur/GodotAdColony.git (tag: master)
- **google-analytics** https://github.com/jlopezcur/GodotGoogleAnalytics.git (tag: master)
- **google-play-services** https://github.com/jlopezcur/GodotGooglePlayGameServices.git (tag:master)
- **share** https://github.com/jlopezcur/GodotShare.git (tag: master)

## License

MIT license
