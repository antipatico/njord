"""An AirVPN CLI manager.

Usage:
  njord -h|--help
  njord --version
  njord selectserver [--best] [--country=<codename>|--continent=<codename>] [--json=<path>]
  njord genconfig [--ssl] [--udp] [--port=<port>] [--ovpn-out=<file>] [--ssl-out=<file>] [--log-path=<path>] [--secrets-path=<path>] <ip>

Options:
  --best, -B            If this flag is on the *Reccomended* server is selected
                        instead of a random one.
  --country, -C=<cn>    Select the server from a specific country codename.
  --continent, -M=<cn>  Select the server from a specific continent codename.   
  --json=<path>     A path to a file containing the status of the AirVPN's
                    servers. (Used for testing and debugging).

Commands:
  selectserver, ss  Downloads the latest status from the AirVPN APIs and
                    select a server with the given parameters. If either
                    country either continent flag is passed the server is
                    chosen completely random.
  genconfig, ovpn   Generate an OpenVPN configuration file with the given
                    options.

Examples:
  njord selectserver --country=DE

"""
from docopt import docopt
from . import version

def main(args=None):
    arguments = docopt(__doc__, version='njord '+str(version))
    print(arguments)
    print(version)

if __name__ == "__main__":
    main()

