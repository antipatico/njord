"""An AirVPN CLI manager.

Usage:
  njord -h|--help
  njord --version
  njord selserv [--best] [--country <cn>|--continent <cn>] [--json <path>]
  njord ovpn [--ssl] [--udp] [--port=<port>] [--ovpn-out=<file>] [--ssl-out=<file>] [--log-path=<path>] [--secrets-path=<path>] <ip>

Options:
  --best, -B            If this flag is on the *Reccomended* server is selected
                        instead of a random one.
  --country, -C=<cn>    Select the server from a specific country codename.
  --continent, -M=<vn>  Select the server from a specific continent codename.
  --json=<path>         A path to a file containing the status of the AirVPN's
                        servers. (Used for testing and debugging).

Commands:
  selserv               Downloads the latest status from the AirVPN APIs and
                        select a server with the given parameters. If either
                        country either continent flag is passed the server is
                        chosen completely random.
  ovpn                  Generate an OpenVPN configuration file with the given
                        options.

Examples:
  njord selectserver --country DE

"""
from docopt import docopt
from . import version
from .selserv import selserv
from .exceptions import *
from sys import stderr, exit

def eprint(*args, **kwargs):
    print(*args, file=stderr, **kwargs)
    exit(1)

def selectserver(best, country, continent, json):
    try:
        country = country.lower() if country else None
        continent = continent.lower().capitalize() if continent else None
        print(selserv(best, country, continent, json))
    except Exception as e:
        eprint(e)

def main(args=None):
    arguments = docopt(__doc__, version='njord '+str(version))
    if arguments['selserv']:
        selectserver(arguments['--best'], arguments['--country'], arguments['--continent'], arguments['--json'])
    elif arguments['ovpn']:
        eprint("Function not implemented yet")

if __name__ == "__main__":
    main()

