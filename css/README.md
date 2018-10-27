# What

Beautify a web page.

# How

## Non-Vue Web Page

1. Adds CSS style and javascript from getmdl.io to &lt;head&gt;:

    ```html
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
    <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
    ```

1. Follows examples on getmdl.io to add "mdl-" styles to html elements.

## Vue Web Page

1. Adds CSS style from Vuetify to &lt;head&gt;:

    ```html
    <link href='https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons' rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/vuetify/dist/vuetify.min.css" rel="stylesheet">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
    ```

1. Add javascript from Vuetify towards end of &lt;body&gt;:

    ```html
    <script src="https://cdn.jsdelivr.net/npm/vuetify/dist/vuetify.js"></script>
    ```

1. Follows examples on vuetifyjs.com to add "v-" html elements.

# References

* [getmdl.io](http://getmdl.io)
* [Vuetify](https://vuetifyjs.com/en/)