from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class UserModel(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    date_of_birth = models.DateField(null=True, blank=True)
    user_email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    in_game_name = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        db_table = 'custom_user'

    groups = models.ManyToManyField(
        Group,
        through='UserGroups',
        through_fields=('user', 'group'),
        related_name='custom_user_groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        through='UserUserPermissions',
        through_fields=('user', 'permission'),
        related_name='custom_user_permissions'
    )

    def __str__(self):
        return '{in_game_name}#{id}'.format(in_game_name=self.in_game_name, id=self.user_id)


class UserGroups(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class UserUserPermissions(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)


class MatchModel(models.Model):
    match_id = models.AutoField(primary_key=True)
    match_name = models.CharField(max_length=50, help_text="Selecciona el nombre de la partida")
    players = models.ManyToManyField(UserModel, through='MatchPlayer', related_name='matches')

    class Meta:
        ordering = ["-match_name"]

    def __str__(self):
        return self.match_name


class MatchPlayer(models.Model):
    match = models.ForeignKey(MatchModel, on_delete=models.CASCADE)
    player = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('match', 'player')

    def __str__(self):
        return '{match}: {id_j1}'.format(match=self.match.match_name, id_j1=self.player.first_name)
