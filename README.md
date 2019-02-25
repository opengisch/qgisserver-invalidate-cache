invalidate-cache: QGIS Server Plugin to invalidate QGIS server cache of a project
=================================================================================

Description
-----------

This plugin adds a new request to QGIS Server `invalidatecache` which allows to invalidate QGIS server cache of a project

Installation
------------

We assume you have a fully functionnal QGIS Server.
See https://docs.qgis.org/testing/en/docs/user_manual/working_with_ogc/server/index.html

We need to download the plugin, and tell QGIS Server where the plugins are stored, the reload the web server.
For example on Debian:

```
# Create needed directory to store plugins
mkdir -p /srv/qgis/plugins

# Get last version
cd /srv/qgis/plugins
wget "https://github.com/opengisch/qgisserver-invalidate-cache/archive/master.zip"
unzip master.zip
mv qgis-invalidate-cache-master qgis-invalidate-cache

# Make sure correct environment variables are set in your web server configuration
# for example in Apache2 with mod_fcgid
nano /etc/apache2/mods-available/fcgid.conf
FcgidInitialEnv QGIS_PLUGINPATH "/srv/qgis/plugins/"

# Reload server, for example with Apache2
service apache2 reload
```

You can now test your installation
