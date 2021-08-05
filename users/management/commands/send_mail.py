from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		send_mail(
			"Senha",
			"message",
			settings.DEFAULT_FROM_EMAIL,
			["lucasosilva68@gmail.com"],
			fail_silently=False,
		)
