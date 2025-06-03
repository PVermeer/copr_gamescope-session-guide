# RPM build of [steam-using-gamescope-guide ](https://github.com/shahnawazshahin/steam-using-gamescope-guide)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/pvermeer/gamescope-session-guide/package/gamescope-session-guide/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/pvermeer/gamescope-session-guide/package/gamescope-session-guide/)

Install [steam-using-gamescope-guide](https://github.com/shahnawazshahin/steam-using-gamescope-guide) on Fedora.

ONLY TESTED with Bazzite Gnome Desktop image

## Patches
### Select the display for gamescope session
Gamescope session is launched with `--prefer-output $GAMESCOPE_SESSION_OUTPUT` so setting:
```sh
# Gamescope session display connector
GAMESCOPE_SESSION_OUTPUT=DP-1
```
in `/etc/environment` will try to use the display of your choice.

# Fedora copr
https://copr.fedorainfracloud.org/coprs/pvermeer/gamescope-session-guide

# Credits
- https://github.com/shahnawazshahin/steam-using-gamescope-guide
