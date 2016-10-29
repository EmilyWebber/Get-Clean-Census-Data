## Download Steps
If you are cloning the repository to get the data that I've cleaned, you probably can just type the following code in your terminal, and all the data will be in your ```Clean-Files``` folder. I'm assuming that you have both git and python installed on your computer. If you don't have git, you'll need to download it in some other way. If you don't have Python, you won't be able to run my cleaning scripts, but you can still use the data in the directory however you want.

```
$ git clone https://github.com/EmilyWebber/Get-Clean-Census-Data.git
```

If you need to make some change to the data that was downloaded, such as by altering the states, the years, or the level of analysis, you'll need to follow these steps.

1. Go to factfinder.census.gov

2. Click on Download Center

3. Click "I know the dataset or table(s) that I want to download"

4. You have to do this one dataset at a time. Set your program to American Community Survey. First select 2015 ACS 1-year Estimates. Click next.

5. Select a geographic type. We'll go with states. Click next.

6. Click check all. Click next.

7. It'll create a zip file with 25 items.

8. Save this in the Zip-File-Download directory. Add an underscore and the year to the zip file name.

9. You have to do this for as many years as you want data. They have ACS 1-yr estimates from 2007 - 2015. If you get all the datasets, it takes about 40 minutes of futzing on your computer to get it done.