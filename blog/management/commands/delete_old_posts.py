# blog/management/commands/delete_old_posts.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from blog.models import BlogPost
import datetime

class Command(BaseCommand):
    help = 'Delete blog posts older than a specified number of days'

    def add_arguments(self, parser):
        parser.add_argument('days', type=int, help='Number of days')

    def handle(self, *args, **kwargs):
        days = kwargs['days']
        cutoff_date = timezone.now() - datetime.timedelta(days=days)
        old_posts = BlogPost.objects.filter(created_at__lt=cutoff_date)
        count = old_posts.count()
        old_posts.delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} blog post(s) older than {days} days'))
