pytest -v -s -m "sanity" --html=Reports/testReport.html --browser edge
:: pytest -v -s -m "regression" --html=Reports/Test_Report.html --browser chrome
:: pytest -v -s -m "sanity and regression" --html=Reports/Test_Report.html --browser edge
:: pytest -v -s -m "sanity or regression" --html=Reports/Test_Report.html --browser edge
:: pytest -n=3 "sanity"
:: pytest "regression" --browser chrome --count=3
