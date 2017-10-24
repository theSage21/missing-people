Missing Persons India
==============


Taken from the pdf available at [National Crime Records Bureau](http://ncrb.nic.in/MissingUidb/20170821-Missing%20Person%20Report.pdf).
We use Tabula to extract the CSVs and perform post processing on top of that.

1. Extract multiple csvs and store in `csvs` folder.
2. Run `python joiner.py`
3. Run `python cleaner.py`


Final dataset is at [cleandata.csv](cleandata.csv)
