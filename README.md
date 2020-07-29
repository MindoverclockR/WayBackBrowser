# WayBackBrowser
![PY3](https://img.shields.io/badge/python3--green) ![JS](https://img.shields.io/badge/javascript--yellow.svg)<br />

A Python + JavaScript program that constantly opens random sites from a list to make a "smokescreen" over your browser history across different dates in the past.

### Supported platforms:

> ##### Windows Vista & up
> ##### GNU/Linux with systemd
Note: Due to the snap packaging of Chromium in Ubuntu 20.04+, you need to specify the browser to use with the `--browser` option.

### Supported browsers:

> <h5>Firefox</h5>
> <h5>Chromium (Default on Linux)</h5>
> <h5>Google Chrome (Default on Windows)</h5>
> <h5>Microsoft Edge</h5>
> <h5>Opera</h5>
> <h5>Safari</h5>

- [What is it?](#what-is-it)
- [How to use it](#how-to-use-it)
  - [Install Python](#py)
  - [Download](#dl)
  - [Extract files](#extract)
    - [Adding your own URLs](#add-own-urls)
  - [Enabling JavaScript and Pop-ups](#enable-js-popups)
  - [Run](#run)
 - [Credits](#credits)

## What is it? <a id="what-is-it">
WayBackBrowsing is a simple Python + JavaScript program that randomly opens sites from a long list of popular URLs from many categories across different dates in the past. This will act as a mask, or "smokescreen" over your browsing history, to troll, confuse, and confound the prying eyes of those who may be spying on your **local** browser history.
## How to use it <a id="how-to-use-it">

> ### 1. Install Python <a id="py">
>
> Firstly, you need to make sure Python 3 is installed on your system.
>
> On Windows, go to https://www.python.org/downloads/windows/. Download and install Python 3 according to your system configuration (In most cases, download "Windows x86-64 executable installer" of the latest release.) It's recommended to **add Python to PATH** for easier access.
>
> On Linux, install Python 3 using your distribution's package manager. For example: (`#` means that the command should be ran as root)
>
> 
>
> Arch (Manjaro...): `# pacman -S python`
> CentOS / RHEL: `# yum install python3`
> Debian / Ubuntu (*Ubuntu, Mint, Elementary, Pop! OS...): `# apt install python3 `
> Fedora: `# dnf install python3 `
> openSUSE / SLE: `# zypper in python3`

> ### 2. Download <a id="dl">
>
> On any OS, you would navigate to https://github.com/MindoverclockR/WayBackBrowsing. Once on this page, click the button that says "Clone or Download" and then "Download as ZIP".
> <br />
> ![Clone or Download](https://github.com/keeganjk/smokescreen/blob/master/images/download.gif?raw=true "")
> <br />
> If you are on Linux, you can type <code>git clone https://github.com/MindoverclockR/WayBackBrowsing</code> into the terminal to 
> clone this repository and then <code>mv</code> into the directory. If you do this, skip to step 4.

<hr>

> ### 3. Extract files <a id="extract">
> Nextly, extract the ZIP file and then move into the <code>WayBackBrowsing</code> folder. <br/><br/>
> <a id="add-own-urls"> 
>If you want, you can add your own URLs to `list.js`, surrounded by quotes. Make sure that it begins with `http://` or `https://`, otherwise, the list won't work. <br/><br/>
> If you want the list to show up as often as everything else, copy it 20 times.
> You can also make it have less copies to show up less frequently or more copies to show up more frequently.

<hr>

> ### 4. Enable JavaScript and Pop-ups <a id="enable-js-popups">
> After opening <code>index.htm</code>, you have to enable pop-ups and JavaScript (for <code>index.htm</code>).
> This will be different in every browser, but it is usually in Settings.
> JavaScript will most likely be enabled, but Pop-ups may be disabled.set-wait

<hr>

> ### 5. Run <a id="run">
>
> On Windows, run CMD with Administrator rights. Go to the location of extracted files using `cd` , then run `waybackbrowser.py` using `python`. For example:
>
> ```
> cd C:\Users\MindoverclockR\Downloads\WayBackBrowser
> python waybackbrowser.py
> ```
>
> On Linux, run `waybackbrowser.py` using `python` or `python3` with a sudoer, like: 
> ```
> $ python3 ~/WayBackBrowser/waybackbrowser.py
> ```
> You will be prompted for sudo to change the system time.
>
> For more usages, run `waybackbrowser.py` with `--help` argument.
>
>
> > <b>WARNING! If you have a data limit, do not use this program unless you expect to be charged extra or prevented from continuing web browsing; this uses random page generation to pollute, or make a "smokescreen" over your browser history. Also, putting the wait time too low can cause crashes, denial-of-service to yourself, and difficulty to stop the script.</b>

## Credits <a id="credits">
[smokescreen](https://github.com/keeganjk/smokescreen), keeganjk

[K4YT3X](https://github.com/k4yt3x/)