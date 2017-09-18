# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from edxval import api as edxval_api
from contextlib import closing
import io

FILE_DATA = u"""
{
  "start": [
    490,
    1920,
    4300,
    5610,
    8410,
    10660,
    13510,
    16480,
    19660,
    21960,
    25550,
    28280,
    31850,
    35830,
    37800,
    40280,
    44220,
    47110,
    49880,
    52680,
    54360,
    56930,
    58670,
    61260,
    63130,
    66430,
    70230,
    73520,
    74770
  ],
  "end": [
    1920,
    4300,
    5610,
    8410,
    10660,
    13510,
    16480,
    19660,
    21960,
    25550,
    28280,
    31850,
    35830,
    37800,
    40280,
    44220,
    47110,
    49880,
    52680,
    54360,
    56930,
    58670,
    61260,
    63130,
    66430,
    70230,
    73520,
    74770,
    76520
  ],
  "text": [
    "Congratulations.",
    "Now you know how to use one of the basic building blocks of",
    "the course.",
    "If you look to your left, you will see a table of contents",
    "for all of the aspects of the course.",
    "Right now, since you are playing this video, you're in",
    "the overview section, which contains various aspects of",
    "administrivia including these tutorials.",
    "Continuing to look to your left, if you click on the",
    "various chapter labels, you will see the course content",
    "that it's associated with each chapter.",
    "You will not change content or interrupt a video until you",
    "actually click on a new course element to navigate to.",
    "Each chapter contains activities that you are",
    "expected to complete, including presentation",
    "sequences, which you should watch and participate in",
    "in order to learn new material concepts.",
    "You should also complete the homeworks and activities in",
    "order to get more practice and solidify your understanding of",
    "the material.",
    "Many courses will grade you based off of your performance",
    "on homework questions.",
    "The next section will describe how to enter",
    "and check your answers.",
    "Note that in this sequence, even though the next section",
    "will give you feedback it will not affect your grade on any",
    "aspect of your interactions with edX, So you should feel",
    "free to experiment.",
    "可以用“我不太懂艺术 但我知道我喜欢什么”做比喻"
  ]
}
"""


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('video_id', type=str)
        parser.add_argument('lang_code', type=str)

    def handle(self, *args, **options):

        file_data = io.BytesIO(FILE_DATA.encode('utf-8'))
        file_data.name = 'whatever_name.sjson'
        file_data.size = 1
        with closing(file_data):
            transcript_url = edxval_api.create_or_update_video_transcript(
                video_id=options['video_id'],
                language_code=options['lang_code'],
                file_name=file_data.name,
                provider=edxval_api.TranscriptProviderType.CUSTOM,
                file_format=edxval_api.TranscriptFormat.SJSON,
                file_data=file_data,
            )
            print transcript_url
