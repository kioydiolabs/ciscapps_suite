# Installing required packages

### Step 1 : _Updating the repositories_

Update the package repositories

```Shell
sudo apt update
```

### Step 2 : _Install required packages_

_Note : You need to be a **sudo** user (administrator privileges), unless you are **root**._

Install **docker.io** and **docker-compose**. \
The `-y` automatically confirms the installation.

```Shell
sudo apt install docker.io docker-compose -y
```

This may take a few minutes.