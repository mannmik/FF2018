from django.db import models
from NFLteams.models import NFL_Team

# ---------- TODO -------------
# Need to set up the Player Model
# Follow desing from the design notebook
# -----------------------------
class Player(models.Model):
    # fullName
    fullName = models.CharField(max_length = 255)
    # firstName
    firstName = models.CharField(max_length = 255)
    # lastName
    lastName = models.CharField(max_length = 255)
    # position
    position = models.CharField(max_length = 5)
    # positionRank
    positionRank = models.IntegerField(default = -1)
    # team 
    team = models.ForeignKey(NFL_Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullName
