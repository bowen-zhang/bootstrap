# What

Creates web app with reusable components.

# How

## Basic Usage

1. Includes vue js file.

    ```html
    <script src="https://cdn.jsdelivr.net/npm/vue"></script>
    ```

1. Add app element.

    ```html
    <div id="app">{{ message }}<div>
    ```

    Variables can be referenced as:

    {{ variableName }}

1. Create vue app instance.

    ```html
    <script>
        var app = new Vue({
            el: '#app',
            data: {
                message: 'Loading...'
            },
            created: function() {
                this.message = 'Hello World!';
            }
        });
    </script>
    ```

## Reusable Component

1. Creates a vue file.

    ```vue
    <template>
        <p>{{ message }}</p>
    </template>
    <script>
        module.exports = {
            props: ['message'],
            data: function() {
                return {
                }
            }
        };
    </script>
    <style scoped>
        p {
            text-size: 120%;
        }
    </style>
    ```

1. Includes HttpVueLoader js file in header.

    ```html
        <script src="https://unpkg.com/http-vue-loader"></script>
    ```

1. Declare components in vue app.

    ```javascript
    var app = new Vue({
        el: '#app',
        components: {
            'my-component': httpVueLoader('my-component.vue'),
        },        
    ```

1. Use component in html.

    ```html
    <my-component message='Hello World!'></my-component>
    ```

# References

* [Vue.js](https://vuejs.org/)
* [HttpVueLoader](https://github.com/FranckFreiburger/http-vue-loader)