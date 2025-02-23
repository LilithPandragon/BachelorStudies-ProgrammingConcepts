#!/usr/bin/env python3

# Requirement for Part 2 Python: Declarative Programming — Pattern Matching with Regular Expression (regex)
#
# Susanne Peer SWD21
#

import re
import html

# if module requests not found --> open cmd and execute this "pip install requests"
# this only is needed for local testing see line 64 f.

import requests


def extractServersFromExternalLinksFromHTML(src):
    result = []
   
    templ = r'href="https://[a-zA-Z0-9.-]+/[a-zA-Z0-9.-]+"'

    matches = re.findall(templ, src)

# extracting server names and add those to result list
    for match in matches:
        parts = match.split("/")
        if len(parts) > 2:
            server = parts[2]
            result.append(server)

    result.sort()
    return result

    
def extractImageAltTextsFromHTML(src):
    result = []
    
    templ = r'<img\s+src="([a-zA-Z0-9.-]+\.png)"\s+alt="([^"]*)"'
    matches = re.findall(templ, src)

    result.extend(matches)

    return result


def extractTranscriptFromHTML(src,guy):
    result = []


    templ = fr'<b>{guy}:</b>.*?I.*?(?=<b>|$)'

    matches = re.findall(templ, src, re.DOTALL)

    cleanMatches = [re.sub('<.*?>', '', match) for match in matches]

    result.extend(cleanMatches)
    return result




# Just for testing. The printed output is NOT relevant for grading.
# Evaluation calls function 'main' and analyses the values returned.

# ------------------------------------------------------------------------
# testing local - comment line 81 and 82 and uncomment line 71 and line 75

#htmlURL = "https://elearning.fh-joanneum.at/pluginfile.php/96999/mod_resource/content/0/xkcd353-down-2022-12-05.html"

# if module requests not found --> open cmd and execute this "pip install requests"

#htmlSource = requests.get(htmlURL).text

#end of testing local 
#------------------------------------------------

# (the moodle-"evaluate" will use the exact same input test data!!)
htmlSource = open("xkcd353-down-2022-12-05.html", encoding = 'utf-8').read()

htmlSource = html.unescape(htmlSource)
# print(htmlSource) # ...<!DOCTYPE html> <html> <head> <link rel="stylesheet" type="text/css" href="/s/7d94e0.css" title="Default"/> <title>xkcd: Python</title>...

print(f"Inspect your (pretty-printed) results during testing:")
print(f"\n* (1/3) The list of external links:\n")
for idx,resource_and_server in enumerate(extractServersFromExternalLinksFromHTML(htmlSource)):
    print(f" {idx+1}: {resource_and_server}") # / what-if.xkcd.com, /xkcd/ twitter.com

print(f"\n* (2/3) The list of alternative image texts:\n")
for idx,imageAltText in enumerate(extractImageAltTextsFromHTML(htmlSource)):
    print(f" {idx+1}: {imageAltText}") # Earth temperature timeline, Selected Comics, ...

print(f"\n* (3/3) Guy 2 says:\n")
for idx,transcriptFirstSentenceGuy2 in enumerate(extractTranscriptFromHTML(htmlSource,'Guy 2')):
    print(f" {idx+1}: {transcriptFirstSentenceGuy2}") # Python!






