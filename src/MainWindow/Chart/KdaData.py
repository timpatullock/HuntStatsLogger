from cmath import inf
from DbHandler import *
from pyqtgraph import PlotDataItem
from MainWindow.Chart.ScatterItem import ScatterItem

class KdaData():
    def __init__(self,parent=None):
        self.parent = parent
        kData = GetKillsByMatch()
        dData = GetDeathsByMatch()
        aData = GetAssistsByMatch()

        totalKills = 0
        totalDeaths = 0
        totalAssists = 0

        kda = 0.0
        data = []

        GameTypes = GetGameTypes()

        i = 0
        self.minKda = inf
        self.maxKda = -inf
        for ts in GameTypes:
            if ts in kData:
                totalKills += kData[ts]['kills']
            if ts in dData:
                totalDeaths += dData[ts]['deaths']
            if ts in aData:
                totalAssists += aData[ts]['assists']

            kda = (totalKills+totalAssists)/(max(1,totalDeaths))
            if kda > self.maxKda:
                self.maxKda = kda
            if kda < self.minKda:
                self.minKda = kda
            data.append({
                'x':i,
                'y':kda,
                'qp':GameTypes[ts],
                'ts':ts
            })
            i += 1

        self.line = PlotDataItem(data,pen="#ffffff88")
        self.qpPoints = ScatterItem(
            [{'x': pt['x'], 'y': pt['y'], 'data':pt['ts']} for pt in data if pt['qp'] == 'true'],
            pen="#000000",brush="#00ffff",name="Quick Play",tip="{data}<br>KDA: {y:.2f}".format, parent=self.parent
        )
        self.bhPoints = ScatterItem(
            [{'x': pt['x'], 'y': pt['y'], 'data':pt['ts']} for pt in data if pt['qp'] == 'false'],
            pen="#000000",brush="#ff0000",name="Bounty Hunt",tip="{data}<br>KDA: {y:.2f}".format,parent=self.parent
        )