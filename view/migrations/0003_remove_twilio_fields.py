from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0002_contactmessage_email_error_contactmessage_email_sent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='sms_error',
        ),
        migrations.RemoveField(
            model_name='contactmessage',
            name='sms_sent',
        ),
        migrations.RemoveField(
            model_name='contactmessage',
            name='sms_sid',
        ),
    ]
