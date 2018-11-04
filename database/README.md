# What

Queries data from and stores data to database across platform/language.

# How

1. Includes Firestore javascript libraries in html.

    ```html
    <script src="https://www.gstatic.com/firebasejs/5.5.6/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/5.5.6/firebase-firestore.js"></script>
    ```

1. Gets Firebase project settings.

    1. Logins at console.firebase.google.com

    1. Goes to "Project Overview" => "Project Settings" => "Add Firebase to
    your web app".

    1. Copy apiKey, databaseURL, projectId.

1. Initializes Firestore.

    ```javascript
    var config = {
      apiKey: "[apiKey]",
      databaseURL: "[databaseURL]",
      projectId: "[projectId]",
    };
    firebase.initializeApp(config);
    var db = firebase.firestore();
    db.settings({
        timestampsInSnapshots: true
    });
    ```

1. Watch data.

    ```javascript
    db.collection('messages').orderBy('timestamp').onSnapshot(querySnapshot => {
        querySnapshot.forEach(doc => {
            // render document
        })
    });
    ```

1. Save data.

    ```javascript
    db.collection('messages').add({
        timestamp: new Date(),
        text: text
    })
    .then(docRef => {
        // indicates document is saved.
    });

# Resources

* [Firestore](https://firebase.google.com/docs/firestore/)
