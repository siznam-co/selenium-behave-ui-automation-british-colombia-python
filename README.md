### How to run with different browsers?
``` behave -D browser=browsername ```

Example:
 ```
  behave -D browser=firefox
  behave -D browser=edge
  behave -D browser=safari
  ....
  
 ```
In our automation suite, the default browser is Chrome so if you don't define any browser name 
it will start with the Chrome browser.

### How to run browsers in headless mode?
``` behave -D headless=true --tags='tagname' ```


### How to run test with specific tag names?
Example:``` behave --tags='tagname' ```


### How to rerun failed test?
``` behave @re_run.txt ```


### how to run tests in parallel with cross-browser capabilities?
```python behave_parallel.py --tags='tagname' ```

### How to run on saucelab?
``` behave -D saucelabs=true --tags='tagname' ```

### How to install allure-report?
Following commands needed to be run on powershell.
```
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
scoop install allure
```


### How to run allure-report?
Following commands needed to be run:

``` 
behave -f allure_behave.formatter:AllureFormatter -o <filename> ./features 
allure serve <filename>
```

### How to generate allure-report files?
``` allure generate ```