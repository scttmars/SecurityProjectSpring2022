# Spectre/Meltdown Vulnerabilties

The script that was used to test for the vulnerabilities can be found here: https://github.com/speed47/spectre-meltdown-checker
This repository is recommened by Intel for checking for both vulnerabilties. This script checks for a variaty of versions of both exploits.
https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/secure-coding/spectre-and-meltdown-checker-script.html

The .txt files included are results from some of the machines. Most of the machines on campus were not vulnerable to any version of the exploit. The exceptions are the newer bg machine machines: bg9 - bg14. All those machines are vulnerable to CVE-2017-5715 which is Spectre variant 2. More information about this specific variant can be found here: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5715
