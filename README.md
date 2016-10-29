## Download Steps
If you are cloning the repository to get the data that I've cleaned, you probably can just type the following code in your terminal, and all the data will be in your ```Clean-Files``` folder.

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

If you want a different geographic boundary, you can use all of file unzip directory, but for processing, I'm sorry, you'll have to modify the code yourself.

### Unzip the files by following the instructions in directory labeled as such.

### Process the files into ready-to-use csvs by following the instructions in the directory labeled as such.