from NBPS.Server.Network.Server import Server
from NBPS.Server.Extra.Changelog import Changelog
from NBPS.Server.Extra.Commands import CommandsHandler

def main():
    print("NBPS v29 is starting...\n")

    Changelog().showChangelog()
    CommandsHandler(key="/").start()
    Server("0.0.0.0", 9339).start()


if __name__ == '__main__':
    main()
