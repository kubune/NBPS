from NBPS.Logic.Messages.Client.Home.EndClientTurnMessage import EndClientTurnMessage
from NBPS.Logic.Messages.Client.Auth.LoginMessage import LoginMessage
from NBPS.Logic.Messages.Client.Auth.KeepAliveMessage import KeepAliveMessage
from NBPS.Logic.Messages.Client.Home.SetNameMessage import SetNameMessage
from NBPS.Logic.Messages.Client.Team.TeamCreateMessage import TeamCreateMessage
from NBPS.Logic.Messages.Client.Team.TeamLeaveMessage import TeamLeaveMessage
from NBPS.Logic.Messages.Client.Team.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage
from NBPS.Logic.Messages.Client.Team.TeamToggleSettingsMessage import TeamToggleSettingsMessage
from NBPS.Logic.Messages.Client.Team.TeamSetLocationMessage import TeamSetLocationMessage
from NBPS.Logic.Messages.Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from NBPS.Logic.Messages.Client.Battle.StartGameMessage import StartGameMessage
from NBPS.Logic.Messages.Client.Home.GetPlayerProfileMessage import GetPlayerProfileMessage
from NBPS.Logic.Messages.Client.Leaderboard.GetLeaderboardMessage import GetLeaderboardMessage
from NBPS.Logic.Messages.Client.Home.SetSupportedCreatorMessage import SetSupportedCreatorMessage
from NBPS.Logic.Messages.Client.Battle.AskForBattleEndMessage import AskForBattleEndMessage
from NBPS.Logic.Messages.Client.Avatar.AvatarNameCheckRequestMessage import AvatarNameCheckRequestMessage
from NBPS.Logic.Messages.Client.Alliance.CreateAllianceMessage import CreateAllianceMessage
from NBPS.Logic.Messages.Client.Alliance.AskForAllianceDataMessage import AskForAllianceDataMessage
from NBPS.Logic.Messages.Client.Alliance.ChangeAllianceSettingsMessage import ChangeAllianceSettingsMessage
from NBPS.Logic.Messages.Client.Alliance.JoinAllianceMessage import JoinAllianceMessage
from NBPS.Logic.Messages.Client.Alliance.AskForJoinableAlliancesListMessage import AskForJoinableAlliancesListMessage
from NBPS.Logic.Messages.Client.Alliance.LeaveAllianceMessage import LeaveAllianceMessage
from NBPS.Logic.Messages.Client.Alliance.SearchAlliancesMessage import SearchAlliancesMessage
from NBPS.Logic.Messages.Client.Alliance.ChatToAllianceStreamMessage import ChatToAllianceStreamMessage
from NBPS.Logic.Messages.Client.Team.TeamSetMemberReadyMessage import TeamSetMemberReadyMessage
from NBPS.Logic.Messages.Client.Analytics.AnalyticEventMessage import AnalyticEventMessage

packets = {
    10101: LoginMessage,
    10110: AnalyticEventMessage,
    14103: StartGameMessage,
    10108: KeepAliveMessage,
    10212: SetNameMessage,
    14102: EndClientTurnMessage,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: AskForBattleEndMessage,
    14113: GetPlayerProfileMessage,
    14301: CreateAllianceMessage,
    14302: AskForAllianceDataMessage,
    14303: AskForJoinableAlliancesListMessage,
    14305: JoinAllianceMessage,
    14308: LeaveAllianceMessage,
    14315: ChatToAllianceStreamMessage,
    14316: ChangeAllianceSettingsMessage,
    14324: SearchAlliancesMessage,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14354: TeamChangeMemberSettingsMessage,
    14363: TeamSetLocationMessage,
    14372: TeamToggleSettingsMessage,
    14403: GetLeaderboardMessage,
    14600: AvatarNameCheckRequestMessage,
    18686: SetSupportedCreatorMessage,
    14355: TeamSetMemberReadyMessage

}
