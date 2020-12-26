# Import Libraries.
import requests
import optparse
import termcolor
import sys
##########################
# Author :- DoSec101
# Date   :- 23/12/2020
##########################
if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, SP_checker.py requires Python 3.x\n")
    sys.exit(1)
def Checker():
    try: # Handling Errors
        # Make Parser Object.
        parser=optparse.OptionParser()
        parser.add_option("-u","--url",dest="url",help="Enter The Single Url.")
        parser.add_option("-U","--urls",dest="urls",help="File That Contain Urls.")
        parser.add_option("-v","--verbose",action="store_true",dest="verbose",help="Set Verbose True.")
        (options,arguments)=parser.parse_args()

        # Define The Options Parameter.
        url=options.url
        urls=options.urls
        verbose=options.verbose
        path="/_profiler" # Identify Endpoint.
        if options.url:# Choose if user use -u then use this.
            try:
                res=requests.get(url+path)
                if "Symfony" in res.text:
                    print(url+path,termcolor.colored(" [+] Symfony Found",'green'))
                else:
                    pass
                if res.history:
                    print(termcolor.colored("[-] False Positive",'red'),"\tRedirect to >> ",res.url,"\n")
                if verbose:
                    print(url+path,termcolor.colored(res.status_code,'red'))
            except Exception:
                print(url," [*] SSL Error Check Site.")
        if options.urls: # Choose if user use -U then use this.
            with open(urls,mode='r') as file: # Open File That Contain Urls.
                for line in file:
                    line=line.strip()
                    try:
                        response=requests.get(line+path)
                        if "Symfony" in response.text:
                            print(url+path,termcolor.colored(" [+] Symfony Found",'green'))
                        else:
                            pass
                        if verbose:
                            print(line+path,termcolor.colored(response.status_code,'red'))
                            if response.history:
                                print(termcolor.colored("[-] False Positive",'red'),"\tRedirect to >> ",response.url,"\n")
                    except Exception:
                        print(line," [*] SSL Error Check Site.")
    except KeyboardInterrupt:
        print("[*] Closing Script.!.Shutdown.")
Checker() # Call The Function.
