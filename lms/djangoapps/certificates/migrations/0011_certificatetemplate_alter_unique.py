# -*- coding: utf-8 -*-

import logging

from __future__ import unicode_literals
from django.db import migrations, models

log = logging.getLogger(__name__)

def revert_alter_unique(apps, schema_editor):
    CertificateTemplateModel = apps.get_model("certificates", "CertificateTemplate")

    # get all unique sets of (org_id, course_key, and mode)
    all_unique_templates_ignoring_language = CertificateTemplateModel.objects.values_list(
        "organization_id",
        "course_key",
        "mode").distinct()

    # for each course specific template by org_id, course_key and mode
    for org_id, course_key, mode in all_unique_templates_ignoring_language:
        course_templates = CertificateTemplateModel.objects.filter(organization_id=org_id, course_key=course_key, mode=mode)
        if course_templates.count() > 1  # theres more than one template for a course
            language_specific_course_templates = course_templates.exclude(language=None)
            for template in language_specific_course_templates:
                log.info('Deleting ' + template.language + ' language template for course '+template.course_key)
            CertificateTemplateModel.objects.filter(id__in=list(language_specific_course_templates)).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0010_certificatetemplate_language'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='certificatetemplate',
            unique_together=set([('organization_id', 'course_key', 'mode', 'language')]),
        ),
        migrations.RunPython(RunPython.noop, reverse_code=revert_alter_unique)
    ]
