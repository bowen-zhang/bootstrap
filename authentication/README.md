# What

Authenticates http request handlers using Google OAuth.

# How

1. Creates OAuth client id.

    1. Logins at console.cloud.google.com

    1. Goes to "APIs & Services" => "Credentials".

    1. Clicks "Create Credentials", select "OAuth Client ID"

    1. Selects "Web application".

    1. Adds "http://localhost:5000" to Authorized javascript origins".

    1. Adds "http://localhost:5000/oauth2callback" to "Authorized redirect URIs".

    1. "Save"

    1. Copy "client id" and "client secret".

1. 