from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QScrollArea, QLineEdit, QPushButton
from PyQt6.QtCore import Qt
from resources import settings
from DbHandler import GetHunterKills, GetHuntersByPartialName, execute_query, getAllUsernames
from Widgets.Modal import Modal
from Widgets.Label import Label

class HunterSearch(QGroupBox):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setStyleSheet("*{margin:16px;padding:8px;}")
        self.setTitle("Search Hunters")
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.searchBar = QLineEdit()
        self.searchBar.setPlaceholderText("Enter Hunter Name")
        self.searchButton = QPushButton("\t\tSearch\t\t")

        self.layout.addWidget(self.searchBar)
        self.layout.addWidget(self.searchButton)
        self.searchBar.returnPressed.connect(self.SubmitSearch)
        self.searchButton.clicked.connect(self.SubmitSearch)

    def SubmitSearch(self):
        name = self.searchBar.text()
        if len(name) <= 0:
            return
        data = GetHuntersByPartialName(name)
        self.ShowResults(data, name)

    def ShowResults(self, data, name):
        resultsWindow = Modal(parent=self)
        if len(data) <= 0:
            resultsWindow.addWidget(
                Label("You've never encountered %s in a Hunt." % name))
        else:
            pid = data[0]['profileid']
            resultsWindow.addWidget(
                Label("You've seen %s in %d hunts." % (name, len(data))))

            allnames = getAllUsernames(pid)
            kills = GetHunterKills(pid)
            killedby = 0
            killed = 0
            for k in kills:
                killedby += k['killedby']
                killed += k['killed']
            sameTeamCount = self.SameTeamCount(data)

            if len(allnames) > 1:
                resultsWindow.addWidget(
                    Label("They've also gone by:\n%s" % ",".join(allnames)))
            if sameTeamCount > 0:
                resultsWindow.addWidget(
                    Label("You've been on their team %d times." % sameTeamCount))
            if killedby > 0:
                resultsWindow.addWidget(
                    Label("They've killed you %d times." % killedby))
            if killed > 0:
                resultsWindow.addWidget(
                    Label("You've killed them %d times." % killed))

        resultsWindow.show()

    def SameTeamCount(self, data):
        teamnums = {}
        for d in data:
            teamnums[d['game_id']] = d['team_num']
        teams = []
        for id in teamnums:

            pids = execute_query(
                "select profileid from 'hunters' where game_id is '%s' and team_num is %d" % (id, teamnums[id]))
            team = []
            for pid in pids:
                team.append(pid[0])
            teams.append(team)
        n = 0
        myId = int(settings.value("profileid"))
        for team in teams:
            if myId in team:
                n += 1
        return n
