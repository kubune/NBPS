from NBPS.Logic.Handlers.CsvReader import CsvReader


class Emotes:
    def get_emotes_id(self):
        emotesID = []
        reader = CsvReader()
        rowData = reader.readCsv(f'{reader.path}/csv_logic/emotes.csv')
        for row in rowData:
            if row[1].lower() != 'true' and row[6].lower != 'true':
                emotesID.append(rowData.index(row))

        return emotesID