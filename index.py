# -*- coding: utf-8 -*-
from time import sleep

from spider.course import Course
from spider.flie_downloader import FileDownloader
from spider.html_generator import HtmlGenerator

if __name__ == '__main__':
    try:
        cid = int(raw_input('Input your course id:'))
        if cid < 0 or cid > 1000:
            raise ValueError
    except:
        print "You have a wrong ID!"
        quit()
    course = Course(cid)
    print "You are about to download [" + course.name + "]"
    print "The following are the videos you will download:"
    for video in course.videos:
        print video['name']
    print "---------------------------------"

    html_generator = HtmlGenerator(course.html)
    html_generator.generate()

    file_downloader = FileDownloader(course.name, course.videos)
    if file_downloader.flag:
        print "Mission completed"
    sleep(60)
