from NBPS.Logic.Commands.Client.Select.LogicSelectSkinCommand import LogicSelectSkinCommand
from NBPS.Logic.Commands.Client.Player.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from NBPS.Logic.Commands.Client.Player.LogicSetPlayerNameColorCommand import LogicSetPlayerNameColorCommand
from NBPS.Logic.Commands.Client.Purchase.LogicPurchaseDoubleCoinsCommand import LogicPurchaseDoubleCoinsCommand
from NBPS.Logic.Commands.Client.Purchase.LogicPurchaseHeroLvlUpMaterialCommand import LogicPurchaseHeroLvlUpMaterialCommand
from NBPS.Logic.Commands.Client.Purchase.LogicPurchaseBrawlPassCommand import LogicPurchaseBrawlPassCommand
from NBPS.Logic.Commands.Client.Purchase.LogicPurchaseOfferCommand import LogicPurchaseOfferCommand
from NBPS.Logic.Commands.Client.Gatcha.LogicGatchaCommand import LogicGatchaCommand
from NBPS.Logic.Commands.Client.LevelUp.LogicLevelUpCommand import LogicLevelUpCommand
from NBPS.Logic.Commands.Client.Select.LogicSelectEmoteCommand import LogicSelectEmoteCommand

commands = {
	500: LogicGatchaCommand,
	505: LogicSetPlayerThumbnailCommand,
	506: LogicSelectSkinCommand,
	509: LogicPurchaseDoubleCoinsCommand,
	519: LogicPurchaseOfferCommand,
	520: LogicLevelUpCommand,
	521: LogicPurchaseHeroLvlUpMaterialCommand,
	527: LogicSetPlayerNameColorCommand,
	534: LogicPurchaseBrawlPassCommand,
    538: LogicSelectEmoteCommand

}
