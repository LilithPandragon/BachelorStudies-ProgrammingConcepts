##More Beautiful, readable and maintainable code
##Susanne Peer SWD21
##Python 3.8.5
##be sure to install the following packages: googlesearch-python, requests, beautifulsoup4
##have fun to try it out :)

import os
import csv
from googlesearch import search
import requests
from bs4 import BeautifulSoup

def download_images(search_term, num_images=5, download_dir='downloads'):
    image_urls = []

    for url in search(search_term, num_results=num_images, lang='en'):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            if img_url and img_url.startswith('http'):
                image_urls.append(img_url)

    # Erstellung eines Verzeichnisses, um Bilder zu speichern
    directory = os.path.join(download_dir, search_term.replace(" ", "_"))
    os.makedirs(directory, exist_ok=True)

    # Bilder werden heruntergeladen
    for i, img_url in enumerate(image_urls):
        image_path = os.path.join(directory, f"{i + 1}.jpg")
        with open(image_path, 'wb') as f:
            f.write(requests.get(img_url).content)
        print(f"Downloaded {image_path}")

    return directory

def create_diashow_and_log(search_term, image_directory, csv_file='log.csv', html_file='slideshow.html'):
    # Die Protokolldatei wird in Excel geschrieben
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Image', 'Download Time'])

        for filename in os.listdir(image_directory):
            if filename.endswith(".jpg"):
                image_path = os.path.join(image_directory, filename)
                csv_writer.writerow([filename, os.path.getctime(image_path)])

    # HTML Diashow wird geschrieben
    with open(html_file, 'w') as html:
        html.write("<!DOCTYPE html>\n<html>\n<body>\n")
        html.write(f"<h1>{search_term} Slideshow</h1>\n")
        html.write("<div style='text-align: center;'>\n")

        for filename in os.listdir(image_directory):
            if filename.endswith(".jpg"):
                image_path = os.path.join(image_directory, filename)
                html.write(f"<img src='{image_path}' style='width: 50%; padding: 10px;'>\n")

        html.write("</div>\n</body>\n</html>")

    print(f"Generated {html_file} and {csv_file}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Download images and generate HTML slideshow and CSV log.")
    parser.add_argument("search_term", type=str, help="Search term for images")
    parser.add_argument("--num_images", type=int, default=5, help="Number of images to download (default: 5)")
    args = parser.parse_args()

    print("Downloading images...")
    download_dir = download_images(args.search_term, args.num_images)

    print("Creating slideshow and log...")
    create_diashow_and_log(args.search_term, download_dir)
