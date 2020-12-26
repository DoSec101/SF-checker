# SF-checker
SF-checker Stand For SymFony-checker  

=======
just check if endpoint  **/_profiler** exist or not Very Simple :) 

### What is Symphony Profiler?
The profiler is a powerful development tool that gives **detailed information** about the execution of any request. **Never** enable the profiler in production environments as it will lead to major **security vulnerabilities** in your project like **logs and database credentials and any request cookies.**

#### Usage:-


**For One Site:-**

python3 SF-checker.py -u _Single Website_

EX:-

python3 SF-checker.py -u https://www.google.com

**For List Of Websites:-**

python3 SF-checker.py -U sites.txt
