

import os
import requests

process = 'y'
# while loop checking the user wants to do the whole process again
while process == 'y':
    os.system('clear')
    process = 'y'
    url_valid = 'y'
    # print and URL input
    print("Welcome to IsItDown.py!")
    raw_url = input("Please write a URL or URLs you want to check. (separated by comma)\n")

    # lower & splitting the URL by , 
    url = raw_url.lower()
    url = url.split(',')

    # checking if the input is a valid URL 
    for url_number in range(len(url)):
        if url[url_number].find(".com") is -1:
            url_valid = 'n'
            print(f"{url[url_number]} is not a valid URL.")
            while True:
                process = input("Do you want to start over? y/n\n")
                if process == 'y' or process == 'n':
                    break
                else:
                    print("That's not a valid answer.")

    
    # run only if the input is a valid url
    if url_valid == 'y':
        #  deleting the blank in the URL 
        for url_number in range(len(url)):
            url[url_number] = url[url_number].strip()

        # if the URL (input) does not have http:// add 
        for url_number in range(len(url)):
            if url[url_number].find('https://') is not 0:
                url[url_number] = "https://" + url[url_number]

        # loop for the actual work
        for url_number in range(len(url)):
            # if the input is not a valid url instead of error run 'except code'
            try: 
                # requests modul checking the url is running run : 200 not run : 404
                url_n = requests.get(url[url_number])
                url_status = url_n.status_code

                if url_status is 200 :
                    print(f"{url[url_number]} is up!")
                else:
                    print(f"{url[url_number]} is down!\n")
            except:
                print(f"{url[url_number]} is down!\n")
        
        while True:
            process = input("Do you want to start over? y/n\n")
            if process == 'y' or process == 'n':
                break
            else:
                print("That's not a valid answer.")


print("k. bye!")
