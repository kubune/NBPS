from NBPS.Server.Network.Server import Server
from NBPS.Server.Extra.Changelog import Changelog
from NBPS.Server.Extra.Commands import CommandsHandler
from NBPS.Inbox.InboxServer import InboxServer
from NBPS.Logic.Handlers.Debugger import banner, Colors, Styles

def main():
    banner("""
    
    ███╗   ██╗██████╗ ██████╗ ███████╗
    ████╗  ██║██╔══██╗██╔══██╗██╔════╝
    ██╔██╗ ██║██████╔╝██████╔╝███████╗    ╭───────────────╮
    ██║╚██╗██║██╔══██╗██╔═══╝ ╚════██║    │ Dev: kubune   │
    ██║ ╚████║██████╔╝██║     ███████║    │ Version: v1.2 │
    ╚═╝  ╚═══╝╚═════╝ ╚═╝     ╚══════╝    ╰───────────────╯
                     
    """, Colors.RED, Colors.ORANGE, style=Styles.BOLD)

    Changelog().showChangelog()
    CommandsHandler(key="/").start()

    InboxServer(port=8000).start()

    Server("0.0.0.0", 9339).start()


if __name__ == '__main__':
    main()
