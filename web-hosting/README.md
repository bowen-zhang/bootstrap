# What

Host a static website for free.

# How

1. Log-in [Firebase Console](https://console.firebase.google.com) with your Google account.

1. Create a new project.

1. Install Firebase tools.

    ```shell
    npm install -g firebase-tools
    ```

1. Sign-in to Firebase.

    ```shell
    firebase login
    ```

1. Initialize Firebase under your project directory.

    1. Run the following command.

    ```shell
    firebase init
    ```

    1. Select "Hosting".

    1. Select the new project.

    1. Use "./" as public directory.

    1. Answer "N" to "Configure as a single-page app?"

    1. Answer "N" to "File .//index.html already exists. Overwrite?"

# References

* [Firebase](https://firebase.google.com/)