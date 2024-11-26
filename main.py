from NBPS.Server.Network.Server import Server
from NBPS.Server.Extra.Changelog import Changelog

def main():
    print("NBPS v29 is starting...\n")

    Changelog().showChangelog()
    Server("0.0.0.0", 9339).start()


if __name__ == '__main__':
    main()
