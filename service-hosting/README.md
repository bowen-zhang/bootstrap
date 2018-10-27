# What

Hosts a backend service in cloud.

# How

## Create VM in Cloud

1. Create a Google account.

1. Login at console.cloud.google.com.

1. Create a project.

1. Enable billing.

1. Create a VM in Compute Engine.

    * Machine type

        Select "micro (1 shared vCPU) 0.6GB memory, f1-micro". Each project has
        free quota for one such VM.

    * OS
        Select Ubuntu or any OS of your preference.

    * Firewall
        Check "allow HTTP(S) traffic".

## SSH to VM

1. Generates a new SSH key.

    ```shell
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/[filename] -C [username]
    ```

1. Add to the project.

    Go to console.cloud.google.com, "Compute Engine", "Metadata", "SSH Keys".
    Paste content from ~/.ssh/\[filename\].pub

1. Add entry to SSH config.

    Add the foolowing to ~/.ssh/config:
    ```
    Host [hostname]
      HostName [VM instance's external IP]
      User [username]
      IdentityFile ~/.ssh/[filename]
    ```
    "hostname" can be arbitrary string.

1. Connect.

    ```shell
    ssh [username]@[hostname]
    ```

## Edit files remotely

1. (for Mac OS) Install [FUSE and SSHFS for Mac](https://osxfuse.github.io/).

1. Mount remote directory via sshfs

    ```shell
    mkdir ~/[mount point]
    sshfs [username]@[hostname]:/home/[username] ~/[mount point]
    ```

## Run example

1. Copy files to VM instance.

    ```shell
    scp * [username]@[hostname]:/home/[username]
    ```

1. SSH to VM instance.

1. Run example.

    ```shell
    make init
    make run
    ```

# Resources

* [Google Cloud Compute Engine](https://cloud.google.com/compute/)
* [Free Quota](https://cloud.google.com/compute/pricing#freeusage)
* [Cloud SDK](https://cloud.google.com/sdk/docs/quickstarts)
* [FUSE](https://osxfuse.github.io/)