from django.db import models
from datetime import datetime


class StatisticClassManager(models.Manager):

    def update_statistic(self, date, status, partner, route, package, amount=0):
        statistic, create = self.get_or_create(
            date=datetime(year=date.year, month=date.month, day=date.day),
            partner=partner,
            route=route,
            package=package,
        )
        if status['statusId'] == 150:
            statistic.delivered += 1
            statistic.amount += amount
        elif status['statusId'] == 160:
            statistic.rejection += 1
            statistic.amount += amount
        else:
            return
        statistic.save()